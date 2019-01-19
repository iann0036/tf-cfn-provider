# Terraform::HuaweiCloud::NetworkingNetworkV2

Manages a V2 Neutron network resource within HuaweiCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create a Neutron network. If omitted, the `Region` argument of the provider is used. Changing this creates a new network.

`Name` - (Optional) The name of the network. Changing this updates the name of the existing network.

`Shared` - (Optional)  Specifies whether the network resource can be accessed by any tenant or not. Changing this updates the sharing capabalities of the existing network.

`TenantId` - (Optional) The owner of the network. Required if admin wants to create a network for another tenant. Changing this creates a new network.

`AdminStateUp` - (Optional) The administrative state of the network. Acceptable values are "true" and "false". Changing this value updates the state of the existing network.

`Segments` - (Optional) An array of one or more provider segment objects.

`ValueSpecs` - (Optional) Map of additional options.

`AvailabilityZoneHints` -  (Optional) An availability zone is used to make network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing this creates a new network.

### Segments Properties

`PhysicalNetwork` - The phisical network where this network is implemented.

`SegmentationId` - An isolated segment on the physical network.

`NetworkType` - The type of physical network.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Shared` - See Properties above.

`TenantId` - See Properties above.

`AdminStateUp` - See Properties above.

`AvailabilityZoneHints` - See Properties above.

## See Also

* [huaweicloud_networking_network_v2](https://www.terraform.io/docs/providers/huaweicloud/r/networking_network_v2.html) in the _Terraform Provider Documentation_