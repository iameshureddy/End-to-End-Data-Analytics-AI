"""
chat_engine.py
--------------
Handles communication between the Streamlit UI and the LangChain agent.
"""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Tuple, Any

# ==========================================================
# PROJECT PATH
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ==========================================================
# IMPORTS
# ==========================================================

from agent import agent
from memory.conversation_memory import chat_memory

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
)


# ==========================================================
# RESPONSE PARSER
# ==========================================================

def extract_text(content: Any) -> str:
    """
    Convert LangChain/Gemini response into plain text.
    """

    if content is None:
        return ""

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):

        parts = []

        for item in content:

            if isinstance(item, str):
                parts.append(item)

            elif isinstance(item, dict):

                if item.get("type") == "text":
                    parts.append(item.get("text", ""))

                elif "text" in item:
                    parts.append(str(item["text"]))

            else:
                parts.append(str(item))

        return "\n".join(parts).strip()

    if hasattr(content, "content"):
        return extract_text(content.content)

    return str(content).strip()


# ==========================================================
# MEMORY
# ==========================================================

def conversation_history():
    """
    Return current LangChain conversation history.
    """

    return chat_memory.messages


def clear_memory() -> None:
    """
    Clear LangChain memory.
    """

    try:

        chat_memory.clear()

    except Exception:

        try:
            chat_memory.messages.clear()
        except Exception:
            pass


# ==========================================================
# MAIN CHAT
# ==========================================================

def ask_assistant(user_message: str) -> Tuple[str, bool]:
    """
    Send a prompt to the LangChain agent.

    Returns
    -------
    (reply, success)
    """

    try:

        # ----------------------------------------
        # Store User Message
        # ----------------------------------------

        chat_memory.add_message(
            HumanMessage(content=user_message)
        )

        # ----------------------------------------
        # Invoke Agent
        # ----------------------------------------

        result = agent.invoke(
            {
                "messages": chat_memory.messages
            }
        )

        # ----------------------------------------
        # DEBUG - Native LangChain Tool Calls
        # ----------------------------------------

        from pprint import pprint

        print("\n================ AGENT RESULT ================\n")
        pprint(result)

        if isinstance(result, dict):

            messages = result.get("messages", [])

            for message in messages:

                print("\n----------------------------------------")
                print(type(message))
                print(message)

                if hasattr(message, "tool_calls") and message.tool_calls:
                    print("\nTool Calls:")
                    pprint(message.tool_calls)

                if hasattr(message, "additional_kwargs"):
                    print("\nAdditional Kwargs:")
                    pprint(message.additional_kwargs)

                if hasattr(message, "response_metadata"):
                    print("\nResponse Metadata:")
                    pprint(message.response_metadata)

        print("\n==============================================\n")

        reply = ""

        # ----------------------------------------
        # Extract Assistant Response
        # ----------------------------------------

        if isinstance(result, dict):

            messages = result.get("messages", [])

            if messages:

                ai_message = None

                for message in reversed(messages):

                    if isinstance(message, AIMessage):
                        ai_message = message
                        break

                if ai_message is None:
                    ai_message = messages[-1]

                reply = extract_text(ai_message.content)

        else:

            reply = extract_text(result)

        # ----------------------------------------
        # Empty Response
        # ----------------------------------------

        if not reply.strip():

            reply = (
                "I couldn't generate a response. "
                "Please try again."
            )

        # ----------------------------------------
        # Save Assistant Response
        # ----------------------------------------

        chat_memory.add_message(
            AIMessage(content=reply)
        )

        return reply, True

    except Exception as error:

        message = (
            "⚠️ **Agent Error**\n\n"
            f"{error}"
        )

        return message, False