import boto3
from botocore.client import ClientError

# aws_s3_client = boto3.client('s3',
#           aws_access_key_id = 'AKIAZUMYRWBEIM6WWQNL',
#           aws_secret_access_key = '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')
aws_s3_client = boto3.client('s3')        
bucketName = 'bucketvivek0721'
# location = {'LocationConstraint': 'ap-south-1'}
filePath = '/Users/blackhat/Documents/hello.txt'
try:
    aws_s3_client.head_bucket(Bucket=bucketName)
    bucket_exist = 'Yes'
except ClientError:
    bucket_exist = 'No'
    print("The bucket does not exist or you have no access.")
    
if bucket_exist == 'No':
    try:
        location = {'LocationConstraint': 'ap-south-1'}
        aws_s3_client.create_bucket(Bucket=bucketName,
                                    CreateBucketConfiguration=location)
        print(f"\n{bucketName} bucket has been created on AWS S3")
    except ClientError as e:
        print(e)
        print(f"{bucketName} cannot be created on s3")
    except:
        print(f"{bucketName} cannot be created on s3")



# Upload a new file
# filePath = '/Users/blackhat/Documents/hello.txt'
filename = 'hello.txt'
# aws_s3_client.meta.client.upload_file(filePath,bucket_name,filename)
aws_s3_client.upload_file(filePath, bucketName, filename)

