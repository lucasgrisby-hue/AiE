import os

from google import genai
from dotenv import load_dotenv

from warnings import filterwarnings

filterwarnings("ignore")

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

message = input("User: ")

response = client.models.generate_content(
    model=os.environ["GEMINI_MODEL_NAME"],
    contents=message
)

print(f"AI: {response.text}")