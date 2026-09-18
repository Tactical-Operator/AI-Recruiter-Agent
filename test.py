import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key NOT found")
    exit()

print("API key loaded successfully")

client = genai.Client(api_key=api_key)

print("Sending request to Gemini...")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say exactly: Gemini API is working!"
)

print("Gemini responded:")
print(response.text)