# Terraform::Google::ComputeSharedVpcServiceProject

Enables the Google Compute Engine
[Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
feature for a project, assigning it as a Shared VPC service project associated
with a given host project.

For more information, see,
[the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
where the Shared VPC feature is referred to by its former name "XPN".

## Properties

`HostProject` - (Required) The ID of a host project to associate.

`ServiceProject` - (Required) The ID of the project that will serve as a Shared VPC service project.


## See Also

* [google_compute_shared_vpc_service_project](https://www.terraform.io/docs/providers/google/r/compute_shared_vpc_service_project.html) in the _Terraform Provider Documentation_