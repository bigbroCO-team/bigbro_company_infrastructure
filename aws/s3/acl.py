import pulumi
import pulumi_aws as aws

from aws.s3.s3 import bucket


public_access_block = aws.s3.BucketPublicAccessBlock(
    's3-public-access-block',
    bucket=bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False
)

ownership_controls = aws.s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule={
        'object_ownership': 'BucketOwnerPreferred'
    }
)

bucket_acl = aws.s3.BucketAclV2(
    's3-acl',
    bucket=bucket.id,
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[
        ownership_controls,
        public_access_block,
    ])
)