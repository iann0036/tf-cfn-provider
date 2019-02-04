# Terraform::AWS::KmsKey

Provides a KMS customer master key.

## Properties

`Description` - (Optional) The description of the key as viewed in AWS console.

`KeyUsage` - (Optional) Specifies the intended use of the key.
Defaults to ENCRYPT_DECRYPT, and only symmetric encryption and decryption are supported.

`Policy` - (Optional) A valid policy JSON document. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`DeletionWindowInDays` - (Optional) Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.

`IsEnabled` - (Optional) Specifies whether the key is enabled. Defaults to true.

`EnableKeyRotation` - (Optional) Specifies whether [key rotation](http://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
is enabled. Defaults to false.

`Tags` - (Optional) A mapping of tags to assign to the object.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) of the key.

`KeyId` - The globally unique identifier for the key.

## See Also

* [aws_kms_key](https://www.terraform.io/docs/providers/aws/r/kms_key.html) in the _Terraform Provider Documentation_