# STEP 4: Real-time AI Thinking Display 
# Shows thinking WHILE it happens, not after completion

import requests
import json

MODEL_NAME = "gpt-oss:20b"
OLLAMA_URL = "http://localhost:11434"

THINKING_COLOR = "\033[90m"  # Gray color - makes thinking less prominent than answers
RESET_COLOR = "\033[0m"      # Reset to default terminal color (important for clean output)

def send_message_with_thinking(system_prompt, user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    
    # think=True: Enables AI to show internal reasoning process
    # stream=True: Sends response in real-time chunks instead of waiting for completion
    payload = {"model": MODEL_NAME, "messages": messages, "think": True, "stream": True}
    
    # Make streaming request to Ollama API
    # stream=True parameter here enables processing chunks as they arrive
    response = requests.post(f"{OLLAMA_URL}/api/chat", json=payload, stream=True)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"
    
    # State tracking variables to control output formatting
    # These prevent duplicate headers and manage visual flow
    thinking_shown = False  # Have we started showing thinking section?
    answer_shown = False    # Have we started showing the answer section?
    
    for line in response.iter_lines():
        if line:  # Skip empty lines (common in streaming responses)
            try:
                # Parse JSON chunk - each line contains a piece of the response
                chunk = json.loads(line.decode('utf-8'))
                
                # THINKING PHASE: Handle AI's internal reasoning process
                # This shows HOW the AI is thinking about the problem
                if 'message' in chunk and 'thinking' in chunk['message']:
                    # First thinking chunk - display header with colored formatting
                    if not thinking_shown:
                        # \n creates spacing from previous output
                        # THINKING_COLOR makes text gray (less prominent)
                        # end="" prevents newline, flush=True forces immediate display
                        print(f"\n{THINKING_COLOR}AI thinking: ", end="", flush=True)
                        thinking_shown = True
                    
                    # Extract thinking content from this chunk
                    thinking_content = chunk['message']['thinking']
                    if thinking_content:
                        # CRITICAL: flush=True makes text appear immediately
                        # Without flush, Python buffers output until newline or buffer full
                        # This creates the real-time "typing" effect
                        print(thinking_content, end="", flush=True)
                
                # The polished answer after thinking is complete
                elif 'message' in chunk and 'content' in chunk['message']:
                    # First answer chunk - display header and reset formatting
                    if not answer_shown:
                        if thinking_shown:
                            # Reset color back to normal, add spacing after thinking
                            # Double \n creates clear separation between thinking and answer
                            print(f"{RESET_COLOR}\n\nAI answer: ", end="", flush=True)
                        else:
                            # Edge case: model provided answer without showing thinking
                            print("\nAI answer: ", end="", flush=True)
                        answer_shown = True
                    
                    # Extract answer content from this chunk
                    answer_content = chunk['message']['content']
                    if answer_content:
                        # Stream answer in real-time just like thinking
                        # User sees words appear as AI generates them
                        print(answer_content, end="", flush=True)
                        
            except json.JSONDecodeError:
                continue

    print()

if __name__ == "__main__":
    system = "You are a helpful AI expert. Think step by step before answering."
    user = "What is CoT in LLMs? Explain in one sentence."
    print(f"System: {system}")
    print(f"\nUser: {user}")
    send_message_with_thinking(system, user)
