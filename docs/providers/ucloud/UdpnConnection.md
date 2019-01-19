# Terraform::UCloud::UdpnConnection

UDPN (UCloud Dedicated Private Network)，you can use Dedicated Private Network to achieve high-speed, stable, secure, and dedicated communications between different data centers. The most frequent scenario is to create network connection of clusters across regions.

~> **VPC Peering Connections with UDPN Connection** The cross-region Dedicated Private Network must be established if the two VPCs located in different regions are expected to be connected.

~> **Note** The addtional packet head will be added and included in the overall length of packet due to the tunneling UDPN adopted. Since the number of the bytes of packet head is fixed, the bigger data packet is, the less usage will be taken for the packet head.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation for UDPN connection, formatted by RFC3339 time string.

`ExpireTime` - The expiration time for UDPN connection, formatted by RFC3339 time string.

## See Also

* [ucloud_udpn_connection](https://www.terraform.io/docs/providers/ucloud/r/udpn_connection.html) in the _Terraform Provider Documentation_