"""
session.py
----------
ChatGPT-style Session & Conversation Management
"""

from __future__ import annotations

from typing import Dict, List
from uuid import uuid4

import streamlit as st


# ==========================================================
# DEFAULT STATE
# ==========================================================

DEFAULT_STATE = {
    "conversations": [],
    "active_chat_id": None,
    "quick_prompt": None,
    "theme": "dark",
    "search_query": "",
}


# ==========================================================
# INITIALIZATION
# ==========================================================

def initialize_session() -> None:
    """
    Initialize Streamlit session.
    """

    for key, value in DEFAULT_STATE.items():

        if key not in st.session_state:

            if isinstance(value, list):
                st.session_state[key] = value.copy()

            elif isinstance(value, dict):
                st.session_state[key] = value.copy()

            else:
                st.session_state[key] = value

    if not st.session_state.conversations:
        create_new_chat()


# ==========================================================
# CHAT CREATION
# ==========================================================

def create_new_chat(title: str = "New Chat") -> str:
    """
    Create a new conversation.
    """

    chat_id = str(uuid4())

    conversation = {
        "id": chat_id,
        "title": title,
        "messages": [],
    }

    st.session_state.conversations.insert(0, conversation)

    st.session_state.active_chat_id = chat_id

    return chat_id


# ==========================================================
# ACTIVE CHAT
# ==========================================================

def active_chat() -> Dict:
    """
    Return active conversation.
    """

    for chat in st.session_state.conversations:

        if chat["id"] == st.session_state.active_chat_id:
            return chat

    create_new_chat()

    return st.session_state.conversations[0]


def set_active_chat(chat_id: str) -> None:
    """
    Switch active conversation.
    """

    st.session_state.active_chat_id = chat_id


# ==========================================================
# CHAT HELPERS
# ==========================================================

def get_messages() -> List[Dict]:
    """
    Messages of current chat.
    """

    return active_chat()["messages"]


def message_count() -> int:
    return len(get_messages())


def last_message() -> Dict | None:

    msgs = get_messages()

    if not msgs:
        return None

    return msgs[-1]


# ==========================================================
# AUTO TITLE
# ==========================================================

def _update_title_from_prompt(prompt: str) -> None:

    chat = active_chat()

    if chat["title"] != "New Chat":
        return

    title = " ".join(prompt.strip().split()[:5])

    if len(title) > 40:
        title = title[:40]

    chat["title"] = title or "New Chat"


# ==========================================================
# MESSAGE FUNCTIONS
# ==========================================================

def add_user_message(message: str) -> None:

    active_chat()["messages"].append(
        {
            "role": "user",
            "content": message,
        }
    )

    _update_title_from_prompt(message)


def add_assistant_message(message: str) -> None:

    active_chat()["messages"].append(
        {
            "role": "assistant",
            "content": message,
        }
    )


def add_system_message(message: str) -> None:

    active_chat()["messages"].append(
        {
            "role": "system",
            "content": message,
        }
    )


# ==========================================================
# CONVERSATIONS
# ==========================================================

def all_conversations() -> List[Dict]:
    return st.session_state.conversations


def search_conversations(query: str) -> List[Dict]:

    if not query.strip():
        return st.session_state.conversations

    query = query.lower()

    return [
        c
        for c in st.session_state.conversations
        if query in c["title"].lower()
    ]


def delete_chat(chat_id: str) -> None:

    st.session_state.conversations = [

        c

        for c in st.session_state.conversations

        if c["id"] != chat_id

    ]

    if not st.session_state.conversations:
        create_new_chat()

    st.session_state.active_chat_id = (
        st.session_state.conversations[0]["id"]
    )


# ==========================================================
# CLEAR CURRENT CHAT
# ==========================================================

def clear_chat() -> None:

    chat = active_chat()

    chat["messages"] = []

    chat["title"] = "New Chat"


# ==========================================================
# EXPORT
# ==========================================================

def conversation_text() -> str:

    lines = []

    for msg in get_messages():

        role = msg["role"].capitalize()

        lines.append(f"{role}: {msg['content']}")

    return "\n\n".join(lines)


# ==========================================================
# STATS
# ==========================================================

def chat_statistics() -> Dict:

    msgs = get_messages()

    users = sum(1 for m in msgs if m["role"] == "user")

    assistants = sum(
        1 for m in msgs if m["role"] == "assistant"
    )

    return {

        "total_messages": len(msgs),

        "user_messages": users,

        "assistant_messages": assistants,

        "total_conversations": len(
            st.session_state.conversations
        ),

    }


# ==========================================================
# STATUS
# ==========================================================

def session_active() -> bool:

    return len(get_messages()) > 0