# Terraform::OpenStack::NetworkingRouterV2

Manages a V2 router resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
router.

`Name` - (Optional) A unique name for the router. Changing this
updates the `Name` of an existing router.

`Description` - (Optional) Human-readable description for the router.

`AdminStateUp` - (Optional) Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`AdminStateUp` of an existing router.

`Distributed` - (Optional) Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.

`ExternalGateway` - (**Deprecated** - use `ExternalNetworkId` instead) The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.

`ExternalNetworkId` - (Optional) The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.

`EnableSnat` - (Optional) Enable Source NAT for the router. Valid values are
"true" or "false". An `ExternalNetworkId` has to be set in order to
set this property. Changing this updates the `EnableSnat` of the router.

`ExternalFixedIp` - (Optional) An external fixed IP for the router. This
can be repeated. The structure is described below. An `ExternalNetworkId`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.

`TenantId` - (Optional) The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.

`ValueSpecs` - (Optional) Map of additional driver-specific options.

`Tags` - (Optional) A set of string tags for the router.

`VendorOptions` - (Optional) Map of additional vendor-specific options.
Supported options are described below.

`AvailabilityZoneHints` -  (Optional) An availability zone is used to make
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.

### ExternalFixedIp Properties

`SubnetId` - (Optional) Subnet in which the fixed IP belongs to.

`IpAddress` - (Optional) The IP address to set on the router.

### VendorOptions Properties

`SetRouterGatewayAfterCreate` - (Optional) Boolean to control whether
the Router gateway is assigned during creation or updated after creation.


## Return Values

### Fn::GetAtt

`Id` - ID of the router.

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`AdminStateUp` - See Properties above.

`ExternalGateway` - See Properties above.

`ExternalNetworkId` - See Properties above.

`EnableSnat` - See Properties above.

`ExternalFixedIp` - See Properties above.

`TenantId` - See Properties above.

`ValueSpecs` - See Properties above.

`AvailabilityZoneHints` - See Properties above.

`Tags` - See Properties above.

## See Also

* [openstack_networking_router_v2](https://www.terraform.io/docs/providers/openstack/r/networking_router_v2.html) in the _Terraform Provider Documentation_