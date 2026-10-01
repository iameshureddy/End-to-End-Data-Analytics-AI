from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "output"
IMAGE_DIR = BASE_DIR / "images"

PROCESSED_DATA = OUTPUT_DIR / "processed_dataset.csv"