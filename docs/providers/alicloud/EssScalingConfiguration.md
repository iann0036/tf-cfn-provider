# Terraform::Alicloud::EssScalingConfiguration

Provides a ESS scaling configuration resource.

~> **NOTE:** Several instance types have outdated in some regions and availability zones, such as `ecs.t1.*`, `ecs.s2.*`, `ecs.n1.*` and so on. If you want to keep them, you should set `is_outdated` to true. For more about the upgraded instance type, refer to `alicloud_instance_types` datasource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The scaling configuration ID.

`Active` - Wether the current scaling configuration is actived.

`ImageId` - The ecs instance Image id.

`InstanceType` - The ecs instance type.

`SecurityGroupId` - ID of the security group to which a newly created instance belongs.

`ScalingConfigurationName` - Name of scaling configuration.

`InternetChargeType` - Internet charge type of ecs instance.

`KeyName` - The name of key pair that has been bound in ECS instance.

`RoleName` - The name of RAM role that has been bound in ECS instance.

`UserData` - The hash value of the user data.

`ForceDelete` - Whether delete the last scaling configuration forcibly with deleting its scaling group.

`Tags` - The scaling instance tags, use jsonencode(item) to display the value.

`InstanceName` - The ecs instance name.

## See Also

* [alicloud_ess_scaling_configuration](https://www.terraform.io/docs/providers/alicloud/r/ess_scaling_configuration.html) in the _Terraform Provider Documentation_