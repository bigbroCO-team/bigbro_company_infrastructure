import pulumi_aws as aws

from aws.ec2 import ec2
from aws.vpc import public_subnet_1, public_subnet_2, vpc
from variable import project_name, ssl_certificate_arn


alb = aws.lb.LoadBalancer(
    'bigbro-alb',
    internal=False,
    load_balancer_type='application',
    subnets=[public_subnet_1, public_subnet_2],
    enable_deletion_protection=True,
    tags={
        'Name': 'bigbro-elb',
        'Project': project_name
    }
)

alb_target_group = aws.lb.TargetGroup(
    'alb-target-group',
    name='alb-target-group',
    vpc_id=vpc.id,
    port=80,
    protocol='HTTP'
)

alb_target_group_attachment = aws.lb.TargetGroupAttachment(
    'alb-target-group-attachment',
    target_group_arn=alb_target_group.arn,
    target_id=ec2.id,
    port=80
)

alb_listener_https = aws.lb.Listener(
    'alb-listener-https',
    load_balancer_arn=alb.arn,
    port=443,
    protocol='HTTPS',
    certificate_arn=ssl_certificate_arn,
    default_actions=[{
        'type': 'forward',
        'target_group_arn': alb_target_group.arn
    }]
)

alb_listener_http = aws.lb.Listener(
    'alb-listener-http',
    load_balancer_arn=alb.arn,
    port=80,
    protocol='HTTP',
    default_actions=[{
        'type': 'redirect',
        'redirect': {
            'port': '443',
            'protocol': 'HTTPS',
            'status_code': 'HTTP_301'
        }
    }]
)