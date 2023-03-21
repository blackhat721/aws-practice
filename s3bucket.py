import boto3
s3 = boto3.client('s3')
bucketName = 'bucketvivek0721'
location = {'LocationConstraint': 'ap-south-1'}
filePath = '/Users/blackhat/Documents/hello.txt'
res = s3.create_bucket(
    ACL='private',
    Bucket = bucketName,CreateBucketConfiguration=location
)
print(res)
s3.meta.client.upload_file(filePath,bucketName, 'hello.txt')