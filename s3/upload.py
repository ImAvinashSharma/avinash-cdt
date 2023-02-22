import boto3
import os
from botocore.exceptions import ClientError


def upload_file(file_name: str, bucketName: str):
    try:
        object_name = os.path.basename(file_name)

        s3_client = boto3.client('s3')
        response = s3_client.upload_file(file_name, bucketName, object_name, ExtraArgs={
                                         'ContentType': 'text/html'})
    except ClientError as e:
        print("error occurred during file upload : % s" % e)
