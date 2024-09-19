import json
import random


# Get recent Messages

def get_recent_messages():
    # Define the file name and learn instruction
    # Prompt Engineering - basically teaching the AI its role and scope.
    file_name = "stored_data.json"
    learn_instruction = {
        "role" : "system",
        "content" : "You are a Japanese language Teacher. Say most words in english and try to teach me a single word in Japanese. Each message you send, you will teach me one new word. The information should be relevant to the topic requested.Your name is EverestAI. The user is called Biwash. Keep your answers to under 30 words."
    }

    # Content Example
    # "content" : "You are a personal assistant to the user. You will provide all the information requested by the user. The information should be relevant to the topic requested.Your name is EverestAI. The user is called Biwash. Keep your answers to under 30 words."
   

    # Initialize messages
    messages = []


    # Add a random element (We use this random to bring some surprises on few answers i.e adding humor, facts, challenges etc)
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include asking me to repeat something like words or sentence back to you in Japanese. Make sure not to repeat the same word while asking to translate back. Make sure you teach new words learning through the conversation."
    else:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will rather have some interesting fact regarding the topic and some light humour.."

    # Another Example
    # x = random.uniform(0, 1)
    # if x < 0.5:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humour."
    # else:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will rather have some interesting fact regarding the topic."


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


# Store Messages
def store_messages(input_message, response_message):

    # Define the file name
    file_name = "stored_data.json"

    # Get recent messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": input_message}
    ai_message = {"role": "assistant", "content": response_message}

    messages.append(user_message)
    messages.append(ai_message)

    # Save the updated file in database
    with open(file_name, "w") as f:
        json.dump(messages, f)


def reset_messages():

    # Overwrite the current file with nothing.
    open("stored_data.json", "w")