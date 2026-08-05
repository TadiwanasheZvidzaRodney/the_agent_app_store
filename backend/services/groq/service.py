import os
import logging

logger = logging.getLogger(__name__)

class GroqLLMServiceStub:
    def __init__(self, model_name: str = "llama-3.1-8b-instant"):
        self.model_name = model_name
        self.api_key = os.getenv("GROQ_API_KEY")
        
    def generate_response(self, prompt: str, user_input: str):
        if not self.api_key or self.api_key == "your_groq_api_key_here":
            logger.warning("GROQ_API_KEY not set!")
            return "Please set your Groq API Key."
        return f"Groq Response using {self.model_name}: I hear you saying '{user_input}'"
