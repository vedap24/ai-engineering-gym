import os
from dotenv import load_dotenv
from groq import Groq

# Load the environment variables
load_dotenv()

# Groq client setup (instead of OpenAI)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def simple_agent():
    system_prompt = "You are a helpful AI assistant."
    
    print("🤖 Agent Online. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            break
            
        try:
            # Groq model (Llama 3) ki request
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant", # free and super fast Groq model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            
            ai_reply = response.choices[0].message.content
            print(f"🤖 Agent: {ai_reply}")
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    simple_agent()