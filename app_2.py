import google.generativeai as genai
from memory_system import load_memory, save_memory, extract_memory, build_memory_context

# 🔑 put your Gemini API key here
genai.configure(api_key="API_KEY_HERE")

model = genai.GenerativeModel("gemini-pro")

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

    prompt = f"""
    You are a smart AI assistant with memory.

    Stored memory:
    {memory_context}

    User message: {user}
    Reply smartly using memory if needed.
    """

    response = model.generate_content(prompt)
    print("Bot:", response.text)

    # show memory used (impress judges)
    print("\nActive Memory:", memory)
    print("--------------------------------------------------")
