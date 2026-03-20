"""
Conversation state machine for the StudyMate story agent.
Each Telegram user gets their own Conversation instance stored in memory.
"""
from enum import Enum
from typing import List, Dict, Any


class ConversationState(Enum):
    CLARIFYING = "clarifying"
    SUMMARISING = "summarising"
    BREAKDOWN = "breakdown"
    CONFIRMED = "confirmed"
    CREATING = "creating"


CONFIRMATION_PHRASES = [
    "create stories",
    "yes create",
    "go ahead",
]


class Conversation:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.state = ConversationState.CLARIFYING
        self.messages: List[Dict[str, str]] = []
        self.pending_stories: List[Dict[str, Any]] = []

    def add_user_message(self, content: str) -> None:
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str) -> None:
        self.messages.append({"role": "assistant", "content": content})

    def is_ready_to_create(self) -> bool:
        return self.state == ConversationState.CONFIRMED

    def set_pending_stories(self, stories: List[Dict[str, Any]]) -> None:
        self.pending_stories = stories

    def transition_to(self, state: ConversationState) -> None:
        self.state = state

    def is_confirmation(self, text: str) -> bool:
        normalised = text.strip().lower()
        return any(phrase in normalised for phrase in CONFIRMATION_PHRASES)

    def reset(self) -> None:
        self.state = ConversationState.CLARIFYING
        self.messages = []
        self.pending_stories = []
