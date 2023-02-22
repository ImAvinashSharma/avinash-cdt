import json
import boto3
from botocore.exceptions import ClientError


def add_bucket_public_access(bucketName: str):
    try:

        s3 = boto3.client("s3")
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucketName}/*"
                }
            ]
        }

        s3.put_bucket_website(
            Bucket=bucketName,
            WebsiteConfiguration={
                'IndexDocument': {'Suffix': 'index.html'},
                'ErrorDocument': {'Key': 'index.html'}
            }
        )

        s3.put_bucket_policy(Bucket=bucketName,
                             Policy=json.dumps(bucket_policy))

        response = s3.put_public_access_block(
            Bucket=bucketName,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )

        website_url = f"http://{bucketName}.s3-website.ap-south-1.amazonaws.com"
        print(f"website url:: {website_url}")

    except ClientError as e:
        print("error occurred during 'at adding Bucket policy': %s" % e)
