from app.gemini_client import GeminiClient
from app.prompts import PromptTemplates
import re

class BusinessInsightsEngine:
    def __init__(self):
        self.gemini = GeminiClient()
    
    def process_query(self, query: str) -> str:
        """Main method to process user queries"""
        try:
            # Check for comparison pattern
            match = re.search(r"compare (.+?) to (.+)", query, re.IGNORECASE)
            if match:
                company = match.group(1).strip()
                competitors = [c.strip() for c in match.group(2).split(",")]
                prompt = PromptTemplates.competitive_analysis(company, competitors)
                return self.gemini.generate(prompt)
            
            # Add other query types here as needed
            return "Please use format: 'Compare COMPANY to COMPETITOR1,COMPETITOR2'"
            
        except Exception as e:
            return f"Processing error: {str(e)}"