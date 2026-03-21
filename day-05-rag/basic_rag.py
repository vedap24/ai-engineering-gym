import os
from dotenv import load_dotenv
from groq import Groq

# 1. Setup API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Read the local document using 'open'
print("📂 Reading company_policy.txt...")
with open("company_policy.txt", "r") as file:
    document_text = file.read()

print("✅ Document read successfully!")

# 3. Augment: Combine Document + Question
user_question = input("\n👤 Ask a question about the policy: ")

# F-string magic! We instruct AI to ONLY use the provided text.
rag_prompt = f"""
Here is the company policy document:
---------------------
{document_text}
---------------------
Based ONLY on the document above, answer the user's question. 
If the answer is not in the document, say "I don't know based on the document."

Question: {user_question}
"""

# 4. Generate: Send to AI
print("\n🧠 Sending document and question to AI...")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": rag_prompt}]
)

print(f"\n🤖 AI Answer: {response.choices[0].message.content}")