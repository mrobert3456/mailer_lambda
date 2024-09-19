from fastapi import FastAPI
from send_mail import lambda_handler
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
class EmailContent(BaseModel):
     name:str
     email:str
     message:str
     token:str

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/sendEmail")
async def send_email(EmailContent:EmailContent):
    gateway_event = json.dumps({"body": EmailContent.dict()})

    
    return lambda_handler(gateway_event, None)

    