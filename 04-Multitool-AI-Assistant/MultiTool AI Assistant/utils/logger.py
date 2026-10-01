"""
logger.py
----------
Central logging configuration for the MultiTool AI Assistant.
"""

import logging
from config import LOG_FILE

# Create logger
logger = logging.getLogger("MultiToolAI")

# Prevent duplicate handlers
if not logger.handlers:
    logger.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)