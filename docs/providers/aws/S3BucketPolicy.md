# Terraform::AWS::S3BucketPolicy

Attaches a policy to an S3 bucket resource.

## Properties

`Bucket` - (Required) The name of the bucket to which to apply the policy.

`Policy` - (Required) The text of the policy. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).


## See Also

* [aws_s3_bucket_policy](https://www.terraform.io/docs/providers/aws/r/s3_bucket_policy.html) in the _Terraform Provider Documentation_