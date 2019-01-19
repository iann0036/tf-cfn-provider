# Terraform::AWS::DxHostedPrivateVirtualInterface

Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the virtual interface.

`Arn` - The ARN of the virtual interface.

`JumboFrameCapable` - Indicates whether jumbo frames (9001 MTU) are supported.

## See Also

* [aws_dx_hosted_private_virtual_interface](https://www.terraform.io/docs/providers/aws/r/dx_hosted_private_virtual_interface.html) in the _Terraform Provider Documentation_