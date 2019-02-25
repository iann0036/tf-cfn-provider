# Terraform::Spotinst::MultaiTarget

Provides a Spotinst Multai Target.

## Properties

`BalancerId` - (Required) The ID of the balancer.

`TargetSetId` - (Required) The ID of the target set.

`Name` - (Required) The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

`Port` - (Required) The port the target will register to.

`Host` - (Required) The address (IP or URL) of the targets to register.

`Weight` - (Required) Defines how traffic is distributed between targets.

`Tags` - (Optional) A list of key:value paired tags.

`Key` - (Required) The tag's key.

`Value` - (Required) The tag's value.


## See Also

* [spotinst_multai_target](https://www.terraform.io/docs/providers/spotinst/r/multai_target.html) in the _Terraform Provider Documentation_