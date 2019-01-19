# Terraform::AWS::MacieS3BucketAssociation

Associates an S3 resource with Amazon Macie for monitoring and data classification.

~> **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).

## Properties

`BucketName` - (Required) The name of the S3 bucket that you want to associate with Amazon Macie.

`ClassificationType` - (Optional) The configuration of how Amazon Macie classifies the S3 objects.

`MemberAccountId` - (Optional) The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `MemberAccountId` isn't specified, the action associates specified S3 resources with Macie for the current master account.

`Prefix` - (Optional) Object key prefix identifying one or more S3 objects to which the association applies.

### ClassificationType Properties

`Continuous` - (Optional) A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket. The only valid value is the default value, `FULL`.

`OneTime` - (Optional) A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket. Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the association.

## See Also

* [aws_macie_s3_bucket_association](https://www.terraform.io/docs/providers/aws/r/macie_s3_bucket_association.html) in the _Terraform Provider Documentation_