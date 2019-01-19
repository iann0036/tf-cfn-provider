# Terraform::Alicloud::Instance

Provides a ECS instance resource.

~> **NOTE:** You can launch an ECS instance for a VPC network via specifying parameter `VswitchId`. One instance can only belong to one VSwitch.

~> **NOTE:** If a VSwitchId is specified for creating an instance, SecurityGroupId and VSwitchId must belong to one VPC.

~> **NOTE:** Several instance types have outdated in some regions and availability zones, such as `ecs.t1.*`, `ecs.s2.*`, `ecs.n1.*` and so on. If you want to keep them, you should set `IsOutdated` to true. For more about the upgraded instance type, refer to `Terraform::Alicloud::InstanceTypes` datasource.

~> **NOTE:** At present, 'PrePaid' instance cannot be deleted and must wait it to be outdated and release it automatically.

~> **NOTE:** The resource supports modifying instance charge type from 'PrePaid' to 'PostPaid' from version 1.9.6.
 However, at present, this modification has some limitation about CPU core count in one month, so strongly recommand that `Don't modify instance charge type frequentlly in one month`.

## Properties

`ImageId` - (Required) The Image to use for the instance. ECS instance's image can be replaced via changing 'image_id'. When it is changed, the instance will reboot to make the change take effect.

`InstanceType` - (Required) The type of instance to start.

`IoOptimized` - (Deprecated) It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.

`IsOutdated` - (Optional) Whether to use outdated instance type. Default to false.

`SecurityGroups` - (Required)  A list of security group ids to associate with.

`AvailabilityZone` - (Optional) The Zone to start the instance in. It is ignored and will be computed when set `VswitchId`.

`InstanceName` - (Optional) The name of the ECS. This instance_name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://. If not specified, Terraform will autogenerate a default name is `ECS-Instance`.

`AllocatePublicIp` - (Deprecated) It has been deprecated from version "1.7.0". Setting "internet_max_bandwidth_out" larger than 0 can allocate a public ip address for an instance.

`SystemDiskCategory` - (Optional) Valid values are `cloud_efficiency`, `cloud_ssd` and `cloud`. `cloud` only is used to some none I/O optimized instance. Default to `cloud_efficiency`.

`SystemDiskSize` - (Optional) Size of the system disk, measured in GiB. Value range: [20, 500]. The specified value must be equal to or greater than max{20, Imagesize}. Default value: max{40, ImageSize}. ECS instance's system disk can be reset when replacing system disk.

`Description` - (Optional, Force New) The description of the data disk.

`InternetChargeType` - (Optional) Internet charge type of the instance, Valid values are `PayByBandwidth`, `PayByTraffic`. Default is `PayByTraffic`. At present, 'PrePaid' instance cannot change the value to "PayByBandwidth" from "PayByTraffic".

`InternetMaxBandwidthIn` - (Optional) Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). Value range: [1, 200]. If this value is not specified, then automatically sets it to 200 Mbps.

`InternetMaxBandwidthOut` - (Optional) Maximum outgoing bandwidth to the public network, measured in Mbps (Mega bit per second). Value range:  [0, 100]. Default to 0 Mbps.

`HostName` - (Optional) Host name of the ECS, which is a string of at least two characters. “hostname” cannot start or end with “.” or “-“. In addition, two or more consecutive “.” or “-“ symbols are not allowed. On Windows, the host name can contain a maximum of 15 characters, which can be a combination of uppercase/lowercase letters, numerals, and “-“. The host name cannot contain dots (“.”) or contain only numeric characters. On other OSs such as Linux, the host name can contain a maximum of 30 characters, which can be segments separated by dots (“.”), where each segment can contain uppercase/lowercase letters, numerals, or “_“. When it is changed, the instance will reboot to make the change take effect.

`Password` - (Optional) Password to an instance is a string of 8 to 30 characters. It must contain uppercase/lowercase letters and numerals, but cannot contain special symbols. When it is changed, the instance will reboot to make the change take effect.

`VswitchId` - (Optional) The virtual switch ID to launch in VPC. This parameter must be set unless you can create classic network instances.

`InstanceChargeType` - (Optional) Valid values are `PrePaid`, `PostPaid`, The default is `PostPaid`.

`PeriodUnit` - (Optional) The duration unit that you will buy the resource. It is valid when `InstanceChargeType` is 'PrePaid'. Valid value: ["Week", "Month"]. Default to "Month".

`Period` - (Optional) The duration that you will buy the resource, in month. It is valid when `InstanceChargeType` is `PrePaid`. Default to 1. Valid values: - [1-9, 12, 24, 36, 48, 60] when `PeriodUnit` in "Month" - [1-3] when `PeriodUnit` in "Week".

`RenewalStatus` - (Optional) Whether to renew an ECS instance automatically or not. It is valid when `InstanceChargeType` is `PrePaid`. Default to "Normal". Valid values: - `AutoRenewal`: Enable auto renewal. - `Normal`: Disable auto renewal. - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.

`AutoRenewPeriod` - (Optional) Auto renewal period of an instance, in the unit of month. It is valid when `InstanceChargeType` is `PrePaid`. Default to 1. Valid value: - [1, 2, 3, 6, 12] when `PeriodUnit` in "Month" - [1, 2, 3] when `PeriodUnit` in "Week".

`Tags` - (Optional) A mapping of tags to assign to the resource. - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string. - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

`UserData` - (Optional) User-defined data to customize the startup behaviors of an ECS instance and to pass data into an ECS instance.

