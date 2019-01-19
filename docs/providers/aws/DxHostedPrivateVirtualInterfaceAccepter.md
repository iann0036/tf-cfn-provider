# Terraform::AWS::DxHostedPrivateVirtualInterfaceAccepter

Provides a resource to manage the accepter's side of a Direct Connect hosted private virtual interface.
This resource accepts ownership of a private virtual interface created by another AWS account.

## Properties

`VirtualInterfaceId` - (Required) The ID of the Direct Connect virtual interface to accept.

`DxGatewayId` - (Optional) The ID of the Direct Connect gateway to which to connect the virtual interface.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`VpnGatewayId` - (Optional) The ID of the [virtual private gateway](vpn_gateway.html) to which to connect the virtual interface.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual interface.

`Arn` - The ARN of the virtual interface.

## See Also

* [aws_dx_hosted_private_virtual_interface_accepter](https://www.terraform.io/docs/providers/aws/r/dx_hosted_private_virtual_interface_accepter.html) in the _Terraform Provider Documentation_