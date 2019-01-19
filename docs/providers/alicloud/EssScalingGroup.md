# Terraform::Alicloud::EssScalingGroup

Provides a ESS scaling group resource which is a collection of ECS instances with the same application scenarios.

It defines the maximum and minimum numbers of ECS instances in the group, and their associated Server Load Balancer instances, RDS instances, and other attributes.

~> **NOTE:** You can launch an ESS scaling group for a VPC network via specifying parameter `vswitch_ids`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The scaling group ID.

`MinSize` - The minimum number of ECS instances.

`MaxSize` - The maximum number of ECS instances.

`ScalingGroupName` - The name of the scaling group.

`DefaultCooldown` - The default cool-down of the scaling group.

`RemovalPolicies` - The removal policy used to select the ECS instance to remove from the scaling group.

`DbInstanceIds` - The db instances id which the ECS instance attached to.

`LoadbalancerIds` - The slb instances id which the ECS instance attached to.

`VswitchIds` - The vswitches id in which the ECS instance launched.

## See Also

* [alicloud_ess_scaling_group](https://www.terraform.io/docs/providers/alicloud/r/ess_scaling_group.html) in the _Terraform Provider Documentation_