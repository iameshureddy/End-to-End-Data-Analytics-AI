"""
streamlit_app.py
----------------
Main Streamlit Entry
"""

from __future__ import annotations

import streamlit as st

from config_ui import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from session import initialize_session
from styles import load_css
from sidebar import render_sidebar
from chat import render_chat


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded",
)


# ==========================================================
# INITIALIZE
# ==========================================================

initialize_session()

load_css()


# ==========================================================
# SIDEBAR
# ==========================================================

render_sidebar()


# ==========================================================
# MAIN CHAT WINDOW
# ==========================================================

st.markdown(
    """
<div class="chat-header">

<div class="chat-header-left">

<h2>
🤖 MultiTool AI Assistant
</h2>

<p>
Powered by LangChain • Gemini
</p>

</div>



</div>
""",
    unsafe_allow_html=True,
)


# ==========================================================
# CHAT
# ==========================================================

render_chat()


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
<div class="chat-footer">

Built with  using
LangChain • Gemini • Streamlit

</div>
""",
    unsafe_allow_html=True,
)