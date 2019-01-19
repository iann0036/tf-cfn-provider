# Terraform::Google::ComputeBackendService

A Backend Service defines a group of virtual machines that will serve traffic for load balancing. For more information
see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
and the [API](https://cloud.google.com/compute/docs/reference/latest/backendServices).

For internal load balancing, use a [google_compute_region_backend_service](/docs/providers/google/r/compute_region_backend_service.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Fingerprint` - The fingerprint of the backend service.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_backend_service](https://www.terraform.io/docs/providers/google/r/compute_backend_service.html) in the _Terraform Provider Documentation_