# Terraform::Triton::InstanceTemplate

The `Terraform::Triton::InstanceTemplate` resource represents a Triton Service Group instance template.

~> **NOTE:**  Triton Service Groups are in Preview and only supported in specific regions at this time. They will become Generally Available in the near future.

## Properties

`TemplateName` - (string, Required) Friendly name for the instance template.

`Image` - (string, Required)  UUID of the image.

`Package` - (string, Required) Package name used for provisioning.

`FirewallEnabled` - (boolean, Optional) Whether to enable the firewall for group instances. Default is `false`.

`Tags` - (map, Optional) Tags for group instances.

`Networks` - (list, Optional) Network IDs for group instances.

`Metadata` - (map, Optional) Metadata for group instances.

`Userdata` - (string, Optional) Data copied to instance on boot.


## See Also

* [triton_instance_template](https://www.terraform.io/docs/providers/triton/r/instance_template.html) in the _Terraform Provider Documentation_