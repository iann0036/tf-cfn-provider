# Terraform::Cloudflare::LoadBalancerMonitor

If you're using Cloudflare's Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S).

## Properties

`ExpectedBody` - (Required) A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.

`ExpectedCodes` - (Required) The expected HTTP response code or code range of the health check. Eg `2xx`.

`Method` - (Optional) The HTTP method to use for the health check. Default: "GET".

`Timeout` - (Optional) The timeout (in seconds) before marking the health check as failed. Default: 5.

`Path` - (Optional) The endpoint path to health check against. Default: "/".

`Interval` - (Optional) The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.

`Retries` - (Optional) The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.

`Header` - (Optional) The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. Fields documented below.

`Type` - (Optional) The protocol to use for the healthcheck. Currently supported protocols are 'HTTP' and 'HTTPS'. Default: "http".

`Description` - (Optional) Free text description.

`Header` - (Required) The header name.

`Values` - (Required) A list of string values for the header.


## Return Values

### Fn::GetAtt

`Id` - Load balancer monitor ID.

`CreatedOn` - The RFC3339 timestamp of when the load balancer monitor was created.

`ModifiedOn` - The RFC3339 timestamp of when the load balancer monitor was last modified.

## See Also

* [cloudflare_load_balancer_monitor](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_monitor.html) in the _Terraform Provider Documentation_