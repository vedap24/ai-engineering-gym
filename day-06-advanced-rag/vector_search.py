import chromadb

# 1. Initialize Vector Database (Local in-memory)
print("🔌 Starting Vector Database...")
client = chromadb.Client()

# 2. Create a "Collection" (Like a table in SQL)
collection = client.create_collection(name="company_policies")

# 3. Add chunks of data (Chroma DB will automatically create Embeddings!)
print("📚 Adding documents and generating Embeddings...")
collection.add(
    documents=[
        "Employees can bring their dogs and puppies to the office.",
        "Work from home is allowed on Thursdays and Fridays.",
        "The cafeteria serves free lunch on Wednesdays."
    ],
    ids=["policy_pets", "policy_wfh", "policy_food"]
)

# 4. Perform a Vector Similarity Search
user_query = input("\n👤 Enter your question: ")        # Ex: "Can I bring my pet?"
print(f"\n👤 User asks: '{user_query}'")

print("🔍 Searching for the most similar meaning (not exact words)...")
results = collection.query(
    query_texts=[user_query],
    n_results=1 # Only get the top 1 most relevant chunk
)

# 5. Display the magic!
best_match = results['documents'][0][0]
print(f"✅ Best Match Found: {best_match}")