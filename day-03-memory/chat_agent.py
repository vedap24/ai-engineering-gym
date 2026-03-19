import os
from dotenv import load_dotenv
from groq import Groq

# 1. Setup API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Initialize Memory (Empty List)
chat_history = []

print("🧠 Memory Agent Online. Type 'exit' to quit.")

# 3. The Infinite Chat Loop
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == 'exit':
        print("👋 Goodbye! Ending chat.")
        break
        
    # 4. Save User Message
    chat_history.append({"role": "user", "content": user_input})
    
    try:
        # 5. Send Full History to AI
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=chat_history
        )
        
        ai_reply = response.choices[0].message.content
        print(f"🤖 Agent: {ai_reply}")
        
        # 6. Save AI Message (Meeru cheppina exact logic ikkade undi!)
        chat_history.append({"role": "assistant", "content": ai_reply})
        # AI answer save ayina ventane, memory limit cross ayyindemo check chestham.
        if len(chat_history) > 6:
            chat_history.pop(0)
    except Exception as e:
        print(f"Error: {e}")