# Terraform::AWS::DxHostedPublicVirtualInterface

Provides a Direct Connect hosted public virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.

## Properties

`AddressFamily` - (Required) The address family for the BGP peer. `ipv4 ` or `ipv6`.

`BgpAsn` - (Required) The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

`ConnectionId` - (Required) The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

`Name` - (Required) The name for the virtual interface.

`OwnerAccountId` - (Required) The AWS account that will own the new virtual interface.

`RouteFilterPrefixes` - (Required) A list of routes to be advertised to the AWS network in this region.

`Vlan` - (Required) The VLAN ID.

`AmazonAddress` - (Optional) The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

`BgpAuthKey` - (Optional) The authentication key for BGP configuration.

`CustomerAddress` - (Optional) The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual interface.

`Arn` - The ARN of the virtual interface.

## See Also

* [aws_dx_hosted_public_virtual_interface](https://www.terraform.io/docs/providers/aws/r/dx_hosted_public_virtual_interface.html) in the _Terraform Provider Documentation_