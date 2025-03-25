from app.gemini_client import GeminiClient

def test_gemini():
    print("\nTesting Gemini API connection...")
    client = GeminiClient()
    
    # Simple test prompt
    test_prompt = "Generate a 1-sentence confirmation that the API is working"
    response = client.generate(test_prompt)
    
    print("\nAPI Response:")
    print(response)
    print("\nTest completed!")

if __name__ == "__main__":
    test_gemini()