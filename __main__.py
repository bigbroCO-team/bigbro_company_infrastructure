from aws.vpc import vpc_resource
from aws.ec2 import ec2_resource
from aws.s3 import s3_resource


aws = {
    'vpc': vpc_resource,
    'ec2': ec2_resource,
    's3': s3_resource
}