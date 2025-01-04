import pulumi_aws as aws

from aws.ec2.keypair import keypair
from aws.ec2.securitgroup import security_group
from aws.vpc.subnets import public_subnet_1
from variable import project_name, ubuntu24_ami


ec2 = aws.ec2.Instance(
    'bigbro-ec2',
    ami=ubuntu24_ami,
    instance_type=aws.ec2.InstanceType.T2_MICRO,
    key_name=keypair.key_name,
    subnet_id=public_subnet_1.id,
    vpc_security_group_ids=[security_group.id],
    associate_public_ip_address=True,
    tags={
        'Name': 'bigbro-ec2',
        'Project': project_name
    }
)