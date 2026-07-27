import os
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

# Models to try in order
MODELS = [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest",
    "gemini-2.0-flash",
]


def analyze_article(article: str) -> str:
    if not article.strip():
        return "Please paste a news article."

    prompt = f"""
{SYSTEM_PROMPT}

NEWS ARTICLE:

{article}
"""

    last_error = None

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )

            if response.text:
                return response.text

        except Exception as e:
            last_error = e
            continue

    return f"❌ All models failed.\n\nLast Error:\n{last_error}"