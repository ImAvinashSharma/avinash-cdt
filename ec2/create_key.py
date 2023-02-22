import boto3
import os
from botocore.exceptions import ClientError


def create_keypair(key_pair_name):
    try:
        ec2 = boto3.client('ec2')

        response = ec2.create_key_pair(KeyName=key_pair_name)

        with open(key_pair_name + '.pem', 'w') as f:
            f.write(response['KeyMaterial'])
        os.chmod(key_pair_name + '.pem', 0o400)
    except ClientError as e:
        print("error occurred during creation of key pair : % s" % e)
