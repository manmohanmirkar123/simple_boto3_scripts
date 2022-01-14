#This Boto3 script will list down all the IAM users
import boto3

aws_mag_console = boto3.session.Session()
aws_iam = aws_mag_console.resource('iam')
for each_user in aws_iam.users.all():
    print(each_user.name)