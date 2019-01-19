# Terraform::OpenStack::NetworkingFloatingipV2

Manages a V2 floating IP resource within OpenStack Neutron (networking)
that can be used for load balancers.
These are similar to Nova (compute) floating IP resources,
but only compute floating IPs can be used with compute instances.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Region` - See Argument Reference above.

`Description` - See Argument Reference above.

`Pool` - See Argument Reference above.

`Address` - The actual floating IP address itself.

`PortId` - ID of associated port.

`TenantId` - the ID of the tenant in which to create the floating IP.

`FixedIp` - The fixed IP which the floating IP maps to.

`Tags` - See Argument Reference above.

## See Also

* [openstack_networking_floatingip_v2](https://www.terraform.io/docs/providers/openstack/r/networking_floatingip_v2.html) in the _Terraform Provider Documentation_