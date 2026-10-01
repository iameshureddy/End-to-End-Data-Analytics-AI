# Customer Review Analytics using Google Gemini

> **Part 3 — GenAI / LLM Customer Review Analytics**

A complete GenAI customer-review analytics workflow built with Python and Google Gemini.  
The project demonstrates prompt engineering, reusable LLM API integration, retry/error handling, structured JSON outputs, prompt comparison, aspect-based sentiment analysis, prompt chaining, multi-turn conversation, and API-key security.

---

# 1. Project Overview

**Customer Review Analytics using Google Gemini** applies a Large Language Model to customer reviews from the **Women's Clothing E-Commerce Reviews Dataset**.

The project is organized as a progression from basic prompt design to a complete GenAI workflow:

```text
Customer Reviews
       |
       v
Data Loading & Cleaning
       |
       v
Task 1 — Prompt Engineering
       |
       +--> Zero-shot
       +--> Few-shot
       +--> Role-based
       |
       v
Task 2 — Reusable Gemini LLM Wrapper
       |
       v
Task 3 — Retry / Error Handling
       |
       v
Task 4 — Prompt Comparison
       |
       v
Task 5 — Aspect-Based Sentiment Analysis
       |
       v
Task 6 — Prompt Chaining
       |
       v
Personalized Customer Response
       |
       v
Task 7 — Multi-turn Conversation
       |
       v
Task 8 — API Key Security
```

The implementation separates prompt construction, API communication, parsing, retry handling, analysis, response generation, and conversation management.



# 3. Dataset

## Dataset Used

**Women's Clothing E-Commerce Reviews Dataset**

The dataset contains customer reviews collected from an online women's clothing store.

Important fields include:

- `Review Text`
- `Rating`
- `Recommended IND`
- `Clothing ID`
- `Age`
- `Positive Feedback Count`
- `Division Name`
- `Department Name`
- `Class Name`

## Dataset Files

```text
data/
├── womens_clothing_reviews.csv
└── cleaned_reviews.csv
```

## Dataset Size

The actual execution logs show:

```text
Original Dataset Shape : (23486, 11)
Cleaned Dataset Shape  : (22634, 11)
```

The main text field used for GenAI analysis is:

```text
Review Text
```

The project therefore uses thousands of customer reviews, while Tasks 4, 5, and 6 intentionally use smaller samples to satisfy their task-specific processing requirements and control API usage.

---

# 4. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM | Google Gemini |
| Data Processing | pandas |
| Environment Variables | python-dotenv |
| API Integration | Google Gemini Python SDK |
| Structured Output | JSON |
| Stored Results | CSV |
| Prompting | Zero-shot, Few-shot, Role-based |
| Analysis | Sentiment Analysis, Aspect-Based Sentiment Analysis |
| Version Control | Git / GitHub |

---

# 5. Project Structure

```text
Part3_GenAI_Customer_Review_Analytics/
│
├── data/
│   ├── womens_clothing_reviews.csv
│   └── cleaned_reviews.csv
│
├── output/
│   ├── csv/
│   │   ├── prompt_comparison.csv
│   │   └── aspect_sentiment_results.csv
│   │
│   └── customer_responses.csv
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── json_parser.py
│   ├── llm_wrapper.py
│   ├── prompt_templates.py
│   ├── prompt_runner.py
│   ├── retry_handler.py
│   ├── aspect_prompt.py
│   ├── aspect_extension_prompt.py
│   ├── aspect_sentiment.py
│   ├── response_generator.py
│   └── conversation_demo.py
│
├── notebooks/
│
├── .env                 # Local only — never commit
├── .gitignore
├── requirements.txt
└── README.md
```

### Separation of Responsibilities

