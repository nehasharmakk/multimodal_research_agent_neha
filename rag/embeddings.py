import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def create_embedding(text):

    response = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text
    )

    return response["embedding"]
