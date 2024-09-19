import json
import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

def send_email(name, email, message):
    client = boto3.client('ses', region_name=os.getenv("AWS_REGION"), aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))    
    
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

def lambda_handler(event, context):
    try:
        return send_email(event["name"], event["email"], event["message"])
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"error: {e.message}")   
        }
    
    