| File | Responsibility |
|---|---|
| `data_loader.py` | Loads and cleans review data |
| `config.py` | Stores project configuration/path settings |
| `prompt_templates.py` | Creates Task 1 prompt templates |
| `llm_wrapper.py` | Provides reusable Gemini API access |
| `retry_handler.py` | Handles retry-enabled LLM calls |
| `json_parser.py` | Parses/validates JSON responses |
| `prompt_runner.py` | Executes Task 4 comparison |
| `aspect_prompt.py` | Builds ABSA prompts |
| `aspect_sentiment.py` | Executes Task 5 |
| `aspect_extension_prompt.py` | Provides prompt logic used for Task 6 analysis/response generation |
| `response_generator.py` | Executes Task 6 prompt chaining |
| `conversation_demo.py` | Executes Task 7 multi-turn conversation |

---

# 6. Environment Setup

## 6.1 Create a Virtual Environment

```bash
python -m venv .venv
```

## 6.2 Activate the Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

## 6.3 Install Dependencies

```bash
pip install -r requirements.txt
```

## 6.4 Configure the Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The real API key must never be placed in:

- Python source files
- README.md
- CSV outputs
- GitHub commits

The application loads the key using an environment variable.

---


# 7. How to Run the Entire Project

Follow these steps in order from the project root directory.

## Step 1 — Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

If the environment has not been created yet:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Step 2 — Install Dependencies

```powershell
pip install -r requirements.txt
```

## Step 3 — Configure the Gemini API Key

Create `.env` in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Do not put the real API key in Python files, README.md, CSV files, screenshots, or Git commits.

## Step 4 — Verify the Dataset

Make sure these files are available:

```text
data/
├── womens_clothing_reviews.csv
└── cleaned_reviews.csv
```

The scripts can create/update the cleaned dataset during execution.

## Step 5 — Run Task 1 and Task 4: Prompt Comparison

Task 1 prompt templates are used by the Task 4 runner.

```powershell
python src/prompt_runner.py
```

This executes:

```text
Zero-shot
Few-shot
Role-based
```

on five reviews and saves:

```text
output/csv/prompt_comparison.csv
```

## Step 6 — Run Task 5: Aspect-Based Sentiment Analysis

```powershell
python src/aspect_sentiment.py
```

This processes 10 reviews and saves:

```text
output/csv/aspect_sentiment_results.csv
```

The terminal should report the number of processed reviews, successful reviews, failed reviews, and aspect records.

## Step 7 — Run Task 6: Prompt Chaining

```powershell
python src/response_generator.py
```

This uses structured Task 5 analysis as input to a second LLM prompt and generates personalized customer responses.

Output:

```text
output/customer_responses.csv
```

## Step 8 — Run Task 7: Multi-turn Conversation

```powershell
python src/conversation_demo.py
```

This demonstrates two complete conversation turns and prints the complete conversation history.

Expected structure:

```text
User
  ↓
Assistant
  ↓
User
  ↓
Assistant
```

## Step 9 — Verify API-Key Security Before Submission

Run:

```powershell
git ls-files .env
```

There should be no output.

Then run:

```powershell
git grep -n "AIza" -- ':!README.md' 
```

There should be no output.

Also check:

```powershell
git status
```

Confirm that `.env` is not listed as a tracked file.

## Complete Execution Order

For a complete demonstration, run the commands in this order:

```powershell
python src/prompt_runner.py
python src/aspect_sentiment.py
python src/response_generator.py
python src/conversation_demo.py
```

Then verify security:

```powershell
git ls-files .env
git grep -n "AIza" -- ':!README.md'
git status
```

## Main Generated Outputs

After successful execution, verify:

```text
output/
├── csv/
│   ├── prompt_comparison.csv
│   └── aspect_sentiment_results.csv
│
└── customer_responses.csv
```

These files contain the generated results required for Tasks 4, 5, and 6.

# 8. Task 1 — Prompt Engineering

## Objective

Task 1 implements three required prompting strategies for customer-review sentiment classification:

1. Zero-shot prompting
2. Few-shot prompting
3. Role-based prompting

## Implementation File

```text
src/prompt_templates.py
```

Functions:

```python
build_zero_shot_prompt(review_text)
build_few_shot_prompt(review_text)
build_role_prompt(review_text)
```

The module creates prompt strings only. Gemini API communication is handled separately by the reusable LLM layer.

---

## 7.1 Zero-shot Prompt

