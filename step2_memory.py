# STEP 2: Add Conversation Loop with Memory 

import requests

MODEL_NAME = "gpt-oss:20b"
OLLAMA_URL = "http://localhost:11434"
SYSTEM_PROMPT = "You are a helpful assistant. Be concise and clear."

def send_message(conversation):
    """Send conversation history to Ollama and get response"""
    payload = {"model": MODEL_NAME, "messages": conversation, "stream": False}
    response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload)
    return response.json()['message']['content'] if response.status_code == 200 else f"Error: {response.status_code}"

def chat_loop():
    """Main interactive chat loop with memory"""
    # Initialize conversation with system prompt
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit']:
            break
            
        # Add user message to conversation history
        conversation.append({"role": "user", "content": user_input})
        
        # Get AI response
        ai_response = send_message(conversation)
        print(f"AI: {ai_response}\n")
        
        # Add AI response to conversation history (maintains context)
        conversation.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    print("Chat with Ollama! Type 'quit' to exit.\n")
    chat_loop()
