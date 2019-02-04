# Terraform::FlexibleEngine::NetworkingFloatingipV2

Manages a V2 floating IP resource within FlexibleEngine Neutron (networking)
that can be used for load balancers.
These are similar to Nova (compute) floating IP resources,
but only compute floating IPs can be used with compute instances.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

`Pool` - (Required) The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

`PortId` - (Optional) ID of an existing port with at least one IP address to
associate with this floating IP.

`TenantId` - (Optional) The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address).

`FixedIp` - Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Pool` - See Properties above.

`Address` - The actual floating IP address itself.

`PortId` - ID of associated port.

`TenantId` - the ID of the tenant in which to create the floating IP.

`FixedIp` - The fixed IP which the floating IP maps to.

## See Also

* [flexibleengine_networking_floatingip_v2](https://www.terraform.io/docs/providers/flexibleengine/r/networking_floatingip_v2.html) in the _Terraform Provider Documentation_