The model receives instructions without classification examples.

The prompt instructs Gemini to:

- Read the review.
- Select exactly one sentiment.
- Use `positive`, `neutral`, or `negative`.
- Return only valid JSON.
- Follow the required schema.

### Purpose

- Establish a baseline.
- Test direct instruction following.
- Avoid demonstration examples.

---

## 7.2 Few-shot Prompt

The model receives multiple labeled examples before the target review.

The examples demonstrate:

- Positive sentiment
- Negative sentiment
- Neutral sentiment

The target review is then classified using the same output structure.

### Purpose

- Demonstrate expected classification behavior.
- Improve consistency.
- Demonstrate the desired output format.

---

## 7.3 Role-based Prompt

The model is assigned the role:

```text
Senior Customer Insights Analyst
```

The prompt also provides customer-feedback context and asks the model to classify the review.

### Purpose

- Provide domain context.
- Encourage professional analysis.
- Produce business-oriented explanations.

---

## 7.4 Common JSON Schema

All three prompt strategies use the same schema:

```json
{
  "label": "positive|neutral|negative",
  "confidence": "low|medium|high",
  "reason": "short explanation"
}
```

Using the same schema makes the three strategies directly comparable and allows responses to be parsed programmatically.

### Task 1 Evidence

| Requirement | Evidence |
|---|---|
| Zero-shot | `build_zero_shot_prompt()` |
| Few-shot | `build_few_shot_prompt()` |
| Role-based | `build_role_prompt()` |
| Common structured output | Shared JSON schema |
| Reusable prompt functions | `src/prompt_templates.py` |
| Separation from API calls | Prompt creation is separate from API wrapper |

---

# 9. Task 2 — Reusable LLM API Wrapper

## Objective

Task 2 creates a reusable Python function for communicating with Google Gemini.

## Implementation File

```text
src/llm_wrapper.py
```

Main function:

```python
call_llm(prompt, temperature=0.3, max_tokens=512)
```

## Required Parameters

### `prompt`

The instruction sent to Gemini.

### `temperature`

Controls the randomness of generated responses.

```text
Lower value  → more deterministic
Higher value → more varied/creative
```

Default:

```text
0.3
```

### `max_tokens`

Controls the maximum output length.

Default:

```text
512
```

## API-Key Handling

The wrapper loads:

```python
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
```

The API key is therefore supplied through the environment instead of being hardcoded.

## Error Handling

The API call is protected with exception handling. If the API request fails, the wrapper reports the error and returns `None`.

## Reusability

Other project tasks call the shared LLM/retry layer rather than duplicating API configuration throughout the project.

### Task 2 Evidence

| Requirement | Evidence |
|---|---|
| Reusable function | `call_llm()` |
| Gemini API communication | Implemented |
| Prompt parameter | Implemented |
| Temperature parameter | Implemented |
| Max-token parameter | Implemented |
| Environment-based key | `GEMINI_API_KEY` |
| API error handling | `try/except` |
| Reuse | Used by downstream tasks |

---

# 10. Task 3 — Retry-on-Failure Handling

## Objective

Task 3 adds a retry layer so temporary failures or invalid outputs can be retried without immediately terminating the workflow.

## Implementation File

```text
src/retry_handler.py
```

Main retry-enabled function:

```python
safe_call_llm(...)
```

## Retry Concept

```text
LLM Request
     |
     v
Response received?
     |
    No
     |
     v
Retry
     |
     v
Validate response
     |
     v
Valid?
 /   \
Yes   No
 |     |
 v     v
Use   Retry / fail safely
```

## Actual Execution Evidence

During Task 5, the system detected an invalid response:

```text
Processing Review 4/10
Invalid output. Retrying Review 4
```

The final execution then completed:

```text
Reviews processed  : 10
Successful reviews : 10
Failed reviews     : 0
Aspect records     : 26
```

This demonstrates that the retry path was actually exercised during execution.

### Task 3 Evidence

