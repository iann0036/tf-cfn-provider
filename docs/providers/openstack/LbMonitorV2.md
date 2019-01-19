# Terraform::OpenStack::LbMonitorV2

Manages a V2 monitor resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create an . If omitted, the `Region` argument of the provider is used. Changing this creates a new monitor.

`PoolId` - (Required) The id of the pool that this monitor will be assigned to.

`Name` - (Optional) The Name of the Monitor.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns the monitor.  Only administrative users can specify a tenant UUID other than their own. Changing this creates a new monitor.

`Type` - (Required) The type of probe, which is PING, TCP, HTTP, or HTTPS, that is sent by the load balancer to verify the member state. Changing this creates a new monitor.

`Delay` - (Required) The time, in seconds, between sending probes to members.

`Timeout` - (Required) Maximum number of seconds for a monitor to wait for a ping reply before it times out. The value must be less than the delay value.

`MaxRetries` - (Required) Number of permissible ping failures before changing the member's status to INACTIVE. Must be a number between 1 and 10..

`UrlPath` - (Optional) Required for HTTP(S) types. URI path that will be accessed if monitor type is HTTP or HTTPS.

`HttpMethod` - (Optional) Required for HTTP(S) types. The HTTP method used for requests by the monitor. If this attribute is not specified, it defaults to "GET".

`ExpectedCodes` - (Optional) Required for HTTP(S) types. Expected HTTP codes for a passing HTTP(S) monitor. You can either specify a single status like "200", or a range like "200-202".

`AdminStateUp` - (Optional) The administrative state of the monitor. A valid value is true (UP) or false (DOWN).


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the monitor.

`TenantId` - See Properties above.

`Type` - See Properties above.

`Delay` - See Properties above.

`Timeout` - See Properties above.

`MaxRetries` - See Properties above.

`UrlPath` - See Properties above.

`HttpMethod` - See Properties above.

`ExpectedCodes` - See Properties above.

`AdminStateUp` - See Properties above.

## See Also

* [openstack_lb_monitor_v2](https://www.terraform.io/docs/providers/openstack/r/lb_monitor_v2.html) in the _Terraform Provider Documentation_