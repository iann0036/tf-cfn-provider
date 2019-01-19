# Terraform::NSXT::LogicalTier1Router

This resource provides a method for the management of a tier 1 logical router. A tier 1 logical router is often used for tenants, users and applications. There can be many tier 1 logical routers connected to a common tier 0 provider router.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the logical Tier1 router.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`AdvertiseConfigRevision` - Indicates current revision number of the advertisement configuration object as seen by NSX-T API server. This attribute can be useful for debugging.

`FirewallSections` - (Optional) The list of firewall sections for this router.

## See Also

* [nsxt_logical_tier1_router](https://www.terraform.io/docs/providers/nsxt/r/logical_tier1_router.html) in the _Terraform Provider Documentation_