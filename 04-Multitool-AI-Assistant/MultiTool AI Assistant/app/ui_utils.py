"""
ui_utils.py
-----------
UI Helper Functions
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Dict, List


# ==========================================================
# TIMESTAMP
# ==========================================================

def current_timestamp() -> str:
    """
    Return formatted timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==========================================================
# EXPORT - TEXT
# ==========================================================

def export_chat_text(messages: List[Dict]) -> str:
    """
    Export conversation as plain text.
    """

    output = []

    output.append("=" * 60)
    output.append("MULTITOOL AI ASSISTANT")
    output.append("Conversation Export")
    output.append("=" * 60)
    output.append("")
    output.append(f"Generated : {current_timestamp()}")
    output.append(f"Messages  : {len(messages)}")
    output.append("")

    for message in messages:

        role = message["role"].capitalize()

        output.append(f"{role}")
        output.append("-" * len(role))
        output.append(message["content"])
        output.append("")

    return "\n".join(output)


# ==========================================================
# EXPORT - MARKDOWN
# ==========================================================

def export_chat_markdown(messages: List[Dict]) -> str:
    """
    Export conversation as Markdown.
    """

    md = []

    md.append("# MultiTool AI Assistant")
    md.append("")
    md.append("## Conversation Export")
    md.append("")
    md.append(f"**Generated:** {current_timestamp()}")
    md.append("")
    md.append("---")
    md.append("")

    for message in messages:

        role = message["role"].capitalize()

        md.append(f"## {role}")
        md.append("")
        md.append(message["content"])
        md.append("")

    return "\n".join(md)


# ==========================================================
# EXPORT - JSON
# ==========================================================

def export_chat_json(messages: List[Dict]) -> str:
    """
    Export conversation as JSON.
    """

    export = {

        "application": "MultiTool AI Assistant",

        "generated": current_timestamp(),

        "message_count": len(messages),

        "messages": messages,

    }

    return json.dumps(
        export,
        indent=4,
        ensure_ascii=False,
    )


# ==========================================================
# CHAT SUMMARY
# ==========================================================

def conversation_summary(messages: List[Dict]) -> Dict:
    """
    Return conversation statistics.
    """

    users = sum(
        1
        for m in messages
        if m["role"] == "user"
    )

    assistants = sum(
        1
        for m in messages
        if m["role"] == "assistant"
    )

    return {

        "total_messages": len(messages),

        "user_messages": users,

        "assistant_messages": assistants,

        "generated": current_timestamp(),

    }


# ==========================================================
# COPY FORMAT
# ==========================================================

def conversation_for_copy(messages: List[Dict]) -> str:
    """
    Format conversation for copy/paste.
    """

    lines = []

    for message in messages:

        role = message["role"].upper()

        lines.append(f"[{role}]")
        lines.append(message["content"])
        lines.append("")

    return "\n".join(lines)


# ==========================================================
# EMPTY CHAT
# ==========================================================

def is_chat_empty(messages: List[Dict]) -> bool:
    """
    Check whether conversation exists.
    """

    return len(messages) == 0


# ==========================================================
# FILE NAME
# ==========================================================

def export_filename(extension: str) -> str:
    """
    Generate export filename.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"multitool_chat_{timestamp}.{extension}"