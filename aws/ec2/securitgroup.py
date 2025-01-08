import pulumi_aws as aws

from aws.vpc.vpc import vpc
from variable import project_name


security_group = aws.ec2.SecurityGroup(
    'bigbro-sg',
    vpc_id=vpc.id,
    ingress=[
        {
            'protocol': 'tcp',
            'from_port': 22,
            'to_port': 22,
            'cidr_blocks': ['0.0.0.0/0'],
        },
        {
            'protocol': 'tcp',
            'from_port': 80,
            'to_port': 80,
            'cidr_blocks': ['0.0.0.0/0'],
        },
        {
            'protocol': 'tcp',
            'from_port': 443,
            'to_port': 443,
            'cidr_blocks': ['0.0.0.0/0'],
        }
    ],
    egress=[
        {
            'protocol': '-1',
            'from_port': 0,
            'to_port': 0,
            'cidr_blocks': ['0.0.0.0/0'],
        }
    ],
    tags={
        'Name': 'bigbro-sg',
        'Project': project_name
    }
) 