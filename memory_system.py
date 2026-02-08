import json

# load memory
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

# save memory
def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

# extract important info
def extract_memory(user_msg, memory):
    msg = user_msg.lower()

    if "my name is" in msg:
        name = user_msg.split("is")[-1].strip()
        memory["name"] = name

    if "i like" in msg:
        like = user_msg.split("like")[-1].strip()
        memory["preference"] = like

    if "call me after" in msg:
        time = user_msg.split("after")[-1].strip()
        memory["call_time"] = time

    if "my exam is" in msg:
        exam = user_msg.split("is")[-1].strip()
        memory["exam"] = exam

    return memory

# create smart reply using memory
def build_memory_context(memory):
    context = ""
    if "name" in memory:
        context += f"User name is {memory['name']}. "
    if "preference" in memory:
        context += f"User likes {memory['preference']}. "
    if "call_time" in memory:
        context += f"Call user after {memory['call_time']}. "
    if "exam" in memory:
        context += f"User exam is {memory['exam']}. "
    return context
