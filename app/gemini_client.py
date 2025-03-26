import google.generativeai as genai
from config import Config
from typing import Optional
import time

genai.configure(api_key=Config.GEMINI_API_KEY)

class GeminiClient:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
        self.safety_settings = {
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE'
        }
    
    def generate(self, prompt: str, max_retries: int = 3) -> Optional[str]:
        """Generate content with retry logic and enhanced error handling"""
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.3,
                        "top_p": 0.95,
                        "max_output_tokens": 4000
                    },
                    safety_settings=self.safety_settings
                )
                
                if response.text:
                    return response.text
                else:
                    raise ValueError("Empty response from API")
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    return f"API Error after {max_retries} attempts: {str(e)}"
                time.sleep(1 * (attempt + 1))  # Exponential backoff
        
        return None