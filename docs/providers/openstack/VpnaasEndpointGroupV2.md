# Terraform::OpenStack::VpnaasEndpointGroupV2

Manages a V2 Neutron Endpoint Group resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create an endpoint group. If omitted, the `Region` argument of the provider is used. Changing this creates a new group.

`Name` - (Optional) The name of the group. Changing this updates the name of the existing group.

`TenantId` - (Optional) The owner of the group. Required if admin wants to create an endpoint group for another project. Changing this creates a new group.

`Description` - (Optional) The human-readable description for the group. Changing this updates the description of the existing group.

`Type` -  The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan. Changing this creates a new group.

`Endpoints` - List of endpoints of the same type, for the endpoint group. The values will depend on the type. Changing this creates a new group.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`TenantId` - See Properties above.

`Description` - See Properties above.

`Type` - See Properties above.

`Endpoints` - See Properties above.

`ValueSpecs` - See Properties above.

## See Also

* [openstack_vpnaas_endpoint_group_v2](https://www.terraform.io/docs/providers/openstack/r/vpnaas_endpoint_group_v2.html) in the _Terraform Provider Documentation_