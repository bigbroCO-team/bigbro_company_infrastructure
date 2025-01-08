from .s3 import bucket
from .acl import (
    public_access_block,
    ownership_controls,
    bucket_acl
)

s3_resource = {
    's3': bucket,
    'acl': {
        'public_access_block': public_access_block,
        'ownership_controls': ownership_controls,
        'bucket_acl': bucket_acl,
    }
}