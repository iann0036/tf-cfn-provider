# Terraform::AWS::DxBgpPeer

Provides a Direct Connect BGP peer resource.

## Properties

`AddressFamily` - (Required) The address family for the BGP peer. `ipv4 ` or `ipv6`.

`BgpAsn` - (Required) The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

`VirtualInterfaceId` - (Required) The ID of the Direct Connect virtual interface on which to create the BGP peer.

`AmazonAddress` - (Optional) The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers on public virtual interfaces.

`BgpAuthKey` - (Optional) The authentication key for BGP configuration.

`CustomerAddress` - (Optional) The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers on public virtual interfaces.


## Return Values

### Fn::GetAtt

`Id` - The ID of the BGP peer.

`BgpStatus` - The Up/Down state of the BGP peer.

## See Also

* [aws_dx_bgp_peer](https://www.terraform.io/docs/providers/aws/r/dx_bgp_peer.html) in the _Terraform Provider Documentation_