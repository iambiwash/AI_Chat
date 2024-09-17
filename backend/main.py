#uvicorn main:app
#uvicorn main:app --reload

#main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Get Environment Vars
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Import the custom functions here

from functions.openai_requests import convert_audio2txt

#Initiate App
app = FastAPI()

#CORS - Origin
origins = [
    "https://localhost:5173",
    "https://localhost:5174",
    "https://localhost:4173",
    "https://localhost:4174",
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

# Check Status
@app.get("/status")
async def post_audio():
   print("Status Ok")

# Get Audio 
@app.get("/post-audio-get/")
async def get_audio():

    # Get Saved Audio
    audio_input = open("my_voice.mp3", "rb")

    # Decode Audio to Text
    decoded_audio_text = convert_audio2txt(audio_input)

    print(decoded_audio_text)

    return "Audio Decoded"

# # Post bot response
# # Note: Not playing back in browser when using post request.
# # Sending your file from frontend to backend
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#    print('hello')