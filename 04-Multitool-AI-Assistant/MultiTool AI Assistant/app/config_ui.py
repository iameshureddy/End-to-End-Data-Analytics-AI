"""
config_ui.py
------------
UI Configuration
"""

# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "MultiTool AI Assistant"

APP_VERSION = "3.0.0"

PAGE_TITLE = APP_NAME

PAGE_ICON = "🤖"

LAYOUT = "wide"


# ==========================================================
# BRANDING
# ==========================================================

COMPANY = "MultiTool AI"

TAGLINE = (
    "An intelligent assistant powered by LangChain and Google Gemini."
)

POWERED_BY = (
    "LangChain • Google Gemini"
)

FOOTER_TEXT = (
    "© 2026 MultiTool AI Assistant"
)



# ==========================================================
# QUICK ACTIONS
# ==========================================================

QUICK_ACTIONS = [

    {
        "label": "🌤 Weather",
        "prompt": "What is the weather in Hyderabad today?"
    },

    {
        "label": "💱 Currency",
        "prompt": "Convert 100 USD to INR."
    },

    {
        "label": "🧮 Calculator",
        "prompt": "Calculate ((125 * 18) + 325) / 5."
    },

    {
        "label": "📝 Summarize",
        "prompt": (
            "Summarize the following text into bullet points:\n\n"
            "Paste your text here."
        ),
    },

    {
        "label": "📅 Date & Time",
        "prompt": "What is today's date and current time?"
    },

    {
        "label": "📄 Report",
        "prompt": "Generate a professional weekly project report."
    },

]


# ==========================================================
# CHAT
# ==========================================================

CHAT_INPUT_PLACEHOLDER = (
    "Message MultiTool AI..."
)

SPINNER_TEXT = (
    "Thinking..."
)

MAX_HISTORY = 100


# ==========================================================
# SIDEBAR
# ==========================================================

SIDEBAR_TITLE = (
    "MultiTool AI"
)

SIDEBAR_SUBTITLE = (
    "Conversation History"
)


# ==========================================================
# COLORS
# ==========================================================

PRIMARY_COLOR = "#4F46E5"

BACKGROUND_COLOR = "#0F172A"

SIDEBAR_COLOR = "#111827"

CARD_COLOR = "#1E293B"

ACCENT_COLOR = "#22C55E"

TEXT_COLOR = "#F8FAFC"

MUTED_TEXT = "#94A3B8"


# ==========================================================
# EXPORT
# ==========================================================

EXPORT_FILENAME = (
    "conversation"
)


# ==========================================================
# FRAMEWORK
# ==========================================================

FRAMEWORK = "LangChain"

MODEL = "Google Gemini"

FRONTEND = "Streamlit"