| Requirement | Evidence |
|---|---|
| Retry handler | `retry_handler.py` |
| Retry-enabled calls | `safe_call_llm()` |
| Invalid response detection | Review 4 |
| Retry execution | `Invalid output. Retrying Review 4` |
| Workflow continuation | Final run completed successfully |

---

# 11. Task 4 — Prompt Comparison

## Objective

Task 4 compares the three Task 1 prompting strategies using the same five customer reviews.

```text
3 strategies × 5 reviews = 15 responses
```

## Implementation File

```text
src/prompt_runner.py
```

## Execution

```bash
python src/prompt_runner.py
```

For each selected review:

```text
Zero-shot
Few-shot
Role-based
```

are executed.

## Dataset Execution

```text
Original Dataset Shape : (23486, 11)
Cleaned Dataset Shape  : (22634, 11)
```

## JSON Validation

The execution produced:

```text
JSON Validity Summary

Few-shot      5
Role-based    5
Zero-shot     5
```

Therefore:

```text
Total responses : 15
Valid JSON      : 15
Invalid JSON    : 0
Validity rate   : 100%
```

## Output File

```text
output/csv/prompt_comparison.csv
```

The output contains:

```text
Prompt
Valid JSON
Label
Confidence
Reason
Raw Response
Review No
Review
```

## Interpretation

All three strategies achieved 100% JSON validity on the five-review execution sample.

Therefore, **JSON validity alone does not identify one strategy as the overall winner**. The CSV also preserves labels, confidence values, reasons, and raw responses so the generated outputs can be inspected qualitatively.

### Task 4 Evidence

| Requirement | Evidence |
|---|---|
| Zero-shot | Compared |
| Few-shot | Compared |
| Role-based | Compared |
| Five reviews | 5 |
| Total outputs | 15 |
| Structured JSON | Yes |
| JSON validation | Yes |
| Validity | 15/15 |
| Output | `prompt_comparison.csv` |
| Interpretation | Included |

---

# 12. Task 5 — Aspect-Based Sentiment Analysis

## Objective

Task 5 performs **Aspect-Based Sentiment Analysis (ABSA)** on **10 customer reviews** using Google Gemini.

Instead of assigning only one overall sentiment, the system identifies relevant aspects mentioned in each review, determines the sentiment for those aspects, and generates an actionable recommendation.

## Implementation Files

```text
src/aspect_prompt.py
src/aspect_sentiment.py
```

## Execution

```bash
python src/aspect_sentiment.py
```

## Target Aspects

The prompt considers:

- Quality
- Size/Fit
- Comfort
- Design/Style
- Delivery, when mentioned
- Overall sentiment

The model can produce only the aspects that are relevant to the individual review.

## Structured Output

The analysis is represented using an aspect/action structure such as:

```json
{
  "aspects": [
    {
      "aspect": "quality",
      "sentiment": "positive",
      "action": "maintain silky fabric quality"
    },
    {
      "aspect": "size/fit",
      "sentiment": "negative",
      "action": "revise sizing measurements for petites"
    }
  ],
  "overall_sentiment": "negative"
}
```

## Actionable Recommendations

The analysis goes beyond sentiment and produces short actions such as:

```text
Maintain silky fabric quality
Keep sexy design details
Preserve comfortable wear experience
Revise sizing measurements for petites
Upgrade quality of net layers
Fix net layer zipper placement
```

These recommendations translate detected customer feedback into potential product or business actions.

## Actual Final Execution

```text
Reviews processed  : 10
Successful reviews : 10
Failed reviews     : 0
Aspect records     : 26
```

## Output

```text
Review No   Aspect          Sentiment   Action
1           quality        positive    Maintain silky fabric standard
1           design/style   positive    Keep sexy design details
1           comfort        positive    Preserve high comfort level
2           design/style   positive    Maintain pretty design details
2           size/fit       positive    Clarify petite length specifications
3           size/fit       negative    Revise sizing measurements for petites
3           comfort        positive    Maintain comfort in top half
3           quality        negative    Upgrade quality of net layers
3           design/style   negative    Fix net layer zipper placement
```

The number of aspect records varies by review because only relevant aspects are included for each customer review.

