import boto3
import uuid
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')

def convert_to_uppercase(text_path, converted_path):
    with open(text_path, 'r') as text_file:
        text = text_file.read()
        converted_text = text.upper()

    with open(converted_path, 'w') as converted_file:
        converted_file.write(converted_text)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        tmpkey = key.replace('/', '')
        download_path = f'/tmp/{uuid.uuid4()}{tmpkey}'
        upload_path = f'/tmp/converted-{tmpkey}'

        s3_client.download_file(bucket, key, download_path)
        convert_to_uppercase(download_path, upload_path)
        s3_client.upload_file(upload_path, f'{bucket}-converted', f'converted-{key}')
