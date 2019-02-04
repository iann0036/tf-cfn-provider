# Terraform::AWS::S3BucketPublicAccessBlock

Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).

## Properties

`Bucket` - (Required) S3 Bucket to which this Public Access Block configuration should be applied.

`BlockPublicAcls` - (Optional) Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:.

`BlockPublicPolicy` - (Optional) Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:.

`IgnorePublicAcls` - (Optional) Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:.

`RestrictPublicBuckets` - (Optional) Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:.


## See Also

* [aws_s3_bucket_public_access_block](https://www.terraform.io/docs/providers/aws/r/s3_bucket_public_access_block.html) in the _Terraform Provider Documentation_