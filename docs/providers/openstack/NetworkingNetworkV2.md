# Terraform::OpenStack::NetworkingNetworkV2

Manages a V2 Neutron network resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create a Neutron network. If omitted, the `Region` argument of the provider is used. Changing this creates a new network.

`Name` - (Optional) The name of the network. Changing this updates the name of the existing network.

`Description` - (Optional) Human-readable description of the network. Changing this updates the name of the existing network.

`Shared` - (Optional) Specifies whether the network resource can be accessed by any tenant or not. Changing this updates the sharing capabilities of the existing network.

`External` - (Optional) Specifies whether the network resource has the external routing facility. Valid values are true and false. Defaults to false. Changing this updates the external attribute of the existing network.

`TenantId` - (Optional) The owner of the network. Required if admin wants to create a network for another tenant. Changing this creates a new network.

`AdminStateUp` - (Optional) The administrative state of the network. Acceptable values are "true" and "false". Changing this value updates the state of the existing network.

`Segments` - (Optional) An array of one or more provider segment objects.

`ValueSpecs` - (Optional) Map of additional options.

`AvailabilityZoneHints` -  (Optional) An availability zone is used to make network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing this creates a new network.

`Tags` - (Optional) A set of string tags for the network.

`TransparentVlan` - (Optional) Specifies whether the network resource has the VLAN transparent attribute set. Valid values are true and false. Defaults to false. Changing this updates the `TransparentVlan` attribute of the existing network.

### Segments Properties

`PhysicalNetwork` - The physical network where this network is implemented.

`SegmentationId` - An isolated segment on the physical network.

`NetworkType` - The type of physical network.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Shared` - See Properties above.

`External` - See Properties above.

`TenantId` - See Properties above.

`AdminStateUp` - See Properties above.

`AvailabilityZoneHints` - See Properties above.

`Tags` - See Properties above.

`TransparentVlan` - See Properties above.

## See Also

* [openstack_networking_network_v2](https://www.terraform.io/docs/providers/openstack/r/networking_network_v2.html) in the _Terraform Provider Documentation_