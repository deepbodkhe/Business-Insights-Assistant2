from app.gemini_client import GeminiClient
from app.prompts import PromptTemplates
import re
from typing import List, Dict, Optional

class BusinessInsightsEngine:
    def __init__(self):
        self.gemini = GeminiClient()
        self.query_handlers = {
            'compare': self._handle_comparison,
            'trend': self._handle_trend,
            'finance': self._handle_finance
        }
    
    def process_query(self, query: str) -> str:
        """Process user queries with improved error handling and multiple query types"""
        if not query or len(query.strip()) < 5:
            return "Please provide a more detailed query (minimum 5 characters)."
        
        try:
            # Normalize and classify query
            query = query.lower().strip()
            
            # Route to appropriate handler
            if "compare" in query:
                return self._handle_comparison(query)
            elif "trend" in query or "forecast" in query:
                return self._handle_trend(query)
            elif any(fin_term in query for fin_term in ["finance", "roi", "revenue"]):
                return self._handle_finance(query)
            else:
                return self._handle_general(query)
                
        except Exception as e:
            return f"System error: {str(e)}. Please try again with a different query."

    def _handle_comparison(self, query: str) -> str:
        """Handle competitive analysis queries"""
        match = re.search(r"compare (.+?) to (.+)", query, re.IGNORECASE)
        if not match:
            return "Please use format: 'Compare COMPANY to COMPETITOR1,COMPETITOR2'"
            
        company = match.group(1).strip()
        competitors = [c.strip() for c in match.group(2).split(",")]
        
        if len(competitors) > 5:
            return "Please limit comparisons to 5 competitors for focused analysis."
            
        prompt = PromptTemplates.competitive_analysis(company, competitors)
        return self.gemini.generate(prompt)

    def _handle_trend(self, query: str) -> str:
        """Handle trend forecasting queries"""
        prompt = PromptTemplates.trend_analysis(query)
        return self.gemini.generate(prompt)

    def _handle_finance(self, query: str) -> str:
        """Handle financial analysis queries"""
        prompt = PromptTemplates.financial_analysis(query)
        return self.gemini.generate(prompt)

    def _handle_general(self, query: str) -> str:
        """Handle general business queries"""
        prompt = PromptTemplates.general_business(query)
        return self.gemini.generate(prompt)