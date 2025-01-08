from .vpc import vpc, internet_gateway
from .subnets import (
    public_subnet_1,
    public_subnet_2,
    private_subnet_1,
    private_subnet_2
)
from .routes import (
    public_route_table,
    private_route_table,
    public_route_table_association_1,
    public_route_table_association_2,
    private_route_table_association_1,
    private_route_table_association_2
)


vpc_resource = {
    'vpc': vpc,
    'internet_gateway': internet_gateway,
    'subnets': {
        'public_1': public_subnet_1,
        'public_2': public_subnet_2,
        'private_1': private_subnet_1,
        'private_2': private_subnet_2
    },
    'routes': {
        'public_table': public_route_table,
        'private_table': private_route_table,
        'association': {
            'public_1': public_route_table_association_1,
            'public_2': public_route_table_association_2,
            'private_1': private_route_table_association_1,
            'private_2': private_route_table_association_2
        }
    }
}