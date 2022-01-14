import boto3

aws_mag_console = boto3.session.Session()
aws_s3 = aws_mag_console.resource('s3')

for each_s3 in aws_s3.buckets.all():
    print(each_s3.name)