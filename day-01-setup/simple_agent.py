import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load Environment Variables (Security First)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_agent():
    # 2. The "Context" (System Prompt)
    system_prompt = "You are a helpful AI assistant capable of answering queries concisely."
    
    print("🤖 Agent Online. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
            
        # 3. The API Call (The 'Brain')
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # Or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            
            # 4. Extract Content
            ai_reply = response.choices[0].message.content
            print(f"Agent: {ai_reply}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_agent()

