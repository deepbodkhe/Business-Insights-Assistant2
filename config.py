import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    BUSINESS_DOMAINS = {
        'finance': "Specializing in financial metrics and ROI analysis",
        'marketing': "Expert in customer segmentation and campaign analytics"
    }