# Terraform::Alicloud::EssScalingConfiguration

Provides a ESS scaling configuration resource.

~> **NOTE:** Several instance types have outdated in some regions and availability zones, such as `ecs.t1.*`, `ecs.s2.*`, `ecs.n1.*` and so on. If you want to keep them, you should set `IsOutdated` to true. For more about the upgraded instance type, refer to `Terraform::Alicloud::InstanceTypes` datasource.

## Properties

`ScalingGroupId` - (Required) ID of the scaling group of a scaling configuration.

`ImageId` - (Required) ID of an image file, indicating the image resource selected when an instance is enabled.

`InstanceType` - (Required) Resource type of an ECS instance.

`InstanceName` - (Optional) Name of an ECS instance. Default to "ESS-Instance". It is valid from version 1.7.1.

`IoOptimized` - (Deprecated) It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.

`IsOutdated` - (Optional) Whether to use outdated instance type. Default to false.

`SecurityGroupId` - (Required) ID of the security group to which a newly created instance belongs.

`ScalingConfigurationName` - (Optional) Name shown for the scheduled task. If this parameter value is not specified, the default value is ScalingConfigurationId.

`InternetChargeType` - (Optional) Network billing type, Values: PayByBandwidth or PayByTraffic. Default to `PayByBandwidth`.

`InternetMaxBandwidthIn` - (Optional) Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].

`InternetMaxBandwidthOut` - (Optional) Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].

`SystemDiskCategory` - (Optional) Category of the system disk. The parameter value options are `cloud_efficiency`, `cloud_ssd` and `cloud`. `cloud` only is used to some no I/O optimized instance. Default to `cloud_efficiency`.

`SystemDiskSize` - (Optional) Size of system disk, in GiB. Optional values: cloud: 40-500, cloud_efficiency: 40-500, cloud_ssd: 40-500, ephemeral_ssd: 40-500 The default value is {40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.

`Enable` - (Optional) Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.

`Active` - (Optional) Whether active current scaling configuration in the specified scaling group. Default to `false`.

`Substitute` - (Optional) The another scaling configuration which will be active automatically and replace current configuration when setting `Active` to 'false'. It is invalid when `Active` is 'true'.

`UserData` - (Optional) User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.

`KeyName` - (Optional) The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.

`RoleName` - (Optional) Instance RAM role name. The name is provided and maintained by RAM. You can use `Terraform::Alicloud::RamRole` to create a new one.

`ForceDelete` - (Optional) The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.

`DataDisk` - (Optional) DataDisk mappings to attach to ecs instance. See [Block datadisk](#block-datadisk) below for details.

`InstanceIds` - (Deprecated) It has been deprecated from version 1.6.0. New resource `Terraform::Alicloud::EssAttachment` replaces it.

`Tags` - (Optional) A mapping of tags to assign to the resource. It will be applied for ECS instances finally.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "http://", or "https://" It can be a null string.


## Return Values

### Fn::GetAtt

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