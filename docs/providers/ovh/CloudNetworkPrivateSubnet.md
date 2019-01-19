# Terraform::OVH::CloudNetworkPrivateSubnet

Creates a subnet in a private network of a public cloud project.

## Properties

TBC

## Return Values

### Fn::GetAtt

`ProjectId` - See Argument Reference above.

`NetworkId` - See Argument Reference above.

`DhcpId` - See Argument Reference above.

`Start` - See Argument Reference above.

`End` - See Argument Reference above.

`Network` - See Argument Reference above.

`Region` - See Argument Reference above.

`GatewayIp` - The IP of the gateway.

`NoGateway` - See Argument Reference above.

`Cidr` - Ip Block representing the subnet cidr.

`IpPools` - List of ip pools allocated in the subnet.

`IpPools/network` - Global network with cidr.

`IpPools/region` - Region where this subnet is created.

`IpPools/dhcp` - DHCP enabled.

`IpPools/end` - Last ip for this region.

`IpPools/start` - First ip for this region.

## See Also

* [ovh_cloud_network_private_subnet](https://www.terraform.io/docs/providers/ovh/r/cloud_network_private_subnet.html) in the _Terraform Provider Documentation_