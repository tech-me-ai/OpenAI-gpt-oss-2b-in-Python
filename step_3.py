# STEP 3: Add Streaming Responses

import requests
import json

MODEL_NAME = "gpt-oss:20b"
OLLAMA_URL = "http://localhost:11434"
SYSTEM_PROMPT = "You are a helpful assistant. Be concise and clear."

def send_message_streaming(conversation):
    """Send message and stream response word-by-word like ChatGPT"""
    payload = {"model": MODEL_NAME, "messages": conversation, "stream": True}
    response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, stream=True)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"
    
    print("AI: ", end="", flush=True)  # Start AI response line
    full_response = ""
    
    # Process each chunk of the streaming response
    for line in response.iter_lines():
        if line:
            try:
                chunk = json.loads(line.decode('utf-8'))
                if 'message' in chunk and 'content' in chunk['message']:
                    content = chunk['message']['content']
                    print(content, end="", flush=True)  # Print immediately without waiting
                    full_response += content
            except:
                continue  # Skip malformed chunks
    
    print()  # New line after streaming is complete
    return full_response

def chat_loop():
    """Interactive chat with streaming responses"""
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit']:
            break
            
        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})
        
        # Get streaming AI response
        ai_response = send_message_streaming(conversation)
        print()  # Extra spacing for readability
        
        # Add AI response to conversation history
        conversation.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    chat_loop()