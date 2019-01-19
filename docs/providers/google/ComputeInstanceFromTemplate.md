# Terraform::Google::ComputeInstanceFromTemplate

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).

This resource is specifically to create a compute instance from a given
`source_instance_template`. To create an instance without a template, use the
`google_compute_instance` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [google_compute_instance_from_template](https://www.terraform.io/docs/providers/google/r/compute_instance_from_template.html) in the _Terraform Provider Documentation_