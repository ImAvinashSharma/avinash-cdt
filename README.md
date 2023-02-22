# Cloud Deployment Test

### let's first understand what is boto3

- boto3 is open-source and actively maintained by Amazon Web Services.

- boto3 is a Python library that provides a simple, yet powerful interface for interacting with Amazon Web Services APIs. It is one of the most popular libraries for working with AWS services apart from terraform and ansible.

- With boto3, you can write Python code to programmatically interact with various AWS services, such as Amazon S3, Amazon EC2, Amazon RDS, and many others. boto3 can be used to perform various tasks, such as creating, deleting, or modifying AWS resources, fetching metadata about your AWS resources, and working with data stored in AWS.

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

[s3 url]()
[ec2 ip]()

Hear are the digram of the aws s3 and ec2

## s3

S3 (Simple Storage Service) is an object storage service provided by Amazon Web Services (AWS).

```bash
.
├── access.py
├── assert
│   └── index.html
├── create_bucket.py
├── main.py
└── upload.py
```

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

![ec2](/img/ec2.png)
