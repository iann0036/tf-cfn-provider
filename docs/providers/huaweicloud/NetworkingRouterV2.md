# Terraform::HuaweiCloud::NetworkingRouterV2

Manages a V2 router resource within HuaweiCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client. A networking client is needed to create a router. If omitted, the `Region` argument of the provider is used. Changing this creates a new router.

`Name` - (Optional) A unique name for the router. Changing this updates the `Name` of an existing router.

`AdminStateUp` - (Optional) Administrative up/down status for the router (must be "true" or "false" if provided). Changing this updates the `AdminStateUp` of an existing router.

`Distributed` - (Optional) Indicates whether or not to create a distributed router. The default policy setting in Neutron restricts usage of this property to administrative users only.

`ExternalNetworkId` - (Optional) The network UUID of an external gateway for the router. A router with an external gateway is required if any compute instances or load balancers will be using floating IPs. Changing this updates the external gateway of the router.

`EnableSnat` - (Optional) Enable Source NAT for the router. Valid values are "true" or "false". An `ExternalNetworkId` has to be set in order to set this property. Changing this updates the `EnableSnat` of the router.

`ExternalFixedIp` - (Optional) An external fixed IP for the router. This can be repeated. The structure is described below. An `ExternalNetworkId` has to be set in order to set this property. Changing this updates the external fixed IPs of the router.

`TenantId` - (Optional) The owner of the floating IP. Required if admin wants to create a router for another tenant. Changing this creates a new router.

`ValueSpecs` - (Optional) Map of additional driver-specific options.

`AvailabilityZoneHints` -  (Optional) An availability zone is used to make network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing this creates a new router.

`SubnetId` - (Optional) Subnet in which the fixed IP belongs to.

`IpAddress` - (Optional) The IP address to set on the router.


## Return Values

### Fn::GetAtt

`Id` - ID of the router.

`Region` - See Properties above.

`Name` - See Properties above.

`AdminStateUp` - See Properties above.

`ExternalNetworkId` - See Properties above.

`EnableSnat` - See Properties above.

`ExternalFixedIp` - See Properties above.

`TenantId` - See Properties above.

`ValueSpecs` - See Properties above.

`AvailabilityZoneHints` - See Properties above.

## See Also

* [huaweicloud_networking_router_v2](https://www.terraform.io/docs/providers/huaweicloud/r/networking_router_v2.html) in the _Terraform Provider Documentation_