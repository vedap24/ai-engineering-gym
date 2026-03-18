import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_user_info(user_text):
    print("⏳ Processing your text to extract data...")
    
    # 1. Prompt Engineering: We STRICTLY order it to return JSON
    system_prompt = """
    You are an expert Data Extraction Agent. 
    Your job is to extract the 'name', 'age', and 'location' from the user's text.
    You MUST respond ONLY in valid JSON format. 
    Do not add any conversational text before or after the JSON.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            # 2. Output Parsing: Forcing the API to lock into JSON mode
            response_format={"type": "json_object"}
        )
        
        # Get the text response
        raw_output = response.choices[0].message.content
        
        # 3. Parse it into a Python Dictionary
        parsed_data = json.loads(raw_output)
        
        print("\n✅ Extraction Successful!")
        print(f"Name extracted: {parsed_data.get('name', 'N/A')}")
        print(f"Age extracted: {parsed_data.get('age', 'N/A')}")
        print(f"Location extracted: {parsed_data.get('location', 'N/A')}")
        
        print("\n📦 The raw JSON looked like this:")
        print(raw_output)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🤖 JSON Extraction Agent Online.")
    sample_text = input("Tell me about someone (e.g., 'My friend Rahul is 25 and lives in Hyderabad'): ")
    extract_user_info(sample_text)