
from tools.report_tool import save_report

result = save_report.invoke(
    {
        "title": "AI Summary",
        "content": """
Artificial Intelligence is transforming industries.

• Automates repetitive tasks
• Supports predictive analytics
• Improves customer experience
• Enhances decision making
"""
    }
)

print(result)