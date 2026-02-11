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

    if "my name is" in msg or "i am" in msg or "i'm" in msg:
        name = user_msg.lower().split("my name is")[-1].strip()
        memory["name"] = name

    if "i like" in msg:
        like = user_msg.split("like")[-1].strip()
        memory["preference"] = like

        if "preferences" not in memory:
            memory["preferences"] = []

        # normalize text (avoid duplicates like AI vs ai)
        like = like.capitalize()

        # add without overwriting
        if like not in memory["preferences"]:
            memory["preferences"].append(like)

    if "my favorite movie is" in msg or "i like to watch" in msg:
        movie = user_msg.split("is")[-1].strip()
        memory["liked_movie"] = movie

    if "eat" in msg:
        food = user_msg.split("eat")[-1].strip()
        memory["food"] = food

    if "call me after" in msg:
        time = user_msg.split("after")[-1].strip()
        memory["call_time"] = time

    if "my exam is" in msg:
        exam = user_msg.lower().split("my exam is")[-1].strip()
        memory["exam"] = exam
        
    if "i listen to" in msg or "i listen to" in msg:
        song = user_msg.split("to")[-1].strip()
        memory["song"] = song

    if "my birthday is on" in msg:
        birthday = user_msg.lower().split("is on")[-1].strip()
        memory["birthday"] = birthday
        
    if "remind me of" in msg:
        event = user_msg.lower().split("of")[-1].strip()
        memory["event"] = event

    return memory

# create smart reply using memory
def build_memory_context(memory):
    context = ""
    if "name" in memory:
        context += f"User name is {memory['name']}. "
    if "preference" in memory and isinstance(memory["preferences"], list):
        likes = ", ".join(memory["preference"])
        context += f"User likes {likes}. "
    if "call_time" in memory:
        context += f"Call user after {memory['call_time']}. "
    if "exam" in memory:
        context += f"User exam is {memory['exam']}. "
    if "liked_movie" in memory:
        context += f"User likes {memory['liked_movie']}. "
    if "food" in memory:
        context += f"User likes {memory['food']}. "
    if "song" in memory:
        context += f"User likes {memory['song']}. "
    if "birthday" in memory:
        context += f"User's birthday is on {memory['birthday']}. "
    if "event" in memory:
        context += f"User has a even {memory['event']}"
    return context
