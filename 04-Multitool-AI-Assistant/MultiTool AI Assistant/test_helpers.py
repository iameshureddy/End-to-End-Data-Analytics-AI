from pathlib import Path

from utils.helpers import (
    current_timestamp,
    save_text_report,
    save_json,
)

print(current_timestamp())

save_text_report(
    "This is a sample report.",
    Path("outputs/reports/sample_report.txt")
)

save_json(
    {"status": "success", "project": "MultiTool AI Assistant"},
    Path("outputs/reports/sample.json")
)

print("Helpers working successfully!")