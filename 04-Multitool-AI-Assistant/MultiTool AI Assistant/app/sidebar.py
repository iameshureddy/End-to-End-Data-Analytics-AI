"""
sidebar.py
----------
ChatGPT-style Sidebar
"""

from __future__ import annotations

import streamlit as st

from session import (
    create_new_chat,
    set_active_chat,
    all_conversations,
    active_chat,
    search_conversations,
)

from ui_utils import (
    export_chat_text,
    export_chat_markdown,
    export_chat_json,
)


def render_sidebar():

    with st.sidebar:

        # ======================================================
        # LOGO
        # ======================================================

        st.markdown(
            """
<div class="sidebar-header">

<h2 style="margin-bottom:0;">
🤖 MultiTool AI
</h2>

<p style="margin-top:0;color:#94A3B8;font-size:13px;">
AI Assistant
</p>

</div>
""",
            unsafe_allow_html=True,
        )

        # ======================================================
        # NEW CHAT
        # ======================================================

        if st.button(
            "➕ New Chat",
            use_container_width=True,
            type="primary",
        ):
            create_new_chat()
            st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # ======================================================
        # SEARCH
        # ======================================================

        search = st.text_input(
            "",
            placeholder="🔍 Search conversations...",
            key="chat_search",
        )

        st.markdown(
            """
<div style="margin:18px 0 10px 0;
font-size:13px;
font-weight:600;
color:#94A3B8;">
CONVERSATIONS
</div>
""",
            unsafe_allow_html=True,
        )

        # ======================================================
        # CONVERSATION LIST
        # ======================================================

        chats = search_conversations(search)

        current_chat = active_chat()

        if not chats:

            st.caption("No conversations found.")

        else:

            for chat in chats:

                title = chat["title"]

                if len(title) > 28:
                    title = title[:28] + "..."

                active = (
                    chat["id"] == current_chat["id"]
                )

                label = f"💬 {title}"

                

                if st.button(
                    label,
                    key=f"chat_{chat['id']}",
                    use_container_width=True,
                ):
                    set_active_chat(chat["id"])
                    st.rerun()

        st.markdown("---")

        # ======================================================
        # EXPORT
        # ======================================================

        st.markdown(
            """
<div style="font-size:13px;
font-weight:600;
color:#94A3B8;
margin-bottom:10px;">
EXPORT CURRENT CHAT
</div>
""",
            unsafe_allow_html=True,
        )

        messages = current_chat["messages"]

        st.download_button(
            "📄 Export TXT",
            export_chat_text(messages),
            "conversation.txt",
            use_container_width=True,
        )

        st.download_button(
            "📝 Export Markdown",
            export_chat_markdown(messages),
            "conversation.md",
            use_container_width=True,
        )

        st.download_button(
            "📦 Export JSON",
            export_chat_json(messages),
            "conversation.json",
            use_container_width=True,
        )

        st.markdown("---")

        # ======================================================
        # FOOTER
        # ======================================================

        st.caption(
            "LangChain • Gemini • Streamlit"
        )