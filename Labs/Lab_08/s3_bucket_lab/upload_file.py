import os
import boto3

s3 = boto3.client('s3', region_name="us-east-1")
bucket = 'ds2002-f25-hzy8ha'
local_file = '~/Downloads/bibble.jpg'
local_file_path = os.path.expanduser(local_file) # added this line because was getting file not found error for using ~ in path

# 1. Open the file in binary read mode ('rb')
with open(local_file_path, 'rb') as data:
    resp = s3.put_object(
        Body=data,        # PASS THE OPEN FILE OBJECT HERE
        Bucket=bucket,
	ACL='public-read',
        Key=os.path.basename(local_file_path)    # This is the destination key/path in S3 - again used correct file path
)
