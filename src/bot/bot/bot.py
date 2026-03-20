"""
StudyMate Story Agent — Telegram bot entry point.

Conversation flow:
  CLARIFYING → SUMMARISING → BREAKDOWN → CONFIRMED → CREATING → done

Required Windows environment variables:
  TELEGRAM_BOT_TOKEN  — from @BotFather on Telegram
  ANTHROPIC_API_KEY   — from console.anthropic.com
  GITHUB_TOKEN        — GitHub personal access token (repo scope)
  GITHUB_REPO         — optional, defaults to Dewaldf/studymate
"""
import logging
import os
import sys
from typing import Dict

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from bot.agent import get_conversational_response, generate_stories_json
from bot.conversation import Conversation, ConversationState
from bot.github_client import GitHubClient
from bot.story_formatter import format_story, format_stories_preview

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

_REQUIRED_ENV_VARS = [
    "TELEGRAM_BOT_TOKEN",
    "ANTHROPIC_API_KEY",
    "GITHUB_TOKEN",
]


def _load_config() -> Dict[str, str]:
    """Read credentials from Windows environment variables and fail fast if any are missing."""
    missing = [v for v in _REQUIRED_ENV_VARS if not os.environ.get(v)]
    if missing:
        for var in missing:
            logger.error("Missing required environment variable: %s", var)
        logger.error(
            "Set these in Windows: System Properties → Advanced → Environment Variables"
        )
        sys.exit(1)

    return {
        "telegram_token": os.environ["TELEGRAM_BOT_TOKEN"],
        "anthropic_api_key": os.environ["ANTHROPIC_API_KEY"],
        "github_token": os.environ["GITHUB_TOKEN"],
        "github_repo": os.environ.get("GITHUB_REPO", "Dewaldf/studymate"),
    }


# Loaded once at startup
_config: Dict[str, str] = {}

# In-memory conversation store: user_id → Conversation
_conversations: Dict[int, Conversation] = {}

WELCOME_MESSAGE = (
    "👋 Hello! I'm the *StudyMate Story Agent*.\n\n"
    "I'm an expert in EdTech and breaking down product requirements into "
    "GitHub user stories.\n\n"
    "Tell me about a feature or requirement — in plain English, as vague or "
    "as specific as you like — and I'll ask you the right questions before we "
    "create any stories.\n\n"
    "When you're happy with the proposed breakdown, just say *create stories* "
    "and I'll raise the GitHub issues for you.\n\n"
    "Use /cancel at any time to start over."
)

CANCEL_MESSAGE = "🔄 Conversation reset. Tell me about your next requirement whenever you're ready."


def _get_conversation(user_id: int) -> Conversation:
    if user_id not in _conversations:
        _conversations[user_id] = Conversation(user_id=user_id)
    return _conversations[user_id]


def _get_github_client() -> GitHubClient:
    return GitHubClient(
        token=_config["github_token"],
        repo=_config["github_repo"],
    )


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    _conversations[user_id] = Conversation(user_id=user_id)
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode="Markdown")


async def cmd_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    conv = _get_conversation(user_id)
    conv.reset()
    await update.message.reply_text(CANCEL_MESSAGE)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    text = update.message.text.strip()
    conv = _get_conversation(user_id)
    api_key = _config["anthropic_api_key"]

    # --- Confirmation trigger: create the stories ---
    if conv.state == ConversationState.BREAKDOWN and conv.is_confirmation(text):
        await _handle_story_creation(update, conv, api_key)
        return

    # --- Normal conversational turn ---
    conv.add_user_message(text)

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action="typing"
    )

    try:
        existing_issues = await _fetch_existing_issues()
        reply = await get_conversational_response(conv, api_key, existing_issues)
    except Exception as exc:
        logger.exception("Error getting Claude response")
        await update.message.reply_text(
            f"⚠️ Something went wrong: {exc}\n\nPlease try again or use /cancel."
        )
        return

    conv.add_assistant_message(reply)

    # Detect state transitions from Claude's response text
    _update_state_from_response(conv, reply)

    await update.message.reply_text(reply, parse_mode="Markdown")


async def _handle_story_creation(
    update: Update,
    conv: Conversation,
    api_key: str,
) -> None:
    conv.transition_to(ConversationState.CONFIRMED)
    await update.message.reply_text("⏳ Generating your user stories...")

    await update.get_bot().send_chat_action(
        chat_id=update.effective_chat.id, action="typing"
    )

    try:
        existing_issues = await _fetch_existing_issues()
        raw_stories = await generate_stories_json(conv, api_key, existing_issues)
    except Exception as exc:
        logger.exception("Error generating stories JSON")
        await update.message.reply_text(
            f"⚠️ Failed to generate stories: {exc}\n\nPlease use /cancel and try again."
        )
        conv.reset()
        return

    # Format stories into GitHub issue payloads
    formatted = [format_story(s) for s in raw_stories]

    await update.message.reply_text("📬 Creating GitHub issues...")
    conv.transition_to(ConversationState.CREATING)

    try:
        github = _get_github_client()
        results = await github.create_issues(formatted)
    except Exception as exc:
        logger.exception("Error creating GitHub issues")
        await update.message.reply_text(
            f"⚠️ Failed to create issues: {exc}"
        )
        conv.reset()
        return

    # Build success message
    lines = [f"✅ *{len(results)} {'issue' if len(results) == 1 else 'issues'} created:*\n"]
    for result in results:
        lines.append(f"• [#{result['number']}]({result['url']})")

    lines.append("\n_Use /cancel to start a new requirement._")
    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")
    conv.reset()


def _update_state_from_response(conv: Conversation, reply: str) -> None:
    """
    Heuristically advance the state based on keywords in Claude's reply.
    Claude's system prompt instructs it to use these signals naturally.
    """
    reply_lower = reply.lower()

    if conv.state == ConversationState.CLARIFYING:
        if any(phrase in reply_lower for phrase in [
            "let me summarise", "let me make sure", "to summarise",
            "so to confirm", "here's what i understand",
        ]):
            conv.transition_to(ConversationState.SUMMARISING)

    elif conv.state == ConversationState.SUMMARISING:
        if any(phrase in reply_lower for phrase in [
            "here's how i'd break", "i'd suggest breaking",
            "story breakdown", "stories to create",
            "here are the stories", "propose the following",
        ]):
            conv.transition_to(ConversationState.BREAKDOWN)


async def _fetch_existing_issues():
    try:
        github = _get_github_client()
        return await github.get_existing_issues()
    except Exception:
        logger.warning("Could not fetch existing issues — proceeding without them")
        return []


def main() -> None:
    global _config
    _config = _load_config()

    app = Application.builder().token(_config["telegram_token"]).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("cancel", cmd_cancel))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("StudyMate Story Agent is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
