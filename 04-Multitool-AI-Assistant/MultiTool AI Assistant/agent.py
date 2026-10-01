"""
LangChain MultiTool AI Assistant

This module initializes the Gemini model, registers all available tools,
and creates the LangChain agent used throughout the application.

The agent uses LangChain's native tool-calling mechanism and applies
ModelCallLimitMiddleware to prevent uncontrolled agent execution.
"""

from __future__ import annotations

# ==========================================================
# LANGCHAIN
# ==========================================================

from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain_google_genai import ChatGoogleGenerativeAI


# ==========================================================
# CONFIGURATION
# ==========================================================

from config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_ITERATIONS,
)


# ==========================================================
# TOOLS
# ==========================================================

from tools.weather_tool import get_weather
from tools.currency_tool import get_exchange_rate
from tools.calculator_tool import calculate
from tools.text_summarizer_tool import summarize_text
from tools.datetime_tool import get_current_datetime
from tools.report_tool import save_report


# ==========================================================
# GEMINI MODEL
# ==========================================================

model = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=TEMPERATURE,
)


# ==========================================================
# TOOL REGISTRY
# ==========================================================

TOOLS = [
    get_weather,
    get_exchange_rate,
    calculate,
    summarize_text,
    get_current_datetime,
    save_report,
]


# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are MultiTool AI Assistant, a professional AI assistant built using
LangChain and Google Gemini.

Your primary goal is to help users accurately, clearly, and efficiently.

You have access to the following tools:

• Weather Information
• Currency Conversion
• Mathematical Calculator
• AI Text Summarization
• Current Date & Time
• Report Generator

Instructions:

1. Always use the appropriate tool whenever it can provide a better answer.
2. Never invent weather, currency, date/time, or calculation results.
3. Keep responses professional, concise, and well formatted.
4. Use bullet points when helpful.
5. Explain calculations clearly.
6. If a tool returns an error, politely explain the issue and suggest
   trying again.
7. If multiple tools are needed, use all relevant tools before responding.
8. When generating reports, produce clean, structured output.
9. Use the native tool-calling mechanism whenever a registered tool is
   required.
10. Do not claim that a tool was used if it was not actually called.

Answer naturally and professionally.
"""


# ==========================================================
# BOUNDED AGENT EXECUTION
# ==========================================================

# ModelCallLimitMiddleware prevents uncontrolled agent loops.
#
# MAX_ITERATIONS is configured in config.py.
# Current value:
#
#     MAX_ITERATIONS = 5
#
# run_limit limits the number of model calls during one agent run.
# exit_behavior="end" gracefully terminates execution when the limit
# is reached.

iteration_limit_middleware = ModelCallLimitMiddleware(
    run_limit=MAX_ITERATIONS,
    exit_behavior="end",
)


# ==========================================================
# CREATE AGENT
# ==========================================================

agent = create_agent(
    model=model,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT,
    middleware=[
        iteration_limit_middleware,
    ],
)