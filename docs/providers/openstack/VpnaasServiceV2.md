# Terraform::OpenStack::VpnaasServiceV2

Manages a V2 Neutron VPN service resource within OpenStack.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Name` - See Argument Reference above.

`TenantId` - See Argument Reference above.

`RouterId` - See Argument Reference above.

`AdminStateUp` - See Argument Reference above.

`SubnetId` - See Argument Reference above.

`Status` - Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.

`ExternalV6Ip` - The read-only external (public) IPv6 address that is used for the VPN service.

`ExternalV4Ip` - The read-only external (public) IPv4 address that is used for the VPN service.

`Description` - See Argument Reference above.

`ValueSpecs` - See Argument Reference above.

## See Also

* [openstack_vpnaas_service_v2](https://www.terraform.io/docs/providers/openstack/r/vpnaas_service_v2.html) in the _Terraform Provider Documentation_