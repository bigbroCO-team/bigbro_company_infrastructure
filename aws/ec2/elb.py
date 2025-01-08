import pulumi_aws as aws

from variable import availability_zones, project_name, ssl_certificate_arn
from aws.ec2.ec2 import ec2


elb = aws.elb.LoadBalancer(
    'bigbro-elb',
    availability_zones=[
        availability_zones['a'],
        availability_zones['b'],
    ],
    listeners=[
        {
            'instance_port': 80,
            'instance_protocol': 'http',
            'lb_port': 80,
            'lb_protocol': 'http',
        },
        {
            'instance_port': 80,
            'instance_protocol': 'http',
            'lb_port':443,
            'lb_protocol': 'https',
            'ssl_certificate_id': ssl_certificate_arn
        }
    ],
    health_check={
        "healthy_threshold": 2,
        "unhealthy_threshold": 2,
        "timeout": 3,
        "target": "HTTP:80/health-check",
        "interval": 30,
    },
    instances=[ec2],
    cross_zone_load_balancing=True,
    idle_timeout=400,
    tags={
        'Name': 'bigbro-elb',
        'Project': project_name
    }
)