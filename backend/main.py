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
from functions.db_log import store_messages, reset_messages
from functions.text2speech import text_to_speech


# Get Environment Vars
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")


#Initiate App
app = FastAPI()


#CORS - Origin
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
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
   return {"message": "healthy"}



# Reset Messages
@app.get("/reset")
async def reset_conversation():
   reset_messages()


# Get Audio 
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # # Get Saved Audio 
    # audio_input = open("my_voice.mp3", "rb")

    # Save file from frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")


    # Decode Audio to Text
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message was decoded 
    if not message_decoded:
        return HTTPException(status_code=400, detail= "Failed to decode the Audio.")
    

    # Get ChatGPT Response here
    chat_response = get_chat_response(message_decoded)

    # Guard: Ensure chat response is received.
    if not chat_response:
        return HTTPException(status_code=400, detail= "Failed to get chat response.")

    # Store Messages
    store_messages(message_decoded, chat_response)

    # Convert chat response to Audio
    # print(chat_response) #---Debugging step for response
    audio_output = text_to_speech(chat_response)

    # Guard: Ensure message was decoded 
    if not audio_output:
        return HTTPException(status_code=400, detail= "Failed to get Eleven Labs Audio Response")
    
    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return Audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")


# # Post bot response
# # Note: Not playing back in browser when using post request.
# # Sending your file from frontend to backend
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#    print('hello')