#!/usr/bin/env python3

import os
import boto3
import requests
import argparse

# using requests code given to download file
def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")
        exit(1)

# command line arguments to fetch
parser = argparse.ArgumentParser(description="Download file, upload to S3, generate presigned URL")
parser.add_argument("file_url", help="URL of the file to download")
parser.add_argument("bucket", help="S3 bucket name")
parser.add_argument("--expires", type=int, default=604800, help="Expiration time for presigned URL in seconds (default 7 days)")

args = parser.parse_args()

# vars
file_url = args.file_url
bucket_name = args.bucket
expires_in = args.expires

# use download func
filename=os.path.basename(file_url) # use os here too so correct part of given path is used
local_path = os.path.join(os.getcwd(), filename)
download_file(file_url, local_path)

# upload to s3
s3 = boto3.client("s3", region_name="us-east-1")  # adjust region if needed
print(f"Uploading {local_path} to s3://{bucket_name}/{filename} ...")
s3.upload_file(
    Filename=local_path,
    Bucket=bucket_name,
    Key=filename,
    ExtraArgs={"ACL": "private"}  # default
)
print("Upload complete.")

# generate url (given)
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': filename},
    ExpiresIn=expires_in
)

print(f"Presigned URL, expires in {expires_in} seconds:")
print(response)
