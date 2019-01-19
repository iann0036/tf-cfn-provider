# Terraform::AWS::DxPublicVirtualInterface

Provides a Direct Connect public virtual interface resource.

## Properties

`AddressFamily` - (Required) The address family for the BGP peer. `ipv4 ` or `ipv6`.

`BgpAsn` - (Required) The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

`ConnectionId` - (Required) The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

`Name` - (Required) The name for the virtual interface.

`Vlan` - (Required) The VLAN ID.

`AmazonAddress` - (Optional) The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

`BgpAuthKey` - (Optional) The authentication key for BGP configuration.

`CustomerAddress` - (Optional) The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

`RouteFilterPrefixes` - (Required) A list of routes to be advertised to the AWS network in this region.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual interface.

`Arn` - The ARN of the virtual interface.

## See Also

* [aws_dx_public_virtual_interface](https://www.terraform.io/docs/providers/aws/r/dx_public_virtual_interface.html) in the _Terraform Provider Documentation_