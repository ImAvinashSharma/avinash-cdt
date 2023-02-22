import boto3
from botocore.exceptions import ClientError


def create_ec2(security_group_id, subnet_id, key_filename):
    try:
        print("Creating EC2 instance")

        ec2_client = boto3.client('ec2')
        instance = ec2_client.run_instances(
            ImageId='ami-0caf778a172362f1c',
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            SecurityGroupIds=[security_group_id],
            SubnetId=subnet_id,
            KeyName=key_filename,
        )

        print("Waiting EC2 instance to get ready...")
        instance_id = instance['Instances'][0]['InstanceId']

        ec2_client.get_waiter('instance_running').wait(
            InstanceIds=[instance_id])

        response = ec2_client.describe_instances(InstanceIds=[instance_id])

        public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        print("EC2 running")
        return public_ip
    except ClientError as e:
        print("error occurred while creation of ec2 instance : % s" % e)
