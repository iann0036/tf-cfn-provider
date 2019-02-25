# Terraform::AWS::RamPrincipalAssociation

Provides a Resource Access Manager (RAM) principal association.

~> *NOTE:* For an AWS Account ID principal, the target account must accept the RAM association invitation after resource creation.

## Properties

`Principal` - (Required) The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ID, or an AWS Organizations Organization Unit ID.

`ResourceShareArn` - (Required) The Amazon Resource Name (ARN) of the resource share.


## Return Values

### Fn::GetAtt

`Id` - The Amazon Resource Name (ARN) of the Resource Share and the principal, separated by a comma.

## See Also

* [aws_ram_principal_association](https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html) in the _Terraform Provider Documentation_