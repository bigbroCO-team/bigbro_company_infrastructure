import pulumi_aws as aws

from variable import bigbro_pub_keypair


keypair = aws.ec2.KeyPair(
    'bigbro-keypair',
    key_name='bigbro-keypair',
    public_key=bigbro_pub_keypair,
)