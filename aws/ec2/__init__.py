from .ec2 import ec2
from .keypair import keypair
from .securitgroup import security_group
from .elb import elb


ec2_resource = {
    'ec2': ec2,
    'keypair': keypair,
    'security_group': security_group,
    'elb': elb
}