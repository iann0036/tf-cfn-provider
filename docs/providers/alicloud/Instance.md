# Terraform::Alicloud::Instance

Provides a ECS instance resource.

~> **NOTE:** You can launch an ECS instance for a VPC network via specifying parameter `vswitch_id`. One instance can only belong to one VSwitch.

~> **NOTE:** If a VSwitchId is specified for creating an instance, SecurityGroupId and VSwitchId must belong to one VPC.

~> **NOTE:** Several instance types have outdated in some regions and availability zones, such as `ecs.t1.*`, `ecs.s2.*`, `ecs.n1.*` and so on. If you want to keep them, you should set `is_outdated` to true. For more about the upgraded instance type, refer to `alicloud_instance_types` datasource.

~> **NOTE:** At present, 'PrePaid' instance cannot be deleted and must wait it to be outdated and release it automatically.

~> **NOTE:** The resource supports modifying instance charge type from 'PrePaid' to 'PostPaid' from version 1.9.6.
 However, at present, this modification has some limitation about CPU core count in one month, so strongly recommand that `Don't modify instance charge type frequentlly in one month`.

## Properties

TBC

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