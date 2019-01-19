# Terraform::AWS::S3AccountPublicAccessBlock

Manages S3 account-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).

~> **NOTE:** Each AWS account may only have one S3 Public Access Block configuration. Multiple configurations of the resource against the same AWS account will cause a perpetual difference.

-> Advanced usage: To use a custom API endpoint for this Terraform resource, use the [`s3control` endpoint provider configuration](/docs/providers/aws/index.html#s3control), not the `s3` endpoint provider configuration.

## Properties

`AccountId` - (Optional) AWS account ID to configure. Defaults to automatically determined account ID of the Terraform AWS provider.

`BlockPublicAcls` - (Optional) Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior: * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access. * PUT Object calls will fail if the request includes an object ACL.

`BlockPublicPolicy` - (Optional) Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to: * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.

`IgnorePublicAcls` - (Optional) Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to: * Ignore all public ACLs on buckets in this account and any objects that they contain.

`RestrictPublicBuckets` - (Optional) Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`: * Only the bucket owner and AWS Services can access buckets with public policies.


## See Also

* [aws_s3_account_public_access_block](https://www.terraform.io/docs/providers/aws/r/s3_account_public_access_block.html) in the _Terraform Provider Documentation_