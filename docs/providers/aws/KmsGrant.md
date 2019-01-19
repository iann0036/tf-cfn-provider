# Terraform::AWS::KmsGrant

Provides a resource-based access control mechanism for a KMS customer master key.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`GrantId` - The unique identifier for the grant.

`GrantToken` - The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).

## See Also

* [aws_kms_grant](https://www.terraform.io/docs/providers/aws/r/kms_grant.html) in the _Terraform Provider Documentation_