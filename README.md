# gpt-oss-2b-in-Python

📺 **Video Tutorial:**
https://youtu.be/31MDEpx2oXA?feature=shared

Build a Complete AI Chat System with Ollama + Python in a Few Steps! Starting from a basic short HTTP request, we'll add conversation memory, real-time streaming responses, and advanced AI thinking display - all using just basic Python libraries. 

# 🤖 gpt-oss-20b + Ollama + Python Integration Demo

A progressive 4-step demo showing how to integrate Ollama with Python to load an run gpt-oss-20b, from basic connection to advanced AI thinking display.

## 🚀 Quick Start 

1. **Install Ollama** and pull the model:
   ```bash
   ollama pull gpt-oss:20b
   ollama serve
   ```

2. **Install Python dependencies**:
   ```bash
   pip install requests
   ```

3. **Run the steps**:
   ```bash
   python step1_basic.py
   python step2_memory.py
   python step3_streaming.py
   python step4_thinking.py
   ```

## 📚 What Each Step Does

| Step | Feature | Demo |
|------|---------|------|
| **1** | Basic Connection | Single question → answer |
| **2** | Conversation Memory | Interactive chat with context |
| **3** | Real-time Streaming | Word-by-word responses |
| **4** | AI Thinking Display | See AI reasoning in real-time |

## 🎯 Key Features

- ✅ **System/User roles** - Proper message structure
- ✅ **Conversation memory** - Context across messages  
- ✅ **Real-time streaming** - ChatGPT-like experience
- ✅ **AI thinking** - Transparent reasoning process
- ✅ **No external dependencies** - Just `requests` + `json`

## 💡 Usage Examples

### Basic Connection (Step 1)
```python
import requests

response = requests.post("http://localhost:11434/api/chat", json={
    "model": "gpt-oss:20b",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"}
    ]
})
```

### AI Thinking (Step 4)
```bash
User: What is Chain-of-Thought in LLMs?

AI thinking: The user is asking about CoT... this refers to Chain-of-Thought prompting... it's a technique that helps LLMs reason step by step...

AI answer: Chain-of-Thought (CoT) is a prompting technique that guides LLMs to show their reasoning steps before providing a final answer.
```

## 🛠️ Requirements

- **Ollama** running locally - free version (`ollama serve`)
- **Python 3.7+** with `requests` library
- **Model**: `gpt-oss:20b` (or change `MODEL_NAME` variable)

## 📝 Notes

- Each step is **self-contained** and runnable independently
- Perfect for **learning** and **demo presentations**
- **No classes** - simple function-based approach
- **Minimal code** - focus on core concepts

## 🎨 Demo Features

- **Colored output** for AI thinking (gray text)
- **Real-time streaming** with proper `flush=True`
- **Clean formatting** with line spacing
- **Error handling** for robust operation

---

**Perfect for**: Learning Ollama integration, demo presentations, quick prototypes, and building AI-powered applications! 🚀
