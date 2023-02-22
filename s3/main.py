import string
import random
from create_bucket import create_s3
from upload import upload_file
from access import add_bucket_public_access

if __name__ == '__main__':
    bucketName = "avinash-commvault-" + \
        ''.join(random.choices(string.ascii_lowercase, k=7))
    print(create_s3(bucketName))
    add_bucket_public_access(bucketName)
    print("Uploading")
    upload_file("./assert/index.html", bucketName)
    print("Uploading completed")
