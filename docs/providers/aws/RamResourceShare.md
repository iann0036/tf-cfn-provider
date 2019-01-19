# Terraform::AWS::RamResourceShare

Provides a Resource Access Manager (RAM) resource share.

## Properties

`Name` - (Required) The name of the resource share.

`AllowExternalPrincipals` - (Optional) Indicates whether principals outside your organization can be associated with a resource share.

`Tags` - (Optional) A mapping of tags to assign to the resource share.


## Return Values

### Fn::GetAtt

`Id` - The Amazon Resource Name (ARN) of the resource share.

## See Also

* [aws_ram_resource_share](https://www.terraform.io/docs/providers/aws/r/ram_resource_share.html) in the _Terraform Provider Documentation_