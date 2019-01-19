# Terraform::NSXT::LbPassiveMonitor

Provides a resource to configure lb passive monitor on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb passive monitor.

`MaxFails` - (Optional) When consecutive failures reach this value, the member is considered temporarily unavailable for a configurable period.

`Timeout` - (Optional) After this timeout period, the member is probed again.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb_passive_monitor.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_passive_monitor](https://www.terraform.io/docs/providers/nsxt/r/lb_passive_monitor.html) in the _Terraform Provider Documentation_