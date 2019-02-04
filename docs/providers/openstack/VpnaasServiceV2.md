# Terraform::OpenStack::VpnaasServiceV2

Manages a V2 Neutron VPN service resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
service.

`Name` - (Optional) The name of the service. Changing this updates the name of
the existing service.

`TenantId` - (Optional) The owner of the service. Required if admin wants to
create a service for another project. Changing this creates a new service.

`Description` - (Optional) The human-readable description for the service.
Changing this updates the description of the existing service.

`AdminStateUp` - (Optional) The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing service.

`SubnetId` - (Optional) SubnetID is the ID of the subnet. Default is null.

`RouterId` - (Required) The ID of the router. Changing this creates a new service.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`TenantId` - See Properties above.

`RouterId` - See Properties above.

`AdminStateUp` - See Properties above.

`SubnetId` - See Properties above.

`Status` - Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.

`ExternalV6Ip` - The read-only external (public) IPv6 address that is used for the VPN service.

`ExternalV4Ip` - The read-only external (public) IPv4 address that is used for the VPN service.

`Description` - See Properties above.

`ValueSpecs` - See Properties above.

## See Also

* [openstack_vpnaas_service_v2](https://www.terraform.io/docs/providers/openstack/r/vpnaas_service_v2.html) in the _Terraform Provider Documentation_