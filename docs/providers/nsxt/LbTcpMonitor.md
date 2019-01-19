# Terraform::NSXT::LbTcpMonitor

Provides a resource to configure lb tcp monitor on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb tcp monitor.

`FallCount` - (Optional) Number of consecutive checks must fail before marking it down.

`Interval` - (Optional) The frequency at which the system issues the monitor check (in seconds).

`MonitorPort` - (Optional) If the monitor port is specified, it would override pool member port setting for healthcheck. Port range is not supported.

`RiseCount` - (Optional) Number of consecutive checks must pass before marking it up.

`Timeout` - (Optional) Number of seconds the target has in which to respond to the monitor request.

`Receive` - (Optional) Expected data, if specified, can be anywhere in the response and it has to be a string, regular expressions are not supported.

`Send` - (Optional) Payload to send out to the monitored server. If both send and receive are not specified, then just a TCP connection is established (3-way handshake) to validate server is healthy, no data is sent.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb_tcp_monitor.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_tcp_monitor](https://www.terraform.io/docs/providers/nsxt/r/lb_tcp_monitor.html) in the _Terraform Provider Documentation_