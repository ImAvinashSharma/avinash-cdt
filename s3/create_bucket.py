import boto3
from botocore.exceptions import ClientError


def create_s3(bucketName: str):
    try:
        print("Creating S3 bucket...")

        s3 = boto3.client("s3")

        response = s3.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == bucketName:
                return "Bucket already exists.."
        s3.create_bucket(Bucket=bucketName, CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'})
        print("Bucket Name: " + bucketName)
        return "Bucket created..."
    except ClientError as e:
        print("error occurred during creating of bucket %s" % e)
