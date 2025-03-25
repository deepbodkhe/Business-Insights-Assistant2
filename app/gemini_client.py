import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

class GeminiClient:
    def __init__(self):
        # Use the model name from your available models list
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Update this based on your check
        
    def generate(self, prompt):
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.3,
                    "top_p": 0.95,
                    "max_output_tokens": 2000
                }
            )
            return response.text
        except Exception as e:
            return f"API Error: {str(e)}"