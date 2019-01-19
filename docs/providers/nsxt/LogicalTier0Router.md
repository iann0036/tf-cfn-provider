# Terraform::NSXT::LogicalTier0Router

This resource provides a method for the management of a tier 0 logical router.

## Properties

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of the resource.

`EdgeClusterId` - (Required) Edge Cluster ID for the logical Tier0 router. Changing this setting on existing router will re-create the router.

`FailoverMode` - (Optional) Failover mode which determines whether the preferred service router instance for given logical router will preempt the peer. Accepted values are PREEMPTIVE/NON_PREEMPTIVE. This setting is relevant only for ACTIVE_STANDBY high availability mode.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical Tier0 router.

`HighAvailabilityMode` - (Optional) High availability mode "ACTIVE_ACTIVE"/"ACTIVE_STANDBY". Changing this setting on existing router will re-create the router.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical Tier0 router.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`FirewallSections` - (Optional) The list of firewall sections for this router.

## See Also

* [nsxt_logical_tier0_router](https://www.terraform.io/docs/providers/nsxt/r/logical_tier0_router.html) in the _Terraform Provider Documentation_