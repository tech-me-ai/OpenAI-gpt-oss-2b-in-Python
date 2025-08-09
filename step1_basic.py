# STEP 1: Basic Ollama Connection

import requests

# Configuration - Change these if needed
MODEL_NAME = "gpt-oss:20b"
OLLAMA_URL = "http://localhost:11434"

# Define the AI's role and user's question
system_prompt = "You are a knowledgeable expert in data science and a helpful assistant."
user_message = "What is CoT in LLMs in one sentence?"

# Build the conversation structure with proper roles
messages = [
    {"role": "system", "content": system_prompt},  # Sets AI behavior
    {"role": "user", "content": user_message}      # User's question
]

# Prepare the request payload
payload = {
    "model": MODEL_NAME,
    "messages": messages,
    "stream": False  # Get complete response at once
}

# Send request to Ollama API
response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload)

'''
response.status_code:
200: Success - everything worked
404: Model not found
500: Server error
Connection refused: Ollama not running
'''

# Handle the response
if response.status_code != 200:
    print(response.status_code)
else:
    result = response.json()
    answer = result['message']['content']  # Extract AI's response
    print(f"User: {user_message}")
    print(f"AI: {answer}")
