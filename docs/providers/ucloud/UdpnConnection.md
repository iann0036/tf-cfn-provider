# Terraform::UCloud::UdpnConnection

UDPN (UCloud Dedicated Private Network)，you can use Dedicated Private Network to achieve high-speed, stable, secure, and dedicated communications between different data centers. The most frequent scenario is to create network connection of clusters across regions.

~> **VPC Peering Connections with UDPN Connection** The cross-region Dedicated Private Network must be established if the two VPCs located in different regions are expected to be connected.

~> **Note** The addtional packet head will be added and included in the overall length of packet due to the tunneling UDPN adopted. Since the number of the bytes of packet head is fixed, the bigger data packet is, the less usage will be taken for the packet head.

## Properties

`Bandwidth` - (Optional) Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). range from 2 - 1000M. The default value is "1".

`Duration` - (Optional) The duration that you will buy the resource, the default value is "1". It is not required when "dynamic" (pay by hour), the value is "0" when pay by month and the instance will be vaild till the last day of that month.

`ChargeType` - (Optional) Charge type. Possible values are: "year" as pay by year, "month" as pay by month, "dynamic" as pay by hour. The default value is "month".

`PeerRegion` - (Optional) The correspondent region of dedicated connection, please refer to the region and [availability zone list](https://docs.ucloud.cn/api/summary/regionlist) and [UDPN price list](https://docs.ucloud.cn/network/udpn/udpn_price).


## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation for UDPN connection, formatted by RFC3339 time string.

`ExpireTime` - The expiration time for UDPN connection, formatted by RFC3339 time string.

## See Also

* [ucloud_udpn_connection](https://www.terraform.io/docs/providers/ucloud/r/udpn_connection.html) in the _Terraform Provider Documentation_