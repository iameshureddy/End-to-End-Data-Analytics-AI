"""
passthrough_chain.py
--------------------
RunnablePassthrough example using LangChain Expression Language (LCEL).
"""

from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
)


# ==========================================================
# Gemini LLM
# ==========================================================
llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=TEMPERATURE,
)


# ==========================================================
# Prompt Template
# ==========================================================
prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer the user's question clearly.

Question:
{question}
"""
)


# ==========================================================
# RunnablePassthrough Chain
# ==========================================================
passthrough_chain = (
    {"question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)