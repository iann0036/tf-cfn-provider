# Terraform::AWS::DxPrivateVirtualInterface

Provides a Direct Connect private virtual interface resource.

## Properties

`AddressFamily` - (Required) The address family for the BGP peer. `ipv4 ` or `ipv6`.

`BgpAsn` - (Required) The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

`ConnectionId` - (Required) The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

`Name` - (Required) The name for the virtual interface.

`Vlan` - (Required) The VLAN ID.

`AmazonAddress` - (Optional) The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

`Mtu` - (Optional) The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.

`BgpAuthKey` - (Optional) The authentication key for BGP configuration.

`CustomerAddress` - (Optional) The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

`DxGatewayId` - (Optional) The ID of the Direct Connect gateway to which to connect the virtual interface.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`VpnGatewayId` - (Optional) The ID of the [virtual private gateway](vpn_gateway.html) to which to connect the virtual interface.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual interface.

`Arn` - The ARN of the virtual interface.

`JumboFrameCapable` - Indicates whether jumbo frames (9001 MTU) are supported.

## See Also

* [aws_dx_private_virtual_interface](https://www.terraform.io/docs/providers/aws/r/dx_private_virtual_interface.html) in the _Terraform Provider Documentation_