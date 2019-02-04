# Terraform::Google::ComputeRegionBackendService

A Region Backend Service defines a regionally-scoped group of virtual machines that will serve traffic for load balancing.
For more information see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/internal/)
and [API](https://cloud.google.com/compute/docs/reference/latest/regionBackendServices).

~> **Note**: Region backend services can only be used when using internal load balancing. For external load balancing, use
  [`Terraform::Google::ComputeBackendService`](compute_backend_service.html) instead.

## Properties

`Name` - (Required) The name of the backend service.

`HealthChecks` - (Required) Specifies a list of health checks
for checking the health of the backend service. Currently at most
one health check can be specified, and a health check is required.

`Backend` - (Optional) The list of backends that serve this BackendService.
Structure is documented below.

`Description` - (Optional) The textual description for the backend service.

`Project` - (Optional) The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

`Protocol` - (Optional) The protocol for incoming requests. Defaults to
`TCP`.

`SessionAffinity` - (Optional) How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP`, `CLIENT_IP_PROTO`, or `CLIENT_IP_PORT_PROTO`.
Defaults to `NONE`.

`Region` - (Optional) The Region in which the created address should reside.
If it is not provided, the provider region is used.

`TimeoutSec` - (Optional) The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

`ConnectionDrainingTimeoutSec` - (Optional) Time for which instance will be drained
(not accept new connections, but still work to finish started ones). Defaults to `0`.

### Backend Properties

`Group` - (Required) The name or URI of a Compute Engine instance group
(`Terraform::Google::ComputeRegionInstanceGroupManager.xyz.instanceGroup`) that can
receive traffic. Instance groups must contain at least one instance.

`Description` - (Optional) Textual description for the backend.


## Return Values

### Fn::GetAtt

`Fingerprint` - The fingerprint of the backend service.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_region_backend_service](https://www.terraform.io/docs/providers/google/r/compute_region_backend_service.html) in the _Terraform Provider Documentation_