`KeyName` - (Optional, Force new resource) The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.

`RoleName` - (Optional, Force new resource) Instance RAM role name. The name is provided and maintained by RAM. You can use `Terraform::Alicloud::RamRole` to create a new one.

`IncludeDataDisks` - (Optional) Whether to change instance disks charge type when changing instance charge type.

`DryRun` - (Optional) Whether to pre-detection. When it is true, only pre-detection and not actually modify the payment type operation. It is valid when `InstanceChargeType` is 'PrePaid'. Default to false.

`PrivateIp` - (Optional) Instance private IP address can be specified when you creating new instance. It is valid when `VswitchId` is specified.

`SpotStrategy` - (Optional, Force New) The spot strategy of a Pay-As-You-Go instance, and it takes effect only when parameter `InstanceChargeType` is 'PostPaid'. Value range: - NoSpot: A regular Pay-As-You-Go instance. - SpotWithPriceLimit: A price threshold for a spot instance - SpotAsPriceGo: A price that is based on the highest Pay-As-You-Go instance.

`SpotPriceLimit` - (Optional, Float, Force New) The hourly price threshold of a instance, and it takes effect only when parameter 'spot_strategy' is 'SpotWithPriceLimit'. Three decimals is allowed at most.

`DeletionProtection` - (Optional, true, force New) Whether enable the deletion protection or not. - true: Enable deletion protection. - false: Disable deletion protection.

`ForceDelete` - (Optional, Available 1.18.0+) If it is true, the "PrePaid" instance will be change to "PostPaid" and then deleted forcibly. However, because of changing instance charge type has CPU core count quota limitation, so strongly recommand that "Don't modify instance charge type frequentlly in one month".

`SecurityEnhancementStrategy` - (Optional, Force New) The security enhancement strategy. - Active: Enable security enhancement strategy, it only works on system images. - Deactive: Disable security enhancement strategy, it works on all images.

`DataDisks` - (Optional, Force New, Available 1.23.1+) The list of data disks created with instance. * `Name` - (Optional, Force New) The name of the data disk. * `Size` - (Required, Force New) The size of the data disk. - cloud：[5, 2000] - cloud_efficiency：[20, 32768] - cloud_ssd：[20, 32768] - ephemeral_ssd：[5, 800] * `Category` - (Optional, Force New) The category of the disk: - `cloud`: The general cloud disk. - `cloud_efficiency`: The efficiency cloud disk. - `cloud_ssd`: The SSD cloud disk. - `ephemeral_ssd`: The local SSD disk.

`Name` - (Optional, Force New) The name of the data disk. * `Size` - (Required, Force New) The size of the data disk. - cloud：[5, 2000] - cloud_efficiency：[20, 32768] - cloud_ssd：[20, 32768] - ephemeral_ssd：[5, 800] * `Category` - (Optional, Force New) The category of the disk: - `cloud`: The general cloud disk. - `cloud_efficiency`: The efficiency cloud disk. - `cloud_ssd`: The SSD cloud disk. - `ephemeral_ssd`: The local SSD disk.

`Size` - (Required, Force New) The size of the data disk. - cloud：[5, 2000] - cloud_efficiency：[20, 32768] - cloud_ssd：[20, 32768] - ephemeral_ssd：[5, 800] * `Category` - (Optional, Force New) The category of the disk: - `cloud`: The general cloud disk. - `cloud_efficiency`: The efficiency cloud disk. - `cloud_ssd`: The SSD cloud disk. - `ephemeral_ssd`: The local SSD disk.

`Category` - (Optional, Force New) The category of the disk: - `cloud`: The general cloud disk. - `cloud_efficiency`: The efficiency cloud disk. - `cloud_ssd`: The SSD cloud disk. - `ephemeral_ssd`: The local SSD disk.

`SnapshotId` - (Optional, Force New) The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk. * `DeleteWithInstance` - (Optional, Force New) Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency and cloud_ssd disk. If the category of this data disk was ephemeral_ssd, please don't set this param.

`DeleteWithInstance` - (Optional, Force New) Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency and cloud_ssd disk. If the category of this data disk was ephemeral_ssd, please don't set this param.


## Return Values

### Fn::GetAtt

`Id` - The instance ID.

`AvailabilityZone` - The Zone to start the instance in.

`InstanceName` - The instance name.

`HostName` - The instance host name.

`Description` - The instance description.

`Status` - The instance status.

`ImageId` - The instance Image Id.

`InstanceType` - The instance type.

`PrivateIp` - The instance private ip.

`PublicIp` - The instance public ip.

`VswitchId` - If the instance created in VPC, then this value is  virtual switch ID.

`Tags` - The instance tags, use jsonencode(item) to display the value.

`KeyName` - The name of key pair that has been bound in ECS instance.

`RoleName` - The name of RAM role that has been bound in ECS instance.

`UserData` - The hash value of the user data.

`Period` - The ECS instance using duration.

`PeriodUnit` - The ECS instance using duration unit.

`RenewalStatus` - The ECS instance automatically renew status.

`AutoRenewPeriod` - Auto renewal period of an instance.

`DryRun` - Whether to pre-detection.

`SpotStrategy` - The spot strategy of a Pay-As-You-Go instance.

`SpotPriceLimit` - The hourly price threshold of a instance.

## See Also

* [alicloud_instance](https://www.terraform.io/docs/providers/alicloud/r/instance.html) in the _Terraform Provider Documentation_