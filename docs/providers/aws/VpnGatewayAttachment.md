# Terraform::AWS::VpnGatewayAttachment

Provides a Virtual Private Gateway attachment resource, allowing for an existing
hardware VPN gateway to be attached and/or detached from a VPC.

-> **Note:** The [`aws_vpn_gateway`](vpn_gateway.html)
resource can also automatically attach the Virtual Private Gateway it creates
to an existing VPC by setting the [`vpc_id`](vpn_gateway.html#vpc_id) attribute accordingly.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`VpcId` - The ID of the VPC that Virtual Private Gateway is attached to.

`VpnGatewayId` - The ID of the Virtual Private Gateway.

## See Also

* [aws_vpn_gateway_attachment](https://www.terraform.io/docs/providers/aws/r/vpn_gateway_attachment.html) in the _Terraform Provider Documentation_