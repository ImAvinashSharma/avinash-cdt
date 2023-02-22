# Cloud Deployment Test

### let's first understand what is boto3

- boto3 is open-source and actively maintained by Amazon Web Services.

- boto3 is a Python library that provides a simple, yet powerful interface for interacting with Amazon Web Services APIs. It is one of the most popular libraries for working with AWS services apart from terraform and ansible.

- With boto3, you can write Python code to programmatically interact with various AWS services, such as Amazon S3, Amazon EC2, Amazon RDS, and many others.boto3 can be used to perform various tasks, such as creating, deleting, or modifying AWS resources, fetching metadata about your AWS resources, and working with data stored in AWS.

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

```sh
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

![s3](/img/s3.png)
![ec2](/img/ec2.png)
