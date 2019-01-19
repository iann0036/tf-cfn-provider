# Terraform::Triton::ServiceGroup

The `Terraform::Triton::ServiceGroup` resource represents a Triton Service Group.

~> **NOTE:**  Triton Service Groups are in Preview and only supported in specific regions at this time. They will become Generally Available in the near future.

## Properties

`GroupName` - (string, Required) Friendly name for the service group.

`Template` - (string, Required)  Identifier of an instance template.

`Capacity` - (int, Optional) Number of instances to launch and monitor.


## See Also

* [triton_service_group](https://www.terraform.io/docs/providers/triton/r/service_group.html) in the _Terraform Provider Documentation_