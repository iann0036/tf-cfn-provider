# Terraform::OpenStack::LbVipV1

Manages a V1 load balancer vip resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create a VIP. If omitted, the `Region` argument of the provider is used. Changing this creates a new VIP.

`Name` - (Required) The name of the vip. Changing this updates the name of the existing vip.

`SubnetId` - (Required) The network on which to allocate the vip's address. A tenant can only create vips on networks authorized by policy (e.g. networks that belong to them or networks that are shared). Changing this creates a new vip.

`Protocol` - (Required)  The protocol - can be either 'TCP, 'HTTP', or HTTPS'. Changing this creates a new vip.

`Port` - (Required) The port on which to listen for client traffic. Changing this creates a new vip.

`PoolId` - (Required) The ID of the pool with which the vip is associated. Changing this updates the pool_id of the existing vip.

`TenantId` - (Optional) The owner of the vip. Required if admin wants to create a vip member for another tenant. Changing this creates a new vip.

`Address` - (Optional)  The IP address of the vip. Changing this creates a new vip.

`Description` - (Optional) Human-readable description for the vip. Changing this updates the description of the existing vip.

`Persistence` - (Optional) Omit this field to prevent session persistence. The persistence object structure is documented below. Changing this updates the persistence of the existing vip.

`ConnLimit` - (Optional) The maximum number of connections allowed for the vip. Default is -1, meaning no limit. Changing this updates the conn_limit of the existing vip.

`FloatingIp` - (Optional) A *Networking* Floating IP that will be associated with the vip. The Floating IP must be provisioned already.

`AdminStateUp` - (Optional) The administrative state of the vip. Acceptable values are "true" and "false". Changing this value updates the state of the existing vip.

`Type` - (Required) The type of persistence mode. Valid values are "SOURCE_IP", "HTTP_COOKIE", or "APP_COOKIE".

`CookieName` - (Optional) The name of the cookie if persistence mode is set appropriately.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`SubnetId` - See Properties above.

`Protocol` - See Properties above.

`Port` - See Properties above.

`PoolId` - See Properties above.

`TenantId` - See Properties above.

`Address` - See Properties above.

`Description` - See Properties above.

`Persistence` - See Properties above.

`ConnLimit` - See Properties above.

`FloatingIp` - See Properties above.

`AdminStateUp` - See Properties above.

`PortId` - Port UUID for this VIP at associated floating IP (if any).

## See Also

* [openstack_lb_vip_v1](https://www.terraform.io/docs/providers/openstack/r/lb_vip_v1.html) in the _Terraform Provider Documentation_