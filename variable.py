import os

project_name = 'bigbro'

aws_region = 'ap-northeast-2'
availability_zones = {
    'a': f'{aws_region}a',
    'b': f'{aws_region}b'
}

vpc_cidr = '10.0.0.0/16'
subnet_cidrs = {
    'public1': '10.0.1.0/24',
    'private1': '10.0.2.0/24',
    'public2': '10.0.3.0/24',
    'private2': '10.0.4.0/24'
}

ubuntu24_ami = 'ami-0dc44556af6f78a7b'

bigbro_public_key = os.environ.get('BIGBRO_PUBLIC_KEY')

ssl_certificate_arn = os.environ.get('SSL_CERTIFICATE_ARN')