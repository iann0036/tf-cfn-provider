# Terraform::AWS::KmsAlias

Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases & keys,
but API (hence Terraform too) allows you to create as many aliases as
the [account limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) allow you.

## Properties

`Name` - (Optional) The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/).

`NamePrefix` - (Optional) Creates an unique alias beginning with the specified prefix.
The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `Name`.

`TargetKeyId` - (Required) Identifier for the key for which the alias is for, can be either an ARN or key_id.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) of the key alias.

`TargetKeyArn` - The Amazon Resource Name (ARN) of the target key identifier.

## See Also

* [aws_kms_alias](https://www.terraform.io/docs/providers/aws/r/kms_alias.html) in the _Terraform Provider Documentation_