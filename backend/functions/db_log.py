import json
import random


# Get recent Messages

def get_recent_messages():
    # Define the file name and learn instruction
    # Prompt Engineering - basically teaching the AI its role and scope.
    file_name = "stored_data.json"
    learn_instruction = {
        "role" : "system",
        "content" : "You are a personal assistant to the user. You will provide all the information requested by the user. The information should be relevant to the topic requested.Your name is NepalGPT. The user is called Biwash. Keep your answers to under 30 words."
    }

    # Initialize messages
    messages = []


    # Add a random element (We use this random to bring some surprises on few answers i.e adding humor, facts, challenges etc)
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will rather have some interesting fact regarding the topic."

    

    # Append instruction to messages
    messages.append(learn_instruction)


    # Get last Messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
            else:
                for item in data[-5:]:
                    messages.append(item)
    except Exception as e:
        print(e)
        pass

    return messages
