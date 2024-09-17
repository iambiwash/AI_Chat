import openai
from decouple import config


#Retrieve Environment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")


# Use Open AI - Whisper
# Convert Audio to Text

def convert_audio2txt(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        messsage_text = transcript["text"]
        return messsage_text
    except Exception as e:
        print(e)
        return