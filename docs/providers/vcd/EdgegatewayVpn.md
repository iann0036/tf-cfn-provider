# Terraform::VCD::EdgegatewayVpn

Provides a vCloud Director IPsec VPN. This can be used to create,
modify, and delete VPN settings and rules.

## Properties

`EdgeGateway` - (Required) The name of the edge gateway on which to apply the Firewall Rules.

`Name` - (Required) The name of the VPN.

`Description` - (Required) A description for the VPN.

`EncryptionProtocol` - (Required) - E.g. `AES256`.

`LocalIpAddress` - (Required) - Local IP Address.

`LocalId` - (Required) - Local ID.

`Mtu` - (Required) - The MTU setting.

`PeerIpAddress` - (Required) - Peer IP Address.

`PeerId` - (Required) - Peer ID.

`SharedSecret` - (Required) - Shared Secret.

`LocalSubnets` - (Required) - List of Local Subnets see [Local Subnets](#localsubnets) below for details.

`PeerSubnets` - (Required) - List of Peer Subnets see [Peer Subnets](#peersubnets) below for details.


## See Also

* [vcd_edgegateway_vpn](https://www.terraform.io/docs/providers/vcd/r/edgegateway_vpn.html) in the _Terraform Provider Documentation_