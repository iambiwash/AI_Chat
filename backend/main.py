#uvicorn main:app
#uvicorn main:app --reload

#main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


#Custom Function Imports

#Initiate App
app = FastAPI()

#CORS - Origin
origins = [
    "https://localhost:5173",
    "https://localhost:5174",
    "https://localhost:4173",
    "https://localhost:4174",
    "https://localhost:3000"
]


@app.get("/")
async def root():
    print("Hello")
    return {"message": "Hello World"}