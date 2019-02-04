# Terraform::Google::ComputeInstanceFromTemplate

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).

This resource is specifically to create a compute instance from a given
`SourceInstanceTemplate`. To create an instance without a template, use the
`Terraform::Google::ComputeInstance` resource.

## Properties

`Name` - (Required) A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

`SourceInstanceTemplate` - (Required) Name or self link of an instance
template to create the instance based on.

`Zone` - (Optional) The zone that the machine should be created in. If not
set, the provider zone is used.


## See Also

* [google_compute_instance_from_template](https://www.terraform.io/docs/providers/google/r/compute_instance_from_template.html) in the _Terraform Provider Documentation_