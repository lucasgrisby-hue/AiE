# -*- coding: utf-8 -*-

from dotenv import load_dotenv

from model import generate_gemini_response, generate_ollama_response
from utils import process_response

from warnings import filterwarnings

filterwarnings("ignore")

load_dotenv()

stream=False

user_input = "Who is Ozymandias?"
# user_input = "What is the last question I asked?"
ai_response, stream = generate_ollama_response(user_input=user_input, stream=stream)

process_response(response=ai_response, stream=stream)
