import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

try:
    # Initialize the model
    model = genai.GenerativeModel("gemini-3.5-flash")

    # Test prompt
    response = model.generate_content(
        "Hello! If you can read this, reply with 'Gemini API is working successfully.'"
    )

    print("\n✅ Gemini Connection Successful!\n")
    print("Response:")
    print("-" * 50)
    print(response.text)
    print("-" * 50)

except Exception as e:
    print("\n❌ Gemini Connection Failed!\n")
    print(f"Error: {e}")