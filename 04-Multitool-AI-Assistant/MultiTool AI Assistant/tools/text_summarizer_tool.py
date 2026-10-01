"""
text_summarizer_tool.py
-----------------------
LangChain Tool for summarizing text using Google Gemini.
"""

from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GOOGLE_API_KEY

from utils.logger import logger


# ==========================================================
# Initialize Gemini LLM
# ==========================================================
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2,
)


# ==========================================================
# Text Summarization Tool
# ==========================================================
@tool
def summarize_text(text: str) -> str:
    """
    Summarize the given text into concise bullet points.

    Args:
        text: Input text.

    Returns:
        Bullet-point summary.
    """

    logger.info("Summarizer tool called.")

    if not text.strip():
        return "Error: No text provided for summarization."

    prompt = f"""
You are an expert text summarizer.

Instructions:
- Read the given text carefully.
- Produce a concise summary.
- Use 5–8 bullet points.
- Preserve important facts.
- Do not add new information.
- Keep each bullet short and clear.

Text:
{text}
"""

    try:

        response = llm.invoke(prompt)

        logger.info("Summarization completed successfully.")

        # --------------------------------------------------
        # Extract plain text from Gemini response
        # --------------------------------------------------
        if hasattr(response, "content"):

            if isinstance(response.content, str):
                return response.content.strip()

            if isinstance(response.content, list):

                parts = []

                for item in response.content:

                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            parts.append(item.get("text", ""))

                    elif hasattr(item, "text"):
                        parts.append(item.text)

                return "\n".join(parts).strip()

        return str(response)

    except Exception as e:

        logger.exception("Summarizer tool failed.")

        error_message = str(e)

        if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:
            return (
                "Gemini API rate limit exceeded.\n\n"
                "Please wait about one minute and try again."
            )

        return f"Summarization failed.\n\nReason: {error_message}"