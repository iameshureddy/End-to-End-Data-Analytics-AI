from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Paths
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

RAW_DATA = DATA_DIR / "womens_clothing_reviews.csv"
CLEAN_DATA = DATA_DIR / "cleaned_reviews.csv"