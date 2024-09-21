import json
import boto3
from botocore.exceptions import ClientError
import requests

def send_email(name, email, message):
    client = boto3.client('ses')   
    
    try:    
        client.send_email(
            Destination={
                'ToAddresses': ["meszarosr734@gmail.com"]
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': message,
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': f"{name} - {email} wants to connect",
                },
            },
            Source='contact@robert-meszaros.com'
            )
        
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': e.response['Error']['Message']
        }
    
    else:
        return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully")
    }

def verify_captcha(token):
    data = {
            'secret': os.getenv("RECAPTCHA_SECRET_KEY"),
            'response': token
        }

    request = requests.post("https://www.google.com/recaptcha/api/siteverify", data = data)

    if request.status_code != 200 or request.json()["success"] == False:
        raise Exception(request.json()["error-codes"])

def lambda_handler(event, context):
    try:
        event_obj = json.loads(event)
        body = event_obj["body"]

        verify_captcha(body["token"])   

        name = body["name"]
        email = body["email"]
        message = body["message"]
        return send_email(name, email ,message)
    
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"error: {e}")   
        }
    
    