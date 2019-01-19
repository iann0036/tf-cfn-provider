# Terraform::Google::ComputeRegionInstanceGroupManager

The Google Compute Engine Regional Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers)

~> **Note:** Use [google_compute_instance_group_manager](/docs/providers/google/r/compute_instance_group_manager.html) to create a single-zone instance group manager.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Fingerprint` - The fingerprint of the instance group manager.

`InstanceGroup` - The full URL of the instance group created by the manager.

`SelfLink` - The URL of the created resource.

## See Also

* [google_compute_region_instance_group_manager](https://www.terraform.io/docs/providers/google/r/compute_region_instance_group_manager.html) in the _Terraform Provider Documentation_