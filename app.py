from google import genai
from memory_system import load_memory, save_memory, extract_memory, build_memory_context

# 🔑 put your Gemini API key here!!!
client = genai.Client(api_key="AIzaSyADZDrsTBFIRrg_oF6X_vZl1hySJE5m1LY")
print("🧠 Infinity Memory AI Started (type 'exit' to stop)\n")

memory = load_memory()

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    # extract and save memory
    memory = extract_memory(user, memory)
    save_memory(memory)

    # build memory context
    memory_context = build_memory_context(memory)
    #AI is getting prompted here
    prompt = f"""
    You are a smart AI assistant with memory.

    Stored memory:
    {memory_context}

    User message: {user}
    Reply smartly using memory if needed.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt 
    )
    print("Bot:", response.text)

    # show memory used (For Hackathon judges)
    print("\nActive Memory:", memory)
    print("--------------------------------------------------")
