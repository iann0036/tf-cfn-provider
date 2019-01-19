# Terraform::AWS::DxHostedPublicVirtualInterfaceAccepter

Provides a resource to manage the accepter's side of a Direct Connect hosted public virtual interface.
This resource accepts ownership of a public virtual interface created by another AWS account.

## Properties

`VirtualInterfaceId` - (Required) The ID of the Direct Connect virtual interface to accept.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual interface.

`Arn` - The ARN of the virtual interface.

## See Also

* [aws_dx_hosted_public_virtual_interface_accepter](https://www.terraform.io/docs/providers/aws/r/dx_hosted_public_virtual_interface_accepter.html) in the _Terraform Provider Documentation_