## Output File

```text
output/csv/aspect_sentiment_results.csv
```

### Task 5 Evidence

### 10-Record Aspect-Based Sentiment Results

The model was run on 10 real customer reviews. Each review contains at least two
relevant aspects. The model generated 26 aspect-level records in total.

| Review | Aspects & Sentiments | Actionable Phrases | Overall Sentiment |
|---|---|---|---|
| 1 | quality — Positive; design/style — Positive; comfort — Positive | Maintain silky fabric quality; keep sexy design details; preserve comfortable wear experience | Positive |
| 2 | design/style — Positive; size/fit — Positive | Maintain pretty aesthetic design details; clarify petite length specifications online | Positive |
| 3 | size/fit — Negative; comfort — Positive; quality — Negative; design/style — Negative | Revise sizing measurements for petites; Maintain comfort in top half; Upgrade quality of net layers; Fix net layer zipper placement | Negative |
| 4 | style/design — Positive; compliments/appeal — Positive | Maintain current design; Highlight style in marketing | Positive |
| 5 | design/style — Positive; size/fit — Positive | Maintain flattering adjustable front tie; Keep perfect length for leggings | Positive |
| 6 | size/fit — Negative; design/style — Neutral; quality — Positive; delivery — Positive | offer petite specific sizing options; proportion skirt for smaller frames; maintain beautiful fabric and embellishments; preserve garment condition during transit | Negative |
| 7 | design/style — Positive; size/fit — Negative | Maintain versatile matching color options; Offer smaller or petite sizing | Positive |
| 8 | design/style — Positive; size/fit — Negative; size/fit — Negative | maintain versatile charcoal shimmer design; offer extra extra small sizes; introduce petite sizing options | Neutral |
| 9 | size/fit — Negative; design/style — Positive | reconsider bust sizing running snug; maintain flattering feminine style details | Positive |
| 10 | size/fit — Positive; design/style — Positive | Maintain accurate petite sizing guidance; Highlight versatile styling for occasions | Positive |

### Task 5 Result

Task 5 successfully processed all 10 customer reviews with 0 failures.
A total of 26 aspect-level records were generated. Each successful review
contains at least two relevant aspects, with sentiment and a specific
actionable phrase provided for every aspect.

The actionable phrases are generated from the review content and are intended
to provide practical product, sizing, quality, design, delivery, or
customer-experience improvement suggestions.

---

# 13. Task 6 — Prompt Chaining

## Objective

Task 6 demonstrates a genuine two-stage LLM workflow.

The structured analysis produced in Task 5 is used as input/context for a second LLM prompt that generates a customer-support response.

## Implementation File

```text
src/response_generator.py
```

## Workflow

```text
Original Customer Review
          |
          v
Task 5 — Aspect Analysis
          |
          v
Structured Analysis
          |
          v
Task 6 Response Prompt
          |
          v
Gemini
          |
          v
Personalized Customer Reply
```

## First LLM Step

The review is analyzed into structured aspects, sentiment, and actions.

The output:

```json
{
  "aspects": [
    {
      "aspect": "size/fit",
      "sentiment": "negative",
      "action": "Revise sizing measurements for petites"
    },
    {
      "aspect": "comfort",
      "sentiment": "positive",
      "action": "Maintain comfort in top half"
    },
    {
      "aspect": "quality",
      "sentiment": "negative",
      "action": "Upgrade quality of net layers"
    },
    {
      "aspect": "design/style",
      "sentiment": "negative",
      "action": "Fix net layer zipper placement"
    }
  ],
  "overall_sentiment": "negative"
}
```

## Second LLM Step

The original review and structured analysis are supplied to the second prompt.

The response prompt requires Gemini to:

- Thank the customer.
- Address specific issues.
- Appreciate positive feedback.
- Apologize for negative experiences where appropriate.
- Mention improvements when appropriate.
- Sound professional and empathetic.
- Avoid generic responses.
- Personalize the reply using the structured analysis.
- Keep the response concise.

## Execution

```bash
python src/response_generator.py
```

Final execution:

