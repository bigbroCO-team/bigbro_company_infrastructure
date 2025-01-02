import pulumi_aws as aws

from variable import (
    project_name, 
    availability_zones, 
    subnet_cidrs
)
from aws.vpc.vpc import vpc


public_subnet_1 = aws.ec2.Subnet(
    'public-subnet-1',
    vpc_id=vpc.id,
    cidr_block=subnet_cidrs['public1'],
    availability_zone=availability_zones['a'],
    tags={
        'Name': 'public-subnet-1',
        'Project': project_name
    }
)

public_private_1 = aws.ec2.Subnet(
    'private-subnet-1',
    vpc_id=vpc.id,
    cidr_block=subnet_cidrs['private1'],
    availability_zone=availability_zones['a'],
    tags={
        'Name': 'private-subnet-1',
        'Project': project_name
    }
)

public_subnet_2 = aws.ec2.Subnet(
    'public-subnet-2',
    vpc_id=vpc.id,
    cidr_block=subnet_cidrs['public2'],
    availability_zone=availability_zones['b'],
    tags={
        'Name': 'public-subnet-2',
        'Project': project_name
    }
)

public_private_2 = aws.ec2.Subnet(
    'private-subnet-2',
    vpc_id=vpc.id,
    cidr_block=subnet_cidrs['private2'],
    availability_zone=availability_zones['b'],
    tags={
        'Name': 'private-subnet-2',
        'Project': project_name
    }
)