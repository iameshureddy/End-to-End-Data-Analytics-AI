"""
datetime_tool.py
----------------
LangChain Tool to get the current date and time.
"""

from datetime import datetime

from langchain.tools import tool

from utils.logger import logger


@tool
def get_current_datetime() -> str:
    """
    Returns the current local date and time.
    """

    logger.info("Datetime tool called.")

    try:

        now = datetime.now()

        current_time = now.strftime(
            "%A, %d %B %Y | %I:%M:%S %p"
        )

        logger.info("Datetime generated successfully.")

        return current_time

    except Exception as e:

        logger.exception("Datetime tool failed.")

        return f"Error: {e}"