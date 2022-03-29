import os
import json
import boto3
import smtplib
from email.message import EmailMessage
from os import environ
from datetime import date
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import json
import base64
from io import BytesIO

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

#S3 bucket name 
destination_bucketname = os.environ['test_yolo_bucket']
destination = 'test-yolo-bucket'
def lambda_handler(event, context):
    print ("in lambda function")
    try:
        print ("in first try")
        image_bytes = event['body'].encode('utf-8')       
        decodeit = open('/tmp/1.png', 'wb')
        image=(base64.b64decode((image_bytes)))
        decodeit.write(image)
        decodeit.close()
    except Exception as e:
        print ("in first except",e)
    filename = "l.png"
    print('before downloading file from S3, filename: at /tmp/', filename)
    print('inside this directory: ',os.getcwd())
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print('contents in current directory:', files)
    print ("checking how many images in tmp folder")
    print('files in /tmp/ are: ', os.system('ls /tmp/')
    print('before calling detect python file')
    try:
        os.system("python3 detect.py --project /tmp/ --exist-ok  --save-txt --source /tmp/1.png")
    except Exception as e:
        print('exception occurred in detect python file: ', e)

    print('before uploading output file to destination S3 bucket')
    
    try:
        s3.upload_file('/tmp/exp/'+filename, destination_bucketname,"output_images/"+filename)
    except:
        print('inside exp 2 ')
        s3.upload_file('/tmp/exp2/'+filename, destination_bucketname,"output_images/"+ filename)
    
    print('end of yolo processing and uploading output image to s3 bucket')