```text
Reviews selected      : 3
Responses generated   : 3
Successful responses  : 3
Failed responses      : 0
```

### Three Original Generated Customer Responses

The following are the original model-generated responses from the Task 6 execution. Each response is tied to its specific customer review and uses the structured Task 5 analysis.

### Response 1

**Customer Review:**

> Absolutely wonderful - silky and sexy and comfortable

**Structured Task 5 Analysis:**

```json
{
  "aspects": [
    {
      "aspect": "quality",
      "sentiment": "positive",
      "action": "maintain silky fabric quality"
    },
    {
      "aspect": "design/style",
      "sentiment": "positive",
      "action": "keep sexy design details"
    },
    {
      "aspect": "comfort",
      "sentiment": "positive",
      "action": "preserve comfortable wear experience"
    }
  ],
  "overall_sentiment": "positive"
}
```

**Original AI Customer Reply:**

> Thank you so much for sharing your wonderful feedback with us! We are thrilled to hear that you love the silky fabric quality and the sexy design details of your new piece. We will certainly maintain these standards to ensure your wear experience remains wonderfully comfortable.

---

### Response 2

**Customer Review:**

> Love this dress! it's sooo pretty. i happened to find it in a store, and i'm glad i did bc i never would have ordered it online bc it's petite. i bought a petite and am 5'8". i love the length on me- hits just a little below the knee. would definitely be a true midi on someone who is truly petite.

**Structured Task 5 Analysis:**

```json
{
  "aspects": [
    {
      "aspect": "design/style",
      "sentiment": "positive",
      "action": "maintain pretty aesthetic design details"
    },
    {
      "aspect": "size/fit",
      "sentiment": "positive",
      "action": "clarify petite length specifications online"
    }
  ],
  "overall_sentiment": "positive"
}
```

**Original AI Customer Reply:**

> Thank you so much for sharing your feedback and for your love of the dress's pretty design! We are thrilled to hear that the petite length worked so well for your 5'8" height, hitting just below the knee as a lovely midi. We appreciate your helpful insight and will work on clarifying our petite length specifications online so other tall shoppers can easily find their perfect fit too.

---

### Response 3

**Customer Review:**

> I had such high hopes for this dress and really wanted it to work for me. i initially ordered the petite small (my usual size) but i found this to be outrageously small. so small in fact that i could not zip it up! i reordered it in petite medium, which was just ok. overall, the top half was comfortable and fit nicely, but the bottom half had a very tight under layer and several somewhat cheap (net) over layers. imo, a major design flaw was the net over layer sewn directly into the zipper - it c

**Structured Task 5 Analysis:**

```json
{
  "aspects": [
    {
      "aspect": "size/fit",
      "sentiment": "negative",
      "action": "Revise sizing measurements for petites"
    },
    {
      "aspect": "comfort",
      "sentiment": "positive",
      "action": "Maintain comfort in top half"
    },
    {
      "aspect": "quality",
      "sentiment": "negative",
      "action": "Upgrade quality of net layers"
    },
    {
      "aspect": "design/style",
      "sentiment": "negative",
      "action": "Fix net layer zipper placement"
    }
  ],
  "overall_sentiment": "negative"
}
```

**Original AI Customer Reply:**

> Thank you for sharing such detailed feedback about your experience with our petite dress. We sincerely apologize for the sizing inconsistencies that required you to exchange the petite small, as well as the frustrating design flaw with the net overlayer getting caught in the zipper and the cheap feel of those layers. On the positive note, we are glad to hear that you found the top half to be comfortable and nicely fitted. Please rest assured that we are taking your input seriously to revise our petite sizing measurements, upgrade the quality of the net material, and fix the zipper placement in future designs.

This response is personalized from the structured analysis by addressing the specific sizing, comfort, quality, and zipper issues identified in the review.

## Output

```text
output/customer_responses.csv
```

The CSV contains:

- Review number
- Customer review
- Structured Task 5 analysis
- AI-generated customer reply
- Status


# 14. Task 7 — Multi-turn Conversation

## Objective

