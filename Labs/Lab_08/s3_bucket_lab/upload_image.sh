#!/bin/bash

# positional arguments
LOCAL_FILE=$1
BUCKET=$2
EXPIRES=$3

# extract the file name, because witht he whole file path the image doesnt work
FILENAME=$(basename "$LOCAL_FILE")

# upload file
echo "Uploading $LOCAL_FILE to s3://$BUCKET/$FILENAME."
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/$FILENAME"

if [ $? -ne 0 ]; then
    echo "Upload failed."
    exit 1
fi

# Generate presigned URL
echo "Generating presigned URL for $FILENAME with expiration $EXPIRES seconds."
PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET/$FILENAME" --expires-in "$EXPIRES")

echo "Presigned URL: "
echo "$PRESIGNED_URL"
