"""
Stateful conditional workflow using LangChain Expression Language (LCEL).

This module demonstrates:
1. RunnablePassthrough
2. RunnablePassthrough.assign()
3. State enrichment
4. RunnableBranch conditional routing
"""

from langchain_core.runnables import (
    RunnableBranch,
    RunnableLambda,
    RunnablePassthrough,
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
)


# ==========================================================
# Gemini Model
# ==========================================================

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=TEMPERATURE,
)


# ==========================================================
# Greeting Response
# ==========================================================

greeting_chain = RunnableLambda(
    lambda state: (
        "Hello! Welcome to the MultiTool AI Assistant.\n\n"
        "I can help with:\n"
        "- Weather\n"
        "- Currency Conversion\n"
        "- Calculations\n"
        "- Text Summarization\n"
        "- Date & Time\n"
        "- Report Generation"
    )
)


# ==========================================================
# Query Classification
# ==========================================================

def classify_query(state):
    """
    Classify the incoming query using the current workflow state.
    """

    question = state["question"].lower().strip()

    greeting_inputs = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    ]

    if question in greeting_inputs:
        return "greeting"

    return "general"


# ==========================================================
# General LLM Chain
# ==========================================================

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer the following question clearly and concisely.

Question:
{question}
"""
)

llm_chain = (
    prompt
    | llm
    | StrOutputParser()
)


# ==========================================================
# Stateful Workflow
# ==========================================================

# Step 1:
# Preserve the original user input as the "question" field.

state_input = {
    "question": RunnablePassthrough()
}


# Step 2:
# Enrich the state with a classification result.

stateful_workflow = (
    state_input
    | RunnablePassthrough.assign(
        category=RunnableLambda(classify_query)
    )
)


# ==========================================================
# Conditional Routing
# ==========================================================

branch_chain = stateful_workflow | RunnableBranch(

    # Greeting route
    (
        lambda state: state["category"] == "greeting",
        greeting_chain,
    ),

    # Default route
    llm_chain,
)