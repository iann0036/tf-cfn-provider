# Terraform::AWS::KmsAlias

Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases & keys,
but API (hence Terraform too) allows you to create as many aliases as
the [account limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) allow you.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) of the key alias.

`TargetKeyArn` - The Amazon Resource Name (ARN) of the target key identifier.

## See Also

* [aws_kms_alias](https://www.terraform.io/docs/providers/aws/r/kms_alias.html) in the _Terraform Provider Documentation_