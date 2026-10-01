"""
Native tool-call demonstration for the MultiTool AI Assistant.

This test explicitly displays:
1. User query
2. Native LangChain tool call
3. Tool name
4. Tool arguments
5. Tool result
6. Final assistant answer
"""

from agent import agent


# ==========================================================
# TEST QUERIES
# ==========================================================

questions = [
    "What is 50 * 120?",
    "What is today's date and time?",
    "Convert USD to INR.",
]


# ==========================================================
# RUN TESTS
# ==========================================================

for q in questions:

    print("\n" + "=" * 80)
    print("USER QUERY:")
    print(q)

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": q,
                }
            ]
        }
    )

    # ------------------------------------------------------
    # Native Tool-Call Trace
    # ------------------------------------------------------

    print("\nNATIVE TOOL-CALL TRACE:")

    tool_call_found = False

    for message in response["messages"]:

        # AIMessage containing native tool calls
        if hasattr(message, "tool_calls") and message.tool_calls:

            for tool_call in message.tool_calls:

                tool_call_found = True

                print("\nTool:")
                print(tool_call["name"])

                print("\nArguments:")
                print(tool_call["args"])

                # Optional tool-call ID for traceability
                if "id" in tool_call:
                    print("\nTool Call ID:")
                    print(tool_call["id"])

        # --------------------------------------------------
        # ToolMessage containing the actual tool result
        # --------------------------------------------------

        if getattr(message, "type", None) == "tool":

            print("\nTool Result:")
            print(message.content)

    if not tool_call_found:
        print("\nNo native tool call detected.")

    # ------------------------------------------------------
    # Final Answer
    # ------------------------------------------------------

    print("\nFINAL ANSWER:")

    final_message = response["messages"][-1]

    if isinstance(final_message.content, list):

        for item in final_message.content:

            if (
                isinstance(item, dict)
                and item.get("type") == "text"
            ):
                print(item["text"])

    else:
        print(final_message.content)