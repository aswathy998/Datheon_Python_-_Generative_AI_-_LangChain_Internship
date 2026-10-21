
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

project_folder = Path(__file__).resolve().parent
load_dotenv(project_folder / ".env")

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

if not api_key:
    raise SystemExit("ERROR: GEMINI_API_KEY is missing from .env")

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents="Reply with exactly: Gemini connection successful"
    )

    if not response.text:
        raise RuntimeError("The model returned no text.")

    print("SUCCESS: Connected to Gemini!")
    print("Model:", model)
    print("Response:", response.text)

except Exception as error:
    print("Gemini API test failed.")
    print("Error type:", type(error).__name__)
    print("Details:", str(error))
