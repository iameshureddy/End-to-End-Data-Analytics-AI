"""
chat.py
-------
Modern ChatGPT-style Chat Interface
"""

from __future__ import annotations

import streamlit as st


from chat_engine import ask_assistant


from config_ui import (
    QUICK_ACTIONS,
    CHAT_INPUT_PLACEHOLDER,
    SPINNER_TEXT,
)

from session import (
    get_messages,
    add_user_message,
    add_assistant_message,
)


# ==========================================================
# WELCOME SCREEN
# ==========================================================

def render_welcome():

    st.markdown(
"""<div class="welcome-container">
<h1 class="welcome-title">👋 Hi, I'm MultiTool AI</h1>

<p class="welcome-subtitle">
Your intelligent assistant powered by
<strong>LangChain</strong> and
<strong>Google Gemini</strong>.<br>
Ask anything or choose one of the suggestions below.
</p>
</div>""",
        unsafe_allow_html=True,
    )

    cols = st.columns(3)

    for index, action in enumerate(QUICK_ACTIONS):
        with cols[index % 3]:
            if st.button(
                action["label"],
                key=f"quick_action_{index}",
                use_container_width=True,
            ):
                st.session_state.quick_prompt = action["prompt"]
# ==========================================================
# CHAT HISTORY
# ==========================================================

def render_messages() -> None:
    """
    Display all chat messages.
    """

    messages = get_messages()

    for message in messages:

        role = message["role"]

        avatar = "👤" if role == "user" else "🤖"

        with st.chat_message(
            role,
            avatar=avatar,
        ):

            st.markdown(message["content"])


# ==========================================================
# PROCESS USER PROMPT
# ==========================================================

def process_prompt(prompt: str) -> None:
    """
    Send the user's prompt to the LangChain agent
    and display the response.
    """

    if not prompt.strip():
        return

    # ------------------------------------------
    # Save user message
    # ------------------------------------------

    add_user_message(prompt)

    with st.chat_message(
        "user",
        avatar="👤",
    ):
        st.markdown(prompt)

    # ------------------------------------------
    # Assistant Response
    # ------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖",
    ):

        with st.spinner(SPINNER_TEXT):

            try:

                reply, success = ask_assistant(prompt)

                if success:

                    st.markdown(reply)

                else:

                    st.error(reply)

            except Exception as e:

                reply = (
                    "⚠️ Something went wrong.\n\n"
                    f"Error: {e}"
                )

                st.error(reply)

    # ------------------------------------------
    # Save assistant message
    # ------------------------------------------

    add_assistant_message(reply)

    # Refresh interface
    st.rerun()
    # ==========================================================
# MAIN CHAT PAGE
# ==========================================================

def render_chat() -> None:
    """
    Render the complete chat interface.
    """

    messages = get_messages()

    # ------------------------------------------------------
    # Welcome Screen
    # ------------------------------------------------------

    if not messages:
        render_welcome()
    else:
        render_messages()

    # ------------------------------------------------------
    # Quick Action Support
    # ------------------------------------------------------

    quick_prompt = st.session_state.pop(
        "quick_prompt",
        None,
    )

    prompt = st.chat_input(
        CHAT_INPUT_PLACEHOLDER,
    )

    if prompt is None:
        prompt = quick_prompt

    # ------------------------------------------------------
    # Process Prompt
    # ------------------------------------------------------

    if prompt:
        process_prompt(prompt)