import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT

# -----------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------
load_dotenv()

# Try Streamlit Secrets first, then .env
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Add it to Streamlit Secrets (Cloud) or your .env file (Local)."
    )

# -----------------------------
# GEMINI CLIENT
# -----------------------------
client = genai.Client(api_key=api_key)

# -----------------------------
# MODELS TO TRY
# -----------------------------
MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
]

# -----------------------------
# ANALYZE ARTICLE
# -----------------------------
def analyze_article(article: str) -> str:
    if not article.strip():
        return "⚠️ Please paste a news article."

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

            if hasattr(response, "text") and response.text:
                return response.text

        except Exception as e:
            last_error = e
            continue

    return f"❌ All Gemini models failed.\n\nLast Error:\n{last_error}"