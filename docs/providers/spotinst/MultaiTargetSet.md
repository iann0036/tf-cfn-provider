# Terraform::Spotinst::MultaiTargetSet

Provides a Spotinst Multai Target Set.

## Properties

`Name` - (Required) The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

`BalancerId` - (Required) The id of the balancer.

`DeploymentId` - (Required) The id of the deployment.

`Protocol` - (Required) The protocol to allow connections to the target.

`Weight` - (Required) Defines how traffic is distributed between the Target Set.

`Protocol` - (Required) The protocol to allow connections to the target for the health check.

`Path` - (Required) The path to perform the health check.

`Port` - (Required) The port on which the load balancer is listening.

`Interval` - (Required) The interval for the health check.

`Timeout` - (Required) The time out for the health check.

`HealthyThreshold` - (Required) Total number of allowed healthy Targets.

`UnhealthyThreshold` - (Required) Total number of allowed unhealthy Targets.

`Tags` - (Optional) A list of key:value paired tags.

`Key` - (Required) The tag's key.

`Value` - (Required) The tag's value.


## See Also

* [spotinst_multai_target_set](https://www.terraform.io/docs/providers/spotinst/r/multai_target_set.html) in the _Terraform Provider Documentation_