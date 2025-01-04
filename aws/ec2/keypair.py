import pulumi_aws as aws

from variable import bigbro_public_key


keypair = aws.ec2.KeyPair(
    'bigbro-keypair',
    key_name='bigbro-keypair',
    public_key=bigbro_public_key,
)