Task 7 demonstrates a two-turn conversation where the second Gemini API call uses the conversation history from the first turn.

## Implementation File

```text
src/conversation_demo.py
```

## Conversation History Design

Messages are stored as dictionaries:

```python
{
    "role": "user",
    "content": "..."
}
```

and:

```python
{
    "role": "assistant",
    "content": "..."
}
```

The history is maintained as a list.

## Turn 1

Customer:

```text
The dress quality is excellent, but the size was too small.
```

The assistant responds to the positive quality feedback and the sizing problem.

## Turn 2

Customer:

```text
Can I exchange it for a larger size?
```

The second Gemini prompt is built from the existing conversation history, so the assistant understands that "it" refers to the previously discussed dress.

## Actual Execution

```text
TURN 1

Customer:
The dress quality is excellent, but the size was too small.

Assistant:
I'm so glad to hear you love the quality, but I'm sorry the sizing
didn't work out for you. I would be happy to help you with an exchange
or return today. Could you please provide your order number so I can
look up your purchase?
```

```text
TURN 2

Customer:
Can I exchange it for a larger size?

Assistant:
Yes, absolutely! I can certainly help you exchange it for a larger
size. Could you please provide your order number so I can look up
your purchase?
```

## Verification

The program verifies:

```text
Total messages in history : 4
Turn 1 assistant response stored : YES
Turn 2 prompt includes Turn 1 history : YES
Follow-up question uses previous context : YES
Conversation contains 2 complete turns : YES
```

Final history:

```text
Message 1 → User
Message 2 → Assistant
Message 3 → User
Message 4 → Assistant
```

### Task 7 Evidence

| Requirement | Evidence |
|---|---|
| Two turns | Turn 1 + Turn 2 |
| User messages | Yes |
| Assistant messages | Yes |
| Conversation history | Maintained |
| History stored structurally | List of role/content messages |
| Turn 2 receives earlier context | Verified |
| Contextual follow-up | Exchange question |
| Complete history displayed | Yes |
| Four final messages | Yes |

---

# 15. Task 8 — API Key Security

## Objective

Protect the Gemini API key and ensure that it is not committed to the repository.

## Local Storage

The real API key is stored only in:

```text
.env
```

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The actual secret is intentionally never included in this README.

## Environment Variable Loading

The application uses:

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
```

The source code therefore accesses the variable rather than storing the secret itself.

## `.gitignore`

The repository includes:

```gitignore
.env
```

It also ignores common local/generated files:

```gitignore
.venv/
.env
__pycache__/
*.pyc
.ipynb_checkpoints/
.vscode/
.DS_Store
*.log
```

## Git Verification

The following checks were executed:

```powershell
git ls-files .env
```

Result:

```text
No output
```

Therefore `.env` is not tracked by Git.

A second check was performed:

```powershell
git grep -n "AIza" -- ':!README.md'
```

Result:

```text
No output
```

This check found no `AIza` API-key pattern in the tracked repository.

### Security Verification

```text
.env stored locally          : PASS
.env ignored by Git          : PASS
.env tracked by Git          : NO
API key hardcoded            : NO
AIza pattern in tracked repo: NO
```

**Important:** never commit the `.env` file or expose the real API key in documentation, screenshots, source code, or output files.

---



# 17. Generated Outputs

## Task 4 Output

```text
output/csv/prompt_comparison.csv
```

Contains:

- Prompt strategy
- JSON validity
- Sentiment label
- Confidence
- Reason
- Raw response
- Review number
- Review text

## Task 5 Output

```text
output/csv/aspect_sentiment_results.csv
```

Contains:

- Review number
- Aspect
- Sentiment
- Action
- Overall sentiment
- Status

Final run:

```text
10 reviews
26 aspect records
10 successful
0 failed
```

## Task 6 Output

```text
output/customer_responses.csv
```

Contains:

- Review number
- Customer review
- Structured Task 5 analysis
- AI-generated customer response
- Status

Final run:

```text
3 selected
3 generated
3 successful
0 failed
```

## Task 7 Output

Task 7 demonstrates the conversation through terminal output and the in-memory conversation history.

Final history:

```text
User
  ↓
