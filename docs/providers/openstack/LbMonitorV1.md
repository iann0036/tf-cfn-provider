# Terraform::OpenStack::LbMonitorV1

Manages a V1 load balancer monitor resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create an LB monitor. If omitted, the `Region` argument of the provider is used. Changing this creates a new LB monitor.

`Type` - (Required) The type of probe, which is PING, TCP, HTTP, or HTTPS, that is sent by the monitor to verify the member state. Changing this creates a new monitor.

`Delay` - (Required) The time, in seconds, between sending probes to members. Changing this creates a new monitor.

`Timeout` - (Required) Maximum number of seconds for a monitor to wait for a ping reply before it times out. The value must be less than the delay value. Changing this updates the timeout of the existing monitor.

`MaxRetries` - (Required) Number of permissible ping failures before changing the member's status to INACTIVE. Must be a number between 1 and 10. Changing this updates the max_retries of the existing monitor.

`UrlPath` - (Optional) Required for HTTP(S) types. URI path that will be accessed if monitor type is HTTP or HTTPS. Changing this updates the url_path of the existing monitor.

`HttpMethod` - (Optional) Required for HTTP(S) types. The HTTP method used for requests by the monitor. If this attribute is not specified, it defaults to "GET". Changing this updates the http_method of the existing monitor.

`ExpectedCodes` - (Optional) Required for HTTP(S) types. Expected HTTP codes for a passing HTTP(S) monitor. You can either specify a single status like "200", or a range like "200-202". Changing this updates the expected_codes of the existing monitor.

`AdminStateUp` - (Optional) The administrative state of the monitor. Acceptable values are "true" and "false". Changing this value updates the state of the existing monitor.

`TenantId` - (Optional) The owner of the monitor. Required if admin wants to create a monitor for another tenant. Changing this creates a new monitor.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Type` - See Properties above.

`Delay` - See Properties above.

`Timeout` - See Properties above.

`MaxRetries` - See Properties above.

`UrlPath` - See Properties above.

`HttpMethod` - See Properties above.

`ExpectedCodes` - See Properties above.

`AdminStateUp` - See Properties above.

`TenantId` - See Properties above.

## See Also

* [openstack_lb_monitor_v1](https://www.terraform.io/docs/providers/openstack/r/lb_monitor_v1.html) in the _Terraform Provider Documentation_