import os
import json
from dotenv import load_dotenv
from groq import Groq

# 1. Setup API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Idi mana Tool (Function)
def calculate_addition(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b
# 3. AI ki ivvaboye Menu Card (Tool Schema)
tools_menu = [
    {
        "type": "function",
        "function": {
            "name": "calculate_addition",
            "description": "Adds two numbers and returns the result. Use this when the user asks you to add numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "The first number to add"
                    },
                    "b": {
                        "type": "integer",
                        "description": "The second number to add"
                    }
                },
                "required": ["a", "b"]
            }
        }
    }
]
# 4. Giving question and tools to AI and asking it to choose the right tool if needed
user_message = input("\n👤 Enter your math question: ")
print(f"👤 User: {user_message}")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile", # Tool calling ki ee model chala baaga pani chestundi
    messages=[{"role": "user", "content": user_message}],
    tools=tools_menu,
    tool_choice="auto" # "Avasaram aithe tool vaduko" ani AI ki chepthunnam
)

ai_message = response.choices[0].message

# 5. Tool call unte, em cheyali?
if ai_message.tool_calls:
    print("\n🛠️ AI wants to use a tool!")
    
    # AI pampinchina tool details teesukuntunnam
    tool_call = ai_message.tool_calls[0]
    function_name = tool_call.function.name
    arguments_string = tool_call.function.arguments # <-- Ikkada define ayyindi
    
    print(f"📞 AI is calling: {function_name}")
    print(f"📦 With arguments: {arguments_string}")
    
    # Step 6: Convert JSON string to Python Dictionary
    arguments_dict = json.loads(arguments_string)
    
    # Extract the numbers
    number_a = arguments_dict["a"]
    number_b = arguments_dict["b"]
    
    # RUN OUR FUNCTION! 🚀
    print(f"⚙️ Running calculate_addition({number_a}, {number_b})...")
    result = calculate_addition(number_a, number_b)
    
    print(f"✅ Result from our Python Tool: {result}")

    # Step 7: Message history loki AI tool call request ni append chesthunnam
    messages = [{"role": "user", "content": user_message}]
    messages.append(ai_message) # AI adigina tool call
    
    # Mana function ichina result ni kuda append chesthunnam (role "tool" tho)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "name": function_name,
        "content": str(result) # Answer ni string ga marchi isthunnam
    })
    
    # Malli AI ki history pampisthunnam (2nd Call)
    print("\n🔄 Sending the result back to AI...")
    second_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    final_answer = second_response.choices[0].message.content
    print(f"\n🤖 Agent Final Answer: {final_answer}")

else:
    print(f"\n🤖 Agent: {ai_message.content}")