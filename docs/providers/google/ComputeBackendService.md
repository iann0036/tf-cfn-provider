# Terraform::Google::ComputeBackendService

A Backend Service defines a group of virtual machines that will serve traffic for load balancing. For more information
see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
and the [API](https://cloud.google.com/compute/docs/reference/latest/backendServices).

For internal load balancing, use a [google_compute_region_backend_service](/docs/providers/google/r/compute_region_backend_service.html).

## Properties

`Name` - (Required) The name of the backend service.

`HealthChecks` - (Required) Specifies a list of HTTP/HTTPS health checks for checking the health of the backend service. Currently at most one health check can be specified, and a health check is required.

`Backend` - (Optional) The list of backends that serve this BackendService. Structure is documented below.

`Iap` - (Optional) Specification for the Identity-Aware proxy. Disabled if not specified. Structure is documented below.

`CdnPolicy` - (Optional) Cloud CDN configuration for this BackendService. Structure is documented below.

`ConnectionDrainingTimeoutSec` - (Optional) Time for which instance will be drained (not accept new connections, but still work to finish started ones). Defaults to `300`.

`CustomRequestHeaders` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Headers that the HTTP/S load balancer should add to proxied requests. See [guide](https://cloud.google.com/compute/docs/load-balancing/http/backend-service#user-defined-request-headers) for details.

`Description` - (Optional) The textual description for the backend service.

`EnableCdn` - (Optional) Whether or not to enable the Cloud CDN on the backend service.

`PortName` - (Optional) The name of a service that has been added to an instance group in this backend. See [related docs](https://cloud.google.com/compute/docs/instance-groups/#specifying_service_endpoints) for details. Defaults to http.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`Protocol` - (Optional) The protocol for incoming requests. Defaults to `HTTP`.

`SecurityPolicy` - (Optional) Name or URI of a [security policy](https://cloud.google.com/armor/docs/security-policy-concepts) to add to the backend service.

`SessionAffinity` - (Optional) How to distribute load. Options are `NONE` (no affinity), `CLIENT_IP` (hash of the source/dest addresses / ports), and `GENERATED_COOKIE` (distribute load using a generated session cookie).

`AffinityCookieTtlSec` - (Optional) Lifetime of cookies in seconds if session_affinity is `GENERATED_COOKIE`. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day.

`TimeoutSec` - (Optional) The number of secs to wait for a backend to respond to a request before considering the request failed. Defaults to `30`.

### Backend Properties

`Group` - (Required) The name or URI of a Compute Engine instance group (`Terraform::Google::ComputeInstanceGroupManager.xyz.instanceGroup`) that can receive traffic.

`BalancingMode` - (Optional) Defines the strategy for balancing load. Defaults to `UTILIZATION`.

`CapacityScaler` - (Optional) A float in the range [0, 1.0] that scales the maximum parameters for the group (e.g., max rate). A value of 0.0 will cause no requests to be sent to the group (i.e., it adds the group in a drained state). The default is 1.0.

`Description` - (Optional) Textual description for the backend.

`MaxRate` - (Optional) Maximum requests per second (RPS) that the group can handle.

`MaxRatePerInstance` - (Optional) The maximum per-instance requests per second (RPS).

`MaxConnections` - (Optional) The max number of simultaneous connections for the group. Can be used with either CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set.

`MaxConnectionsPerInstance` - (Optional) The max number of simultaneous connections that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set.

`MaxUtilization` - (Optional) The target CPU utilization for the group as a float in the range [0.0, 1.0]. This flag can only be provided when the balancing mode is `UTILIZATION`. Defaults to `0.8`.

### CdnPolicy Properties

`CacheKeyPolicy` - (Optional) The CacheKeyPolicy for this CdnPolicy. Structure is documented below.

### CacheKeyPolicy Properties

`IncludeHost` - (Optional) If true, requests to different hosts will be cached separately.

`IncludeProtocol` - (Optional) If true, http and https requests will be cached separately.

`IncludeQueryString` - (Optional) If true, include query string parameters in the cache key according to `QueryStringWhitelist` and `QueryStringBlacklist`. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely.

`QueryStringBlacklist` - (Optional) Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify `QueryStringWhitelist` or `QueryStringBlacklist`, not both. '&' and '=' will be percent encoded and not treated as delimiters.

`QueryStringWhitelist` - (Optional) Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify `QueryStringWhitelist` or `QueryStringBlacklist`, not both. '&' and '=' will be percent encoded and not treated as delimiters.

### Iap Properties

`Oauth2ClientId` - (Required) The client ID for use with OAuth 2.0.

`Oauth2ClientSecret` - (Required) The client secret for use with OAuth 2.0.


## Return Values

### Fn::GetAtt

`Fingerprint` - The fingerprint of the backend service.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_backend_service](https://www.terraform.io/docs/providers/google/r/compute_backend_service.html) in the _Terraform Provider Documentation_