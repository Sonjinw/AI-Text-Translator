import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language="French"):
    """Translates the given text into the target language using OpenAI GPT-4."""
    openai.api_key = API_KEY
    prompt = f"Translate the following text to {target_language}: {text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a translation assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    text_input = input("Enter text to translate: ")
    lang = input("Enter target language (e.g., French, Spanish): ")
    translation = translate_text(text_input, lang)
    print("\nTranslation:\n", translation)
