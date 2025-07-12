from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create the model object (make sure the name is valid!)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Send a prompt
response = model.generate_content("What is LangChain?")
print(response.text)
