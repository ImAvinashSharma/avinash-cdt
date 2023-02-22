import boto3
from botocore.exceptions import ClientError


def create_vpc():
    try:

        ec2_client = boto3.client('ec2')

        vpc_response = ec2_client.create_vpc(
            CidrBlock='10.0.0.0/16'
        )
        vpc_id = vpc_response['Vpc']['VpcId']

        ec2_client.modify_vpc_attribute(
            EnableDnsSupport={'Value': True},
            VpcId=vpc_id
        )

        ec2_client.modify_vpc_attribute(
            EnableDnsHostnames={'Value': True},
            VpcId=vpc_id
        )

        ec2_client.modify_vpc_attribute(
            EnableNetworkAddressUsageMetrics={'Value': True},
            VpcId=vpc_id
        )

        print("VPC Created")

        internet_gateway_response = ec2_client.create_internet_gateway()
        internet_gateway_id = internet_gateway_response['InternetGateway']['InternetGatewayId']
        ec2_client.attach_internet_gateway(
            VpcId=vpc_id, InternetGatewayId=internet_gateway_id)

        print("Gateway Created")

        subnet_response = ec2_client.create_subnet(
            CidrBlock='10.0.1.0/24',
            VpcId=vpc_id,
            AvailabilityZone='ap-south-1a'
        )

        subnet_id = subnet_response['Subnet']['SubnetId']

        ec2_client.modify_subnet_attribute(
            SubnetId=subnet_id,
            MapPublicIpOnLaunch={'Value': True},
        )

        print("Subnet Created")

        route_table_response = ec2_client.create_route_table(VpcId=vpc_id)
        route_table_id = route_table_response['RouteTable']['RouteTableId']

        ec2_client.associate_route_table(
            RouteTableId=route_table_id, SubnetId=subnet_id)

        ec2_client.create_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock='0.0.0.0/0',
            GatewayId=internet_gateway_id
        )

        print("Route Table Created")

        security_group_response = ec2_client.create_security_group(
            GroupName='my-security-group',
            Description='My security group',
            VpcId=vpc_id
        )
        security_group_id = security_group_response['GroupId']

        print("Security Group Created")

        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )

        print("Ingress added for port 80 and 22")

        return security_group_id, subnet_id
    except ClientError as e:
        print("error occurred while VPC creation : % s" % e)
