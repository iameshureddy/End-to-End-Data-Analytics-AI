"""
conversation_memory.py
----------------------
Stores conversation history for the MultiTool AI Assistant.
"""

from langchain_core.chat_history import InMemoryChatMessageHistory

# ==========================================================
# Global Conversation Memory
# ==========================================================
chat_memory = InMemoryChatMessageHistory()