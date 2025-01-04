import pulumi_aws as aws

from variable import project_name


bucket = aws.s3.Bucket(
    'bigbro-s3',
    bucket='bigbro-s3',
    acl=aws.s3.CannedAcl.PUBLIC_READ,
    tags={
        'Name': 'bigbro-ec2',
        'Project': project_name
    }
)