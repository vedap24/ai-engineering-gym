import os
import json
from dotenv import load_dotenv
from groq import Groq

# Setup API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 1. Define our Local Tools (The Agent's Hands & Brain)
def calculate_addition(a, b):
    print(f"   [Tool Executing] Adding {a} + {b}...")
    return str(a + b)

def search_company_policy(query):
    print(f"   [Tool Executing] Searching Vector DB for: '{query}'...")
    # (In real life, ChromaDB code goes here. For now, we mock it)
    if "pet" in query.lower():
        return "Employees can bring dogs and puppies to the office."
    return "No exact policy found. Please contact HR."

# The Agent's Menu Card with 2 Superpowers!
tools_menu = [
    {
        "type": "function",
        "function": {
            "name": "calculate_addition",
            "description": "Adds two numbers. Use this ONLY when the user asks you to do math or add numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_policy",
            "description": "Searches the private vector database for company rules, HR policies, leaves, and WFH guidelines. Use this when the user asks about the company.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The exact search term to look for in the database (e.g., 'pet policy', 'wfh days')"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# 3. Chat Loop
print("🤖 Ultimate Agent is Ready! (Type 'exit' to quit)")
messages = [{"role": "system", "content": "You are a helpful AI assistant with tools."}]

while True:
    user_input = input("\n👤 You: ")
    if user_input.lower() == 'exit':
        break
        
    messages.append({"role": "user", "content": user_input})
    
    # Send to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools_menu,
        tool_choice="auto" # Let the AI decide!
    )
    
    response_message = response.choices[0].message
    
    # 4. Agentic Routing!
    if response_message.tool_calls:
        tool_call = response_message.tool_calls[0]
        function_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        # Routing logic
        if function_name == "calculate_addition":
            tool_result = calculate_addition(args.get("a"), args.get("b"))
        elif function_name == "search_company_policy":
            tool_result = search_company_policy(args.get("query"))
            
        print(f"🤖 AI used {function_name} and got: {tool_result}")
        
    else:
        # The 'else' block you perfectly guessed! Just normal chat.
        print(f"🤖 AI: {response_message.content}")