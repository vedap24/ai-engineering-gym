## Day 1: Local Environment Setup & The First AI Agent

### 🎯 Objective
To set up a secure local Python environment, integrate a Large Language Model (LLM) via API, and solve a foundational DSA problem related to AI memory (HashMaps).

### 🛠️ Tech Stack Used
* **Language:** Python
* **AI Model:** `llama-3.1-8b-instant` (via Groq API)
* **Libraries:** `groq`, `python-dotenv`
* **Version Control:** Git & GitHub

### 🚀 Steps Executed
1. **Virtual Environment Setup:** Created an isolated Python space (`venv`) to manage dependencies cleanly.
2. **API Security:** Set up a `.env` file to store the API key securely.
3. **Git Ignore:** Configured `.gitignore` to prevent the accidental upload of `.env` and `venv` to GitHub.
4. **Built a CLI AI Agent:** Wrote a Python script (`simple_agent.py`) using the Groq API that maintains an infinite loop (REPL) to chat with the LLM directly from the terminal.
5. **Logic Building (DSA):** Solved LeetCode 242 (Valid Anagram) using HashMaps. This logic mimics how LLMs perform token frequency counting (Bag of Words).

### 💻 Code Snippets

**1. The Groq AI Agent (`day-01-setup/simple_agent.py`)**
```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def simple_agent():
    system_prompt = "You are a helpful AI assistant."
    print("🤖 Agent Online. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            print(f"🤖 Agent: {response.choices[0].message.content}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    simple_agent()