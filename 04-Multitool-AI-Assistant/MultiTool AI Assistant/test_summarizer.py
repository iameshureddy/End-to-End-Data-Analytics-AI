from tools.text_summarizer_tool import summarize_text

text = """
Artificial Intelligence is transforming industries by automating repetitive
tasks, assisting decision-making, improving customer service,
and enabling predictive analytics.
Machine learning is one of the major branches of AI that learns patterns
from data without explicit programming.
"""

result = summarize_text.invoke(
    {
        "text": text
    }
)

print(result)