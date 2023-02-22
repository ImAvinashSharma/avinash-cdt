# Cloud Deployment Test

### OutPut :

Static website URL ::> [S3 URL](http://avinash-commvault-kexfwlv.s3-website.ap-south-1.amazonaws.com/)

EC2 URL (nginx) ::> [EC2 IP](http://43.205.177.147/)

### let's first understand what is boto3

- boto3 is open-source and actively maintained by Amazon Web Services.

- boto3 is a Python library that provides a simple, yet powerful interface for interacting with Amazon Web Services APIs.

- With boto3, you can write Python code to programmatically interact with various AWS services, such as Amazon S3, Amazon EC2, Amazon RDS, and many others. boto3 can be used to perform various tasks, such as creating, deleting, or modifying AWS resources, fetching metadata about your AWS resources.

## Prerequisites

| tools    | version | command to install           |
| -------- | :-----: | :--------------------------- |
| python   |  3.10   | sudo apt-get install python3 |
| boto3    |  1.26   | pip3 install boto3           |
| aws-cli  |   2.9   | -                            |
| paramiko |  3.0.0  | pip3 install paramiko        |

### configure aws cli

For installing aws cli follow the following article:

[Installation Link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

After downloading aws cli we need to configure the aws configuration. Here are a

```bash
aws configure
```

#### Example :

```
AWS Access Key ID : <access_key>
AWS Secret Access Key : <secret_access_key>
Default region name : <ap-south-1>
Default output format : <json>
```

File directory structure:
There are two folder for is for setting up s3 and ec2.

---

Hear are the digram of the aws s3 and ec2

## s3

S3 (Simple Storage Service) is an object storage service provided by Amazon Web Services (AWS).

```bash
.
├── access.py         // to give public access to bucket
├── assert
│   └── index.html    // hello world
├── create_bucket.py  // bucket creation
├── main.py
└── upload.py         // upload file
```

## Approach

- The idea hear is that we will be creating a s3 bucket and performing a check wethers the bucket already exists or no (any ways we are creating the bucket name dynamically means a alpha numeric stings is generated to make sure the bucket name is unique).

- Then we will make sure that the bucket is accessible publicly (and static hosting is enabled), and print the url of the bucket.

- And then upload the content (index.html) on to the bucket.

### Create bucket (create_bucket.py)

The **create_s3** function we provided bucketName. And here's how it works:

1. The function checks if a bucket with the given bucketName already exists by using boto3 to list all the buckets in the AWS account.

2. If the bucket already exists, the function returns a message indicating that the bucket already exists.

3. If the bucket doesn't exist, the function uses boto3 to create the bucket with the given bucketName. The bucket now is created in the ap-south-1 region.

4. If there is an error during the bucket creation process, such as the specified bucket name being invalid or the AWS account lacking the necessary permissions, the function catches the ClientError exception and prints an error message.

### Making bucket publicly available (access.py)

The **add_bucket_public_access** function we provided bucketName. And here's how it works:

1. The function creates a bucket_policy object that specifies an S3 bucket policy that allows public read access to all objects present in the bucket.

2. The function then uses boto3 to set up a website configuration for the bucket with the _put_bucket_website_ method, which sets the Index and Error pages for the bucket. (Basically we enable static hosting)

3. The function uses boto3 to put the bucket*policy to the specified bucket using the \_put_bucket_policy* method.

4. And finally we print the url of s3 bucket. (Basic hello world)

### Uploading static website to s3 bucket (upload.py)

The **upload_file** function we provided bucketName. And here's how it works:

1. The function takes in a file_name, bucketName, which is the name of the S3 object to be created.

2. The function creates an file object.

3. The function uses the _upload_file_ method of the s3_client object to upload file to the s3 bucket.

4. The ExtraArgs parameter is used for specifying content type of the file being uploaded.

5. If there is an error during the file upload process, such as the specified file not being found or the AWS account lacking the necessary permissions, the function catches the ClientError exception and prints an error message.

### Main (main.py)

1. The string and random modules are imported for generating a random string to append to the bucket name.

2. Then call's the function to create bucket with the given name.

3. Then add public access to the bucket that's created. (for static hosting)

4. Then we, Finally upload the content to the bucket.

![s3](/img/s3.png)

## EC2

Amazon Elastic Compute Cloud (Amazon EC2) is a web service provided by Amazon Web Services (AWS) that provides scalable computing capacity in the cloud. It allows users to create and run virtual machines, known as instances, in the cloud.

```bash
├── create_key.py
├── install.py
├── instance.py
├── main.py
└── vpc.py
```

## Approach

- The idea hear is that we will be creating a vpc with CidrBlock '10.0.0.0/16'.
- Then create a subnet with CidrBlock '10.0.1.0/24' and attache it to the vpc that's created.
- Then we create a enables instances as it allows a VPC to connect to the Internet.
- Then we create a routetable and the need is determine where network traffic is directed.
- Then we create a security group for our instances to control inbound and outbound traffic (virtual firewall).
- Now, The VPC creation is completed. We need to create a ec2 instance that is public facing.
- To do that we need AMI (Amazon Machine Image) of Ubuntu. And then run the instance. Then next step is to connect to instance and install nginx
- To do that we need to install paramiko, to make ssh connections. and when the connection is established we run the command 'sudo apt install nginx -y'.
- Finally, We have a ec2 public facing vm running nginx.

### Creation of VPC (vpc.py)

The **create_vpc** function. And here's how it works:

1. The function uses the _create_vpc()_ function to create a VPC with CIDR block 10.0.0.0/16.

2. Then it creates an internet gateway, attaches it to the VPC, and creates a subnet with CIDR block 10.0.1.0/24 in availability zone ap-south-1a.

3. Then it creates a route table and associates it with the subnet, adds a route to the internet gateway, and creates a security group with name my-security-group.

4. It authorizes inbound traffic to the security group on ports 22 and 80 from all IP addresses.

5. function returns the security group ID and subnet ID.

### Creation of key pair (create_key.py)

The **create_keypair** function we provide key_pair_name. And here's how it works:

1. The _create_keypair()_ function takes a key_pair_name, which specifies the name of the key pair. The function then create the key pair. The private key is then written to a file with the same name as the key pair name and the .pem extension. The file is given read-only permission with chmod() method.

2. If there is an error during creation of key pair,such as the specified key pair is already exists or the AWS account lacking the necessary permissions, the function catches the ClientError exception and prints an error message.

### Creation of ec2 instance (instance.py)

The **create_ec2** function we provide security_group_id, subnet_id, and key_filename. And here's how it works:

1. The function uses the boto3 ec2 client to create the EC2 instance using the _run_instances()_ method. The method takes the AMI ID, the instance type, the number of instances, the security group ID, the subnet ID, and the key pair name.

2. The code then waits for the instance to become available using the _get_waiter()_ method with the 'instance_running' parameter. Once the instance is available, the code uses the describe_instances() method to retrieve the public IP address of the instance.

3. The public IP address is returned by the function. The public ip is used in installation of nginx via paramiko

### Installation of nginx via paramiko (install.py)

The **create_ec2** function we provide public_ip, key_filename. And here's how it works:

1. The function waits for 90 seconds to make sure that the EC2 instance is fully initialized and ready to accept SSH connections.

2. Then initializes ssh with _paramiko.SSHClient()_

3. It establishes an SSH connection to the EC2 instance using paramiko (ssh.connect).

4. It runs the **sudo apt install nginx -y** command on the EC2 instance using the SSH connection (ssh.exec_command).

5. It prints the output of the command to the console.

6. It closes the SSH connection.

![ec2](/img/ec2.png)

## Console outputs

### s3

![s3](/img/s3_output.png)

### EC2

![ec2 1](/img/ec2_output1.png)
![ec2 1](/img/ec2_output2.png)
![ec2 1](/img/ec2_output3.png)
