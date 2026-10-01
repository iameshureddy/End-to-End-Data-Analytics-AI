"""
report_tool.py
--------------
LangChain Tool for saving reports to the outputs/reports folder.
"""

from pathlib import Path
from datetime import datetime

from langchain.tools import tool

from utils.logger import logger


REPORT_FOLDER = Path("outputs/reports")
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)


@tool
def save_report(title: str, content: str) -> str:
    """
    Save a text report with a timestamp.

    Args:
        title: Report title.
        content: Report content.

    Returns:
        Success message containing the saved file path.
    """

    logger.info("Report tool called.")

    try:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        safe_title = (
            title.strip()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )

        filename = f"{safe_title}_{timestamp}.txt"

        filepath = REPORT_FOLDER / filename

        with open(filepath, "w", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write(f"{title}\n")
            file.write("=" * 60 + "\n\n")
            file.write(content)

        logger.info(f"Report saved: {filepath}")

        return f"Report successfully saved to:\n{filepath}"

    except Exception as e:

        logger.exception("Failed to save report.")

        return f"Error: {str(e)}"