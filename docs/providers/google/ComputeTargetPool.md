# Terraform::Google::ComputeTargetPool

Manages a Target Pool within GCE. This is a collection of instances used as
target of a network load balancer (Forwarding Rule). For more information see
[the official
documentation](https://cloud.google.com/compute/docs/load-balancing/network/target-pools)
and [API](https://cloud.google.com/compute/docs/reference/latest/targetPools).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_target_pool](https://www.terraform.io/docs/providers/google/r/compute_target_pool.html) in the _Terraform Provider Documentation_