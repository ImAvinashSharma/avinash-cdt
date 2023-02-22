import boto3

ec2_client = boto3.client('ec2')

vpc_response = ec2_client.create_vpc(
    CidrBlock='10.0.0.0/16'
)
vpc_id = vpc_response['Vpc']['VpcId']


ec2_client.modify_vpc_attribute(
    EnableDnsSupport={'Value': True},
    VpcId=vpc_id,
)

ec2_client.modify_vpc_attribute(
    EnableDnsHostnames={'Value': True},
    VpcId=vpc_id,
)

ec2_client.modify_vpc_attribute(
    EnableNetworkAddressUsageMetrics={'Value': True},
    VpcId=vpc_id,
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

print("Ingress added")

# if wanted to create a new key_pair un comment this code
# response = ec2_client.create_key_pair(KeyName='c-cdt-key')

instance = ec2_client.run_instances(
    ImageId='ami-0caf778a172362f1c',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[security_group_id],
    SubnetId=subnet_id,
    KeyName='c-cdt-key',
    # NetworkInterfaces=[{'AssociatePublicIpAddress': True}]
)

print(instance)
