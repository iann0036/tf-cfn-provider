# Terraform::Google::ComputeRegionBackendService

A Region Backend Service defines a regionally-scoped group of virtual machines that will serve traffic for load balancing.
For more information see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/internal/)
and [API](https://cloud.google.com/compute/docs/reference/latest/regionBackendServices).

~> **Note**: Region backend services can only be used when using internal load balancing. For external load balancing, use
  [`google_compute_backend_service`](compute_backend_service.html) instead.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Fingerprint` - The fingerprint of the backend service.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_region_backend_service](https://www.terraform.io/docs/providers/google/r/compute_region_backend_service.html) in the _Terraform Provider Documentation_