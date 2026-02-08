import os
import json
import streamlit as st
from google import genai
from google.genai import types

# --- MEMORY HELPERS ---
def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            return json.load(f)
    return {"name": "Unknown", "hobbies": []}

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f)

# --- APP SETUP ---
st.set_page_config(page_title="Memory Bot")
user_data = load_memory()

st.title(f"👋 Welcome back, {user_data['name']}!")
api_key = st.sidebar.text_input("Gemini API Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    for m in client.models.list():
        if 'generateContent' in m.supported_actions:
            print(m.name)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Say something..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # SYSTEM PROMPT: Injecting the long-term memory
        system_info = f"User Name: {user_data['name']}. Hobbies: {', '.join(user_data['hobbies'])}."
        
        with st.chat_message("assistant"):
            # Simplified generate call for the hackathon
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=f"System context: {system_info}\nUser: {prompt}"
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

        # --- BACKGROUND TASK: Update Memory ---
        # Ask the AI to extract facts from the last message
        extraction_prompt = f"Extract the user's name or hobbies from this text: '{prompt}'. Return JSON only: {{\"name\": \"...\", \"hobbies\": []}}"
        fact_check = client.models.generate_content(model="gemini-2.5-flash", contents=extraction_prompt)
        
        try:
            new_facts = json.loads(fact_check.text)
            if new_facts.get("name") and new_facts["name"] != "Unknown":
                user_data["name"] = new_facts["name"]
            user_data["hobbies"] = list(set(user_data["hobbies"] + new_facts.get("hobbies", [])))
            save_memory(user_data)
        except:
            pass # Skip if AI didn't return perfect JSON