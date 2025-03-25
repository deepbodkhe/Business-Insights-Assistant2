import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def list_available_models():
    try:
        models = genai.list_models()
        print("Available Models:")
        for m in models:
            print(f"- {m.name} (Supports: {', '.join(m.supported_generation_methods)})")
        return models
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

if __name__ == "__main__":
    list_available_models()