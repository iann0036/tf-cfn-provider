# Terraform::OpenStack::NetworkingTrunkV2

Manages a networking V2 trunk resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client.
A networking client is needed to create a trunk. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
trunk.

`Name` - (Optional) A unique name for the trunk. Changing this
updates the `Name` of an existing trunk.

`Description` - (Optional) Human-readable description of the trunk. Changing this
updates the name of the existing trunk.

`PortId` - (Required) The ID of the port to be used as the parent port of the
trunk. This is the port that should be used as the compute instance network
port. Changing this creates a new trunk.

`AdminStateUp` - (Optional) Administrative up/down status for the trunk
(must be "true" or "false" if provided). Changing this updates the
`AdminStateUp` of an existing trunk.

`TenantId` - (Optional) The owner of the Trunk. Required if admin wants
to create a trunk on behalf of another tenant. Changing this creates a new trunk.

`SubPort` - (Optional) The set of ports that will be made subports of the trunk.
The structure of each subport is described below.

`Tags` - (Optional) A set of string tags for the port.

### SubPort Properties

`PortId` - (Required) The ID of the port to be made a subport of the trunk.

`SegmentationType` - (Required) The segmentation technology to use, e.g., "vlan".

`SegmentationId` - (Required) The numeric id of the subport segment.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`PortId` - See Properties above.

`AdminStateUp` - See Properties above.

`TenantId` - See Properties above.

`SubPort` - See Properties above.

`Tags` - See Properties above.

`AllTags` - The collection of tags assigned on the trunk, which have been.

## See Also

* [openstack_networking_trunk_v2](https://www.terraform.io/docs/providers/openstack/r/networking_trunk_v2.html) in the _Terraform Provider Documentation_