# Terraform::Heroku::SpaceVpnConnection

Provides a resource for creating a VPN connection between a network and a Heroku Private Space. For more information, see [Private Spaces VPN Connection](https://devcenter.heroku.com/articles/private-space-vpn-connection?preview=1) in the Heroku DevCenter.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SpaceCidrBlock` - The CIDR block for the Heroku Private Space. The network where the VPN will be established should be configured to route traffic destined for this CIDR block over the VPN link.

`IkeVersion` - The IKE version used to setup the IPsec tunnel.

`Tunnels` - Details about each VPN tunnel endpoint.

`Ip` - The public IP address of the tunnel.

`PreSharedKey` - The pre-shared IPSec secret for the tunnel.

## See Also

* [heroku_space_vpn_connection](https://www.terraform.io/docs/providers/heroku/r/space_vpn_connection.html) in the _Terraform Provider Documentation_