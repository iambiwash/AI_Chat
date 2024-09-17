#uvicorn main:app
#uvicorn main:app --reload

#main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Import the custom functions here
from functions.openai_requests import convert_audio_to_text, get_chat_response


# Get Environment Vars
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")


#Initiate App
app = FastAPI()

#CORS - Origin
origins = [
    "https://localhost:5173",
    "https://localhost:5174",
    "https://localhost:4173",
    "https://localhost:3000",
]

#CORS - Origin
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Check health Status
@app.get("/health")
async def check_health():
   return {"response": "healthy"}

# Get Audio 
@app.get("/post-audio/")
async def get_audio():

    # Get Saved Audio
    audio_input = open("my_voice.mp3", "rb")

    # Decode Audio to Text
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message was decoded 
    if not message_decoded:
        return HTTPException(status_code=400, detail= "Failed to decode the Audio.")
    

    # Get ChatGPT Response here
    chat_response = get_chat_response(message_decoded)

    print(chat_response)

    return "Audio Decoded"

# # Post bot response
# # Note: Not playing back in browser when using post request.
# # Sending your file from frontend to backend
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#    print('hello')