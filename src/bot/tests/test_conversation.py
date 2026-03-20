"""
Tests for the conversation state machine.
The agent moves through defined states and never skips ahead.
"""
import pytest
from bot.conversation import Conversation, ConversationState


class TestConversationState:

    def test_state_enum_has_required_states(self):
        states = [s.value for s in ConversationState]
        assert "clarifying" in states
        assert "summarising" in states
        assert "breakdown" in states
        assert "confirmed" in states
        assert "creating" in states


class TestConversation:

    def test_new_conversation_starts_in_clarifying_state(self):
        conv = Conversation(user_id=123)
        assert conv.state == ConversationState.CLARIFYING

    def test_new_conversation_has_empty_history(self):
        conv = Conversation(user_id=123)
        assert conv.messages == []

    def test_user_id_is_stored(self):
        conv = Conversation(user_id=456)
        assert conv.user_id == 456

    def test_add_user_message_appends_to_history(self):
        conv = Conversation(user_id=123)
        conv.add_user_message("I want students to log in")
        assert len(conv.messages) == 1
        assert conv.messages[0]["role"] == "user"
        assert conv.messages[0]["content"] == "I want students to log in"

    def test_add_assistant_message_appends_to_history(self):
        conv = Conversation(user_id=123)
        conv.add_assistant_message("What type of student are you thinking of?")
        assert len(conv.messages) == 1
        assert conv.messages[0]["role"] == "assistant"

    def test_is_ready_to_create_false_when_not_confirmed(self):
        conv = Conversation(user_id=123)
        assert conv.is_ready_to_create() is False

    def test_is_ready_to_create_false_in_breakdown_state(self):
        conv = Conversation(user_id=123)
        conv.state = ConversationState.BREAKDOWN
        assert conv.is_ready_to_create() is False

    def test_is_ready_to_create_true_when_confirmed(self):
        conv = Conversation(user_id=123)
        conv.state = ConversationState.CONFIRMED
        assert conv.is_ready_to_create() is True

    def test_reset_clears_state_and_history(self):
        conv = Conversation(user_id=123)
        conv.add_user_message("some requirement")
        conv.state = ConversationState.BREAKDOWN
        conv.reset()
        assert conv.state == ConversationState.CLARIFYING
        assert conv.messages == []

    def test_reset_preserves_user_id(self):
        conv = Conversation(user_id=789)
        conv.reset()
        assert conv.user_id == 789

    def test_pending_stories_initially_empty(self):
        conv = Conversation(user_id=123)
        assert conv.pending_stories == []

    def test_set_pending_stories_stores_stories(self):
        conv = Conversation(user_id=123)
        stories = [{"title": "Story 1"}, {"title": "Story 2"}]
        conv.set_pending_stories(stories)
        assert conv.pending_stories == stories

    def test_transition_to_summarising(self):
        conv = Conversation(user_id=123)
        conv.state = ConversationState.CLARIFYING
        conv.transition_to(ConversationState.SUMMARISING)
        assert conv.state == ConversationState.SUMMARISING

    def test_transition_to_breakdown(self):
        conv = Conversation(user_id=123)
        conv.state = ConversationState.SUMMARISING
        conv.transition_to(ConversationState.BREAKDOWN)
        assert conv.state == ConversationState.BREAKDOWN

    def test_transition_to_confirmed(self):
        conv = Conversation(user_id=123)
        conv.state = ConversationState.BREAKDOWN
        conv.transition_to(ConversationState.CONFIRMED)
        assert conv.state == ConversationState.CONFIRMED


class TestConversationTriggers:

    def test_is_confirmation_phrase_true_for_create_stories(self):
        conv = Conversation(user_id=123)
        assert conv.is_confirmation("create stories") is True

    def test_is_confirmation_phrase_case_insensitive(self):
        conv = Conversation(user_id=123)
        assert conv.is_confirmation("Create Stories") is True
        assert conv.is_confirmation("CREATE STORIES") is True

    def test_is_confirmation_false_for_random_text(self):
        conv = Conversation(user_id=123)
        assert conv.is_confirmation("yes please") is False
        assert conv.is_confirmation("ok") is False
        assert conv.is_confirmation("looks good") is False

    def test_is_confirmation_true_for_yes_create(self):
        conv = Conversation(user_id=123)
        assert conv.is_confirmation("yes create") is True

    def test_is_confirmation_true_for_go_ahead(self):
        conv = Conversation(user_id=123)
        assert conv.is_confirmation("go ahead") is True
