# Terraform::NSXT::LogicalTier1Router

This resource provides a method for the management of a tier 1 logical router. A tier 1 logical router is often used for tenants, users and applications. There can be many tier 1 logical routers connected to a common tier 0 provider router.

## Properties

`EdgeClusterId` - (Optional) Edge Cluster ID for the logical Tier1 router.

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of the resource.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical Tier1 router.

`FailoverMode` - (Optional) This failover mode determines, whether the preferred service router instance for given logical router will preempt the peer. Note - It can be specified if and only if logical router is ACTIVE_STANDBY and NON_PREEMPTIVE mode is supported only for a Tier1 logical router. For ACTIVE_ACTIVE logical routers, this field must not be populated.

`EnableRouterAdvertisement` - (Optional) Enable the router advertisement.

`AdvertiseConnectedRoutes` - (Optional) Enable the router advertisement for all NSX connected routes.

`AdvertiseStaticRoutes` - (Optional) Enable the router advertisement for static routes.

`AdvertiseNatRoutes` - (Optional) Enable the router advertisement for NAT routes.

`AdvertiseLbVipRoutes` - (Optional) Enable the router advertisement for LB VIP routes.

`AdvertiseLbSnatIpRoutes` - (Optional) Enable the router advertisement for LB SNAT IP routes.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical Tier1 router.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`AdvertiseConfigRevision` - Indicates current revision number of the advertisement configuration object as seen by NSX-T API server. This attribute can be useful for debugging.

`FirewallSections` - (Optional) The list of firewall sections for this router.

## See Also

* [nsxt_logical_tier1_router](https://www.terraform.io/docs/providers/nsxt/r/logical_tier1_router.html) in the _Terraform Provider Documentation_