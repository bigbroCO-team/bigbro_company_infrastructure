import pulumi_aws as aws

from aws.vpc.vpc import vpc, internet_gateway
from aws.vpc.subnets import (
    public_subnet_1,
    public_private_1,
    public_subnet_2,
    public_private_2
)
from aws.vpc.routes import (
    public_route_table,
    private_route_table,
    public_route_table_association_1,
    public_route_table_association_2,
    private_route_table_association_1,
    private_route_table_association_2
)

from aws.ec2.ec2 import ec2
from aws.ec2.keypair import keypair
from aws.ec2.security_group import security_group