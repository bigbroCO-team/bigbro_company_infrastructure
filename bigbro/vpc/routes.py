import pulumi_aws as aws

from variable import project_name
from vpc.vpc import vpc, internet_gateway
from vpc.subnets import (
    public_subnet_1,
    public_private_1,
    public_subnet_2,
    public_private_2
)


public_route_table = aws.ec2.RouteTable(
    'public-route-table',
    vpc_id=vpc.id,
    routes=[
        {
            'cidr_block': '0.0.0.0/0',
            'gateway_id': internet_gateway.id
        }
    ],
    tags={
        'Name': 'public-route-table',
        'Project': project_name
    }
)

private_route_table = aws.ec2.RouteTable(
    'private-route-table',
    vpc_id=vpc.id,
    tags={
        'Name': 'private-route-table',
        'Project': project_name
    }
)


public_route_table_association_1 = aws.ec2.RouteTableAssociation(
    'public-route-table-association-1',
    subnet_id=public_subnet_1.id,
    route_table_id=public_route_table.id
)

private_route_table_association_1 = aws.ec2.RouteTableAssociation(
    'private-route-table-association-1',
    subnet_id=public_private_1.id,
    route_table_id=private_route_table.id
)

public_route_table_association_2 = aws.ec2.RouteTableAssociation(
    'public-route-table-association-2',
    subnet_id=public_subnet_2.id,
    route_table_id=public_route_table.id
)

private_route_table_association_2 = aws.ec2.RouteTableAssociation(
    'private-route-table-association-2',
    subnet_id=public_private_2.id,
    route_table_id=private_route_table.id
)

