from fastapi import FastAPI
from send_mail import send_email
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class EmailContent(BaseModel):
     name:str
     email:str
     message:str

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
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully")
    }
    