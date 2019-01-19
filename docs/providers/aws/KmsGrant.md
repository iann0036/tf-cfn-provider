# Terraform::AWS::KmsGrant

Provides a resource-based access control mechanism for a KMS customer master key.

## Properties

`Name` - (Optional, Forces new resources) A friendly name for identifying the grant.

`KeyId` - (Required, Forces new resources) The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

`GranteePrincipal` - (Required, Forces new resources) The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

`Operations` - (Required, Forces new resources) A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`.

`RetireePrincipal` - (Optional, Forces new resources) The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, terraform's state may not always be refreshed to reflect what is true in AWS.

`Constraints` - (Optional, Forces new resources) A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).

`GrantCreationTokens` - (Optional, Forces new resources) A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.

### Constraints Properties

`EncryptionContextEquals` - (Optional) A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. Conflicts with `EncryptionContextSubset`.

`EncryptionContextSubset` - (Optional) A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. Conflicts with `EncryptionContextEquals`.


## Return Values

### Fn::GetAtt

`GrantId` - The unique identifier for the grant.

`GrantToken` - The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).

## See Also

* [aws_kms_grant](https://www.terraform.io/docs/providers/aws/r/kms_grant.html) in the _Terraform Provider Documentation_