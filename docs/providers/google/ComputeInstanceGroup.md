# Terraform::Google::ComputeInstanceGroup

Creates a group of dissimilar Compute Engine virtual machine instances.
For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)

-> Recreating an instance group that's in use by another resource will give a
`resourceInUseByAnotherResource` error. You can avoid this error with a
Terraform `lifecycle` block as outlined in the example below.

## Properties

TBC

## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

`Size` - The number of instances in the group.

## See Also

* [google_compute_instance_group](https://www.terraform.io/docs/providers/google/r/compute_instance_group.html) in the _Terraform Provider Documentation_