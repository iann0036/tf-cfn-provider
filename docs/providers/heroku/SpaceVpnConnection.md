# Terraform::Heroku::SpaceVpnConnection

Provides a resource for creating a VPN connection between a network and a Heroku Private Space. For more information, see [Private Spaces VPN Connection](https://devcenter.heroku.com/articles/private-space-vpn-connection?preview=1) in the Heroku DevCenter.

## Properties

`Name` - (Required) The name of the VPN connection.

`Space` - (Required) The name of the Heroku Private Space where the VPN connection will be established.

`PublicIp` - (Required) The public IP address of the VPN endpoint on the network where the VPN connection will be established.

`RoutableCidrs` - (Required) A list of IPv4 CIDR blocks used by the network where the VPN connection will be established.


## Return Values

### Fn::GetAtt

`SpaceCidrBlock` - The CIDR block for the Heroku Private Space. The network where the VPN will be established should be configured to route traffic destined for this CIDR block over the VPN link.

`IkeVersion` - The IKE version used to setup the IPsec tunnel.

`Tunnels` - Details about each VPN tunnel endpoint.

`Ip` - The public IP address of the tunnel.

`PreSharedKey` - The pre-shared IPSec secret for the tunnel.

## See Also

* [heroku_space_vpn_connection](https://www.terraform.io/docs/providers/heroku/r/space_vpn_connection.html) in the _Terraform Provider Documentation_