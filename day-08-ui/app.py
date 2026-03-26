import streamlit as st
import os
import json
from dotenv import load_dotenv
from groq import Groq

# 1. Setup API & Page
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Ultimate AI Agent", page_icon="🤖")
st.title("🤖 My Ultimate AI Agent")
st.caption("Powered by Groq, Python, and Streamlit")

# 2. Define our Local Tools
def calculate_addition(a, b):
    return str(a + b)

def search_company_policy(query):
    if "pet" in query.lower():
        return "Employees can bring dogs and puppies to the office."
    return "No exact policy found."

tools_menu = [
    {
        "type": "function",
        "function": {
            "name": "calculate_addition",
            "description": "Adds two numbers.",
            "parameters": {"type": "object", "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}}, "required": ["a", "b"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_policy",
            "description": "Searches for company rules and HR policies.",
            "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
        }
    }
]

# 3. Streamlit Memory (Session State)
# Day 3 lo manam list () vaadam, browser kosam st.session_state vadutham
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful AI assistant with tools."}]

# Patha messages anni screen meeda print cheyadaniki
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# 4. The Chat Input Box
if user_input := st.chat_input("Ask me a math question or policy question..."):
    # User message ni memory lo add chesi screen meeda chupinchu
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI ki pampinchu
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            tools=tools_menu,
            tool_choice="auto"
        )
        
        response_msg = response.choices[0].message
        
        # 5. Agentic Routing logic
        if response_msg.tool_calls:
            tool_call = response_msg.tool_calls[0]
            func_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            
            if func_name == "calculate_addition":
                result = calculate_addition(args.get("a"), args.get("b"))
                final_text = f"🛠️ **Tool Used:** Calculator\n\n**Result:** {result}"
            elif func_name == "search_company_policy":
                result = search_company_policy(args.get("query"))
                final_text = f"🔍 **Tool Used:** Vector Search\n\n**Result:** {result}"
                
            message_placeholder.markdown(final_text)
            st.session_state.messages.append({"role": "assistant", "content": final_text})
        else:
            message_placeholder.markdown(response_msg.content)
            st.session_state.messages.append({"role": "assistant", "content": response_msg.content})