# Terraform::NSXT::LbIcmpMonitor

Provides a resource to configure lb icmp monitor on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb icmp monitor.

`FallCount` - (Optional) Number of consecutive checks must fail before marking it down.

`Interval` - (Optional) The frequency at which the system issues the monitor check (in seconds).

`MonitorPort` - (Optional) If the monitor port is specified, it would override pool member port setting for healthcheck. Port range is not supported.

`RiseCount` - (Optional) Number of consecutive checks must pass before marking it up.

`Timeout` - (Optional) Number of seconds the target has in which to respond to the monitor request.

`DataLength` - (Optional) The data size (in bytes) of the ICMP healthcheck packet.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb_icmp_monitor.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_icmp_monitor](https://www.terraform.io/docs/providers/nsxt/r/lb_icmp_monitor.html) in the _Terraform Provider Documentation_