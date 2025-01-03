import pulumi_aws as aws

ubuntu = aws.ec2.get_ami(
    most_recent=True,
    filters=[
        {
            'name': 'name',
            'values': ['Ubuntu Server', '24.04', 'LTS']
        },
        {
            "name": "virtualization-type",
            "values": ["hvm"],
        },
    ]
)