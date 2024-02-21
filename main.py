import os
import google.generativeai as genai

# Fetch the API key from the environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key is available
if GOOGLE_API_KEY is None:
    print("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

# Configure the API key for Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)


generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = {
    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
}
model = genai.GenerativeModel(
    "gemini-pro", generation_config=generation_config, safety_settings=safety_settings
)

chat = model.start_chat(
    history=[]
)

response = chat.send_message("System prompt: You are an amazing content creator")
print(response.text)
response = chat.send_message("who are you? describe yourself")
print(response.text)
print(chat.history)
