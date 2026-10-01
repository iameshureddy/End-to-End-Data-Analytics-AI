"""
config.py
----------
Central configuration for the MultiTool AI Assistant project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ======================================================
# Project Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_DIR = OUTPUT_DIR / "reports"
LOG_DIR = OUTPUT_DIR / "logs"
CHART_DIR = OUTPUT_DIR / "charts"

# Create output folders if they don't exist
REPORT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)

# ======================================================
# Gemini Configuration
# ======================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")

MODEL_NAME = "gemini-3.5-flash"
SUMMARIZER_MODEL = "gemini-3.5-flash"
TEMPERATURE = 0.2

TEMPERATURE = 0.2

MAX_OUTPUT_TOKENS = 1024

# ======================================================
# Agent Configuration
# ======================================================

MAX_ITERATIONS = 5
VERBOSE = True

# ======================================================
# External APIs
# ======================================================

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

CURRENCY_API_URL = "https://api.frankfurter.app/latest"

# ======================================================
# Logging
# ======================================================

LOG_FILE = LOG_DIR / "assistant.log"

# ======================================================
# Project Information
# ======================================================

APP_NAME = "MultiTool AI Assistant"

VERSION = "1.0.0"

AUTHOR = "Bhuvaneswari Yennapusala"