Assistant
  ↓
User
  ↓
Assistant
```

---

# 18. Execution Results

## Task 4

```text
Original Dataset Shape : (23486, 11)
Cleaned Dataset Shape  : (22634, 11)

Few-shot      5
Role-based    5
Zero-shot     5

Total responses : 15
Valid JSON      : 15
Invalid JSON    : 0
```

**Result: 15/15 valid JSON responses (100% validity).**

## Task 5

```text
Reviews processed  : 10
Successful reviews : 10
Failed reviews     : 0
Aspect records     : 26
```

**Result: 10/10 reviews completed successfully.**

## Task 6

```text
Reviews selected      : 3
Responses generated   : 3
Successful responses  : 3
Failed responses      : 0
```

**Result: 3/3 customer responses generated successfully.**

## Task 7

```text
Total messages in history : 4
Turn 1 assistant response stored : YES
Turn 2 prompt includes Turn 1 history : YES
Follow-up question uses previous context : YES
Conversation contains 2 complete turns : YES
```

**Result: 2-turn contextual conversation demonstrated successfully.**

## Task 8

```text
git ls-files .env
→ no output

git grep -n "AIza" -- ':!README.md'
→ no output
```

**Result: API-key security checks passed.**

---

# 19. Rubric Coverage Matrix

## Project Task Summary

| Task | What was implemented | Evidence / Output |
|---|---|---|
| **Task 1 – Prompt Engineering** | Zero-shot, few-shot, and role-based prompts with a common JSON response format | `src/prompt_templates.py` |
| **Task 2 – LLM API Wrapper** | Reusable Gemini API function with prompt, temperature, max-token settings, environment-based API key, and error handling | `src/llm_wrapper.py` |
| **Task 3 – Retry Handling** | Retry mechanism for failed or invalid LLM responses | `src/retry_handler.py` — retry observed during Task 5 |
| **Task 4 – Prompt Comparison** | Compared zero-shot, few-shot, and role-based prompting on 5 reviews | `output/csv/prompt_comparison.csv` — 15/15 valid JSON responses |
| **Task 5 – Aspect-Based Sentiment Analysis** | Analyzed 10 reviews for relevant aspects, sentiment, overall sentiment, and actionable recommendations | `output/csv/aspect_sentiment_results.csv` — 10/10 successful reviews |
| **Task 6 – Prompt Chaining** | Used Task 5 structured analysis as input to a second LLM prompt for personalized customer replies | `output/customer_responses.csv` — 3/3 responses generated |
| **Task 7 – Multi-turn Conversation** | Demonstrated a two-turn customer-support conversation using conversation history | `src/conversation_demo.py` — 2 turns / 4 messages |
| **Task 8 – API Key Security** | Stored the API key in `.env`, excluded it with `.gitignore`, and checked that it was not tracked or exposed | `git ls-files .env` and `git grep -n "AIza" -- ':!README.md'` returned no output |

---

# 20. Conclusion

This project demonstrates a complete GenAI customer-review analytics pipeline using Google Gemini.

The implementation progresses from:

```text
Prompt Design
      ↓
Reusable LLM Integration
      ↓
Retry/Error Handling
      ↓
Prompt Comparison
      ↓
Aspect-Based Sentiment Analysis
      ↓
Prompt Chaining
      ↓
Multi-turn Conversation
      ↓
API-Key Security
```

The final demonstrated results are:

```text
Task 4 → 15/15 valid JSON responses
Task 5 → 10/10 successful reviews, 26 aspect records
Task 6 → 3/3 successful customer responses
Task 7 → 2 turns, 4-message conversation history
Task 8 → .env untracked + no "AIza" pattern detected
```

The project combines prompt engineering, structured LLM outputs, reusable API integration, robustness, contextual reasoning, customer-response generation, conversational memory, and secure credential management into one end-to-end GenAI workflow.

---

## Author

**Bhuvaneswari Yennapusala**

**Project:** Customer Review Analytics using Google Gemini
