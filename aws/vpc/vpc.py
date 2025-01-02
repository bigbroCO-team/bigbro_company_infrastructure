import pulumi_aws as aws

from variable import project_name, vpc_cidr


vpc = aws.ec2.Vpc(
    'bigbro-vpc',
    cidr_block=vpc_cidr,
    tags={
        'Name': 'bigbro-vpc',
        'Project': project_name
    }
)

internet_gateway = aws.ec2.InternetGateway(
    'internet-gateway',
    vpc_id=vpc.id,
    tags={
        'Name': 'internet-gateway',
        'Project': project_name
    }
)

