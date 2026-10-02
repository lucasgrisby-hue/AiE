import os

from ollama import Client
from google import genai

from utils import log

@log
def generate_gemini_response(user_input):

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model=os.environ["GEMINI_MODEL_NAME"],
        contents=user_input
    )

    return response.text


@log
def generate_ollama_response(user_input, system_prompt=None, stream=True):
    if system_prompt is None:
        system_prompt = "You are a general knowledge expert. Please answer questions for me."
    
    ollama_client = Client()
    response = ollama_client.chat(
        model=os.environ["OLLAMA_MODEL"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        stream=stream
    )

    return response.message.content if not stream else response, stream
