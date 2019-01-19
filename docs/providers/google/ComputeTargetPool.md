# Terraform::Google::ComputeTargetPool

Manages a Target Pool within GCE. This is a collection of instances used as
target of a network load balancer (Forwarding Rule). For more information see
[the official
documentation](https://cloud.google.com/compute/docs/load-balancing/network/target-pools)
and [API](https://cloud.google.com/compute/docs/reference/latest/targetPools).

## Properties

`Name` - (Required) A unique name for the resource, required by GCE. Changing this forces a new resource to be created.

`BackupPool` - (Optional) URL to the backup target pool. Must also set failover\_ratio.

`Description` - (Optional) Textual description field.

`FailoverRatio` - (Optional) Ratio (0 to 1) of failed nodes before using the backup pool (which must also be set).

`HealthChecks` - (Optional) List of zero or one health check name or self_link. Only legacy `Terraform::Google::ComputeHttpHealthCheck` is supported.

`Instances` - (Optional) List of instances in the pool. They can be given as URLs, or in the form of "zone/name". Note that the instances need not exist at the time of target pool creation, so there is no need to use the Terraform interpolators to create a dependency on the instances from the target pool.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`Region` - (Optional) Where the target pool resides. Defaults to project region.

`SessionAffinity` - (Optional) How to distribute load. Options are "NONE" (no affinity). "CLIENT\_IP" (hash of the source/dest addresses / ports), and "CLIENT\_IP\_PROTO" also includes the protocol (default "NONE").


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_target_pool](https://www.terraform.io/docs/providers/google/r/compute_target_pool.html) in the _Terraform Provider Documentation_