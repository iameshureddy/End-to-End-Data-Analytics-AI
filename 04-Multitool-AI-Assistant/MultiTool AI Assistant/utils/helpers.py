"""
helpers.py
-----------
Reusable helper functions for the MultiTool AI Assistant.
"""

from pathlib import Path
from datetime import datetime
import json

from utils.logger import logger


def ensure_directory(path: Path):
    """
    Create a directory if it does not exist.
    """
    path.mkdir(parents=True, exist_ok=True)


def current_timestamp():
    """
    Return current timestamp as a formatted string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_text_report(content: str, output_path: Path):
    """
    Save text content into a report file.
    """
    ensure_directory(output_path.parent)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    logger.info(f"Report saved: {output_path}")


def save_json(data: dict, output_path: Path):
    """
    Save dictionary as a JSON file.
    """
    ensure_directory(output_path.parent)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logger.info(f"JSON saved: {output_path}")


def separator():
    """
    Print a separator line.
    """
    print("-" * 60)