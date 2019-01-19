# Terraform::Google::ComputeInstanceGroup

Creates a group of dissimilar Compute Engine virtual machine instances.
For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)

-> Recreating an instance group that's in use by another resource will give a
`resourceInUseByAnotherResource` error. You can avoid this error with a
Terraform `lifecycle` block as outlined in the example below.

## Properties

`Name` - (Required) The name which the port will be mapped to.

`Zone` - (Required) The zone that this instance group should be created in.

`Description` - (Optional) An optional textual description of the instance group.

`Instances` - (Optional) List of instances in the group. They should be given as self_link URLs. When adding instances they must all be in the same network and zone as the instance group.

`NamedPort` - (Optional) The named port configuration. See the section below for details on configuration.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`Network` - (Optional) The URL of the network the instance group is in. If this is different from the network where the instances are in, the creation fails. Defaults to the network where the instances are in (if neither `Network` nor `Instances` is specified, this field will be blank).

`Port` - (Required) The port number to map the name to.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

`Size` - The number of instances in the group.

## See Also

* [google_compute_instance_group](https://www.terraform.io/docs/providers/google/r/compute_instance_group.html) in the _Terraform Provider Documentation_