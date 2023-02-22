import boto3
import os


def create_keypair():
    ec2 = boto3.client('ec2')

    key_pair_name = "avi_test"

    response = ec2.create_key_pair(KeyName=key_pair_name)

    with open(key_pair_name + '.pem', 'w') as f:
        f.write(response['KeyMaterial'])
    os.chmod(key_pair_name + '.pem', 0o400)
