from agent import agent
from memory.conversation_memory import chat_memory

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)


def ask(question: str):
    """Send a message to the agent while maintaining conversation memory."""

    # Store user message
    chat_memory.add_message(
        HumanMessage(content=question)
    )

    # Invoke the agent with conversation history
    response = agent.invoke(
        {
            "messages": chat_memory.messages
        }
    )

    # Get the final response
    final_message = response["messages"][-1]

    # Extract text from Gemini response
    if isinstance(final_message.content, list):

        answer = ""

        for item in final_message.content:

            if isinstance(item, dict) and item.get("type") == "text":
                answer += item.get("text", "")

            elif hasattr(item, "text"):
                answer += item.text

    else:
        answer = str(final_message.content)

    # Save assistant response to memory
    chat_memory.add_message(
        AIMessage(content=answer)
    )

    # Display conversation
    print("\n" + "=" * 70)
    print("USER:")
    print(question)

    print("\nASSISTANT:")
    print(answer)


# ==========================================================
# Conversation Test
# ==========================================================

ask("Hello!")

ask("My name is Bhuvaneswari.")

ask("What is my name?")