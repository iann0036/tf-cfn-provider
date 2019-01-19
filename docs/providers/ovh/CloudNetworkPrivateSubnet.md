# Terraform::OVH::CloudNetworkPrivateSubnet

Creates a subnet in a private network of a public cloud project.

## Properties

`ProjectId` - (Required) The id of the public cloud project. If omitted, the `OVH_PROJECT_ID` environment variable is used. Changing this forces a new resource to be created.

`NetworkId` - (Required) The id of the network. Changing this forces a new resource to be created.

`Dhcp` - (Optional) Enable DHCP. Changing this forces a new resource to be created. Defaults to false. _.

`Start` - (Required) First ip for this region. Changing this value recreates the subnet.

`End` - (Required) Last ip for this region. Changing this value recreates the subnet.

`Network` - (Required) Global network in CIDR format. Changing this value recreates the subnet.

`Region` - The region in which the network subnet will be created. Ex.: "GRA1". Changing this value recreates the resource.

`NoGateway` - Set to true if you don't want to set a default gateway IP. Changing this value recreates the resource. Defaults to false.


## Return Values

### Fn::GetAtt

`ProjectId` - See Properties above.

`NetworkId` - See Properties above.

`DhcpId` - See Properties above.

`Start` - See Properties above.

`End` - See Properties above.

`Network` - See Properties above.

`Region` - See Properties above.

`GatewayIp` - The IP of the gateway.

`NoGateway` - See Properties above.

`Cidr` - Ip Block representing the subnet cidr.

`IpPools` - List of ip pools allocated in the subnet.

`IpPools/network` - Global network with cidr.

`IpPools/region` - Region where this subnet is created.

`IpPools/dhcp` - DHCP enabled.

`IpPools/end` - Last ip for this region.

`IpPools/start` - First ip for this region.

## See Also

* [ovh_cloud_network_private_subnet](https://www.terraform.io/docs/providers/ovh/r/cloud_network_private_subnet.html) in the _Terraform Provider Documentation_