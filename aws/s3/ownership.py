import pulumi_aws as aws

from aws.s3.s3 import bucket


ownership_controls = aws.s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule=aws.s3.BucketOwnershipControlsRuleArgs(
        object_ownership='ObjectWriter'
    )
)