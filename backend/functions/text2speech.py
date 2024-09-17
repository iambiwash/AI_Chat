import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

#ELEVEN LABS
# Convert the text to speech
def text_to_speech(message):
    body = {
        "text": message,
        "voice_setting" : {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    #Define Voise from Eleven Labs
    voice_EverestAI = "pNInz6obpgDQGcFmaJgB"


    # Constructing Headers and Endpoints
    headers = {"xi-api-key" : ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_EverestAI}"

    # Send Request

    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return 
    
    # Handle response
    if response.status_code == 200:
        return response.content
    else:
        return