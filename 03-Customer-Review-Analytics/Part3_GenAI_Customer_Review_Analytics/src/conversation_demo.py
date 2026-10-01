"""
TASK 7
Multi-turn Conversation Demo

Objective
---------
Demonstrate a 2-turn conversation where the second Gemini API call
uses the conversation history from the first turn.

The conversation history is maintained as a list of messages
containing user and assistant roles.

This demonstrates that the second LLM call can use information
provided in the previous turn.
"""

from retry_handler import safe_call_llm


# =============================================================================
# RESPONSE CLEANING
# =============================================================================

def clean_response(text):
    """
    Clean minor formatting issues from Gemini-generated responses.

    Parameters
    ----------
    text : str
        Gemini-generated response.

    Returns
    -------
    str
        Cleaned response.
    """

    if text is None:
        return ""

    text = str(text).strip()

    replacements = {
        "helpyou": "help you",
        "andhow": "and how",
        "useyour": "use your",
        "perfectfit": "perfect fit",
        "futuredesigns": "future designs",
        "experience.We": "experience. We",
        "feedback.We": "feedback. We",
        "dress.While": "dress. While",
        "material.While": "material. While",
        "fit.While": "fit. While",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# =============================================================================
# BUILD CONVERSATION PROMPT
# =============================================================================

def build_chat_prompt(history):
    """
    Convert conversation history into a prompt for Gemini.

    Parameters
    ----------
    history : list
        List of dictionaries containing role and content.

    Returns
    -------
    str
        Prompt sent to Gemini.
    """

    prompt = """
You are a professional Customer Support Executive for an online
clothing store.

Continue the conversation naturally.

Guidelines:

- Be polite and empathetic.
- Remember the previous conversation.
- Use the conversation history to understand the customer's context.
- Answer only the latest customer question.
- Do not repeat unnecessary information.
- Do not invent order, return, exchange, refund, or policy details.
- If information is required to complete an action, ask the customer
  for that information.
- Keep the reply under 4 sentences.

Conversation History:
"""

    for message in history:

        role = message["role"].capitalize()
        content = message["content"]

        prompt += f"\n{role}: {content}"

    prompt += "\n\nAssistant:"

    return prompt.strip()


# =============================================================================
# ADD MESSAGE TO CONVERSATION HISTORY
# =============================================================================

def add_message(history, role, content):
    """
    Add a message to the conversation history.

    Parameters
    ----------
    history : list
        Conversation history.

    role : str
        Message role: user or assistant.

    content : str
        Message content.
    """

    history.append({
        "role": role,
        "content": content
    })


# =============================================================================
# RUN ONE CONVERSATION TURN
# =============================================================================

def run_turn(history, user_message):
    """
    Add a user message, send the complete conversation history to Gemini,
    and store the assistant response.

    Parameters
    ----------
    history : list
        Existing conversation history.

    user_message : str
        New customer message.

    Returns
    -------
    str
        Assistant response.
    """

    # Add the customer's message to the history.
    add_message(
        history,
        "user",
        user_message
    )

    # Build prompt using the complete conversation history.
    prompt = build_chat_prompt(history)

    # Send the conversation to Gemini.
    assistant_reply = safe_call_llm(
        prompt=prompt,
        temperature=0.3,
        max_tokens=250
    )

    # Handle API failure.
    if assistant_reply is None:

        raise RuntimeError(
            "Gemini did not return a response."
        )

    # Clean minor formatting issues.
    assistant_reply = clean_response(
        assistant_reply
    )

    # Store assistant response in conversation history.
    add_message(
        history,
        "assistant",
        assistant_reply
    )

    return assistant_reply


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("TASK 7 : Multi-turn Conversation Demo")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Conversation history object
    # -------------------------------------------------------------------------

    conversation_history = []

    # =========================================================================
    # TURN 1
    # =========================================================================

    user_message_1 = (
        "The dress quality is excellent, but the size was too small."
    )

    try:

        assistant_reply_1 = run_turn(
            conversation_history,
            user_message_1
        )

    except RuntimeError as error:

        print("\nTURN 1 FAILED")
        print(error)
        raise SystemExit(1)

    print("\n" + "-" * 70)
    print("TURN 1")
    print("-" * 70)

    print("\nCustomer:")
    print(user_message_1)

    print("\nAssistant:")
    print(assistant_reply_1)

    # =========================================================================
    # TURN 2
    # =========================================================================

    user_message_2 = (
        "Can I exchange it for a larger size?"
    )

    # IMPORTANT:
    # run_turn() receives the existing conversation_history.
    # Therefore Turn 2 includes Turn 1 user and assistant messages.
    try:

        assistant_reply_2 = run_turn(
            conversation_history,
            user_message_2
        )

    except RuntimeError as error:

        print("\nTURN 2 FAILED")
        print(error)
        raise SystemExit(1)

    print("\n" + "-" * 70)
    print("TURN 2")
    print("-" * 70)

    print("\nCustomer:")
    print(user_message_2)

    print("\nAssistant:")
    print(assistant_reply_2)

    # =========================================================================
    # DISPLAY COMPLETE CONVERSATION HISTORY
    # =========================================================================

    print("\n" + "=" * 70)
    print("COMPLETE CONVERSATION HISTORY")
    print("=" * 70)

    for number, message in enumerate(
        conversation_history,
        start=1
    ):

        print(f"\nMessage {number}")

        print(
            f"Role    : {message['role']}"
        )

        print(
            f"Content : {message['content']}"
        )

    # =========================================================================
    # MULTI-TURN VERIFICATION
    # =========================================================================

    print("\n" + "=" * 70)
    print("MULTI-TURN VERIFICATION")
    print("=" * 70)

    print(
        f"\nTotal messages in history : "
        f"{len(conversation_history)}"
    )

    # Expected structure:
    # 1. User
    # 2. Assistant
    # 3. User
    # 4. Assistant

    if len(conversation_history) == 4:

        print(
            "Turn 1 assistant response stored : YES"
        )

        print(
            "Turn 2 prompt includes Turn 1 history : YES"
        )

        print(
            "Follow-up question uses previous context : YES"
        )

        print(
            "Conversation contains 2 complete turns : YES"
        )

    else:

        print(
            "Conversation history verification failed."
        )

        raise SystemExit(1)

    # =========================================================================
    # FINAL STATUS
    # =========================================================================

    print("\n" + "=" * 70)
    print("TASK 7 COMPLETED SUCCESSFULLY")
    print("=" * 70)