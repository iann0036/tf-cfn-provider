# Terraform::UCloud::Instance

Provides an UHost Instance resource.

## Properties

`AvailabilityZone` - (Required) Availability zone where instance is located. such as: `cn-bj-02`. You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist).

`ImageId` - (Required) The ID for the image to use for the instance.

`RootPassword` - (Required) The password for the instance, which contains 8-30 characters, and at least 3 items of capital letters, lower case letters, numbers and special characters. The special characters include <code>`()~!@#$%^&*-+=_|{}\[]:;'<>,.?/</code>. Note: When it is changed, the instance will reboot to make the change take effect.

`InstanceType` - (Required) The type of instance. There are two types, one is defined by UCloud provider: `n-Type-CPU`(eg:`n-highcpu-2`), thereinto, `Type` can be `highcpu`, `basic`, `standard`, `highmem` which represent the ratio of CPU and memory respectively (1:1, 1:2, 1:4, 1:8). The other is defined Customized: `n-customized-CPU-Memory`(eg:`n-customized-1-3`). Be attention, if the type can be defined by `n-Type-CPU`, another type will not be allowed. In addition, range of CPU in core: 1-32, range of memory in MB: 1-256. When it is changed, the instance will reboot to make the change take effect.

`BootDiskSize` - (Optional) The size of the boot disk, measured in GB (GigaByte). Range: 20-100. The value set of disk size must be larger or equal to `20`(default: `20`) for Linux and `40` (default: `40`) for Windows. The responsive time is a bit longer if the value set is larger than default for local boot disk, and further settings may be required on host instance if the value set is larger than default for cloud boot disk. The disk volume adjustment must be a multiple of 10 GB. When it is changed, the instance will reboot to make the change take effect. In addition, any reduction of boot disk size is not supported.

`BootDiskType` - (Optional) The type of boot disk. Possible values are: `local_normal` and `local_ssd` for local boot disk, `cloud_normal` and `cloud_ssd` for cloud boot disk. (Default: `local_normal`). The `local_ssd`, `cloud_normal` and `cloud_ssd` are not supported in all regions as boot disk type, please proceed to UCloud console for more details.

`DataDiskType` - (Optional) The type of local data disk. Possible values are: `local_normal` and `local_ssd` for local data disk. (Default: `local_normal`). The `local_ssd` is not supported in all regions as disk type, please proceed to UCloud console for more details.

`DataDiskSize` - (Optional) The size of data disk, measured in GB (GigaByte), range: 0-8000 (Default: `20`), 0-8000 for cloud disk, 0-2000 for local sata disk and 100-1000 for local ssd disk (all the GPU type instances are included). The volume adjustment must be a multiple of 10 GB. When it is changed, the instance will reboot to make the change take effect. In addition, any reduction of data disk size is not supported.

`ChargeType` - (Optional) The charge type of instance, possible values are: `year`, `month` and `dynamic` as pay by hour (specific permission required). (Default: `month`).

`Duration` - (Optional) The duration that you will buy the instance (Default: `1`). The value is `0` when pay by month and the instance will be vaild till the last day of that month. It is not required when `dynamic` (pay by hour).

`Name` - (Optional) The name of instance, which contains 1-63 characters and only support Chinese, English, numbers, '-', '_', '.'. If not specified, terraform will autogenerate a name beginning with `tf-instance`.

`Remark` - (Optional) The remarks of instance. (Default: `""`).

`SecurityGroup` - (Optional) The ID of the associated security group.

`SubnetId` - (Optional) The ID of subnet.

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

`VpcId` - (Optional) The ID of VPC linked to the instance.


## Return Values

### Fn::GetAtt

`AutoRenew` - Whether to renew an instance automatically or not.

`Cpu` - The number of cores of virtual CPU, measureed in core.

`Memory` - The size of memory, measured in MB (Megabyte).

`CreateTime` - The time of creation for instance, formatted in RFC3339 time string.

`ExpireTime` - The expiration time for instance, formatted in RFC3339 time string.

`Status` - Instance current status. Possible values are `Initializing`, `starting`, `Running`, `Stopping`, `Stopped`, `Install Fail`, `ResizeFail` and `Rebooting`.

`IpSet` - It is a nested type which documented below.

`DiskSet` - It is a nested type which documented below.

`Id` - The ID of disk.

`Size` - The size of disk, measured in GB (Gigabyte).

`Type` - The type of disk.

`IsBoot` - Specifies whether boot disk or not.

`InternetType` - Type of Elastic IP routes. Possible values are: `International` as internaltional BGP IP, `BGP` as china BGP IP and `Private` as private IP.

`Ip` - Elastic IP address.

## See Also

* [ucloud_instance](https://www.terraform.io/docs/providers/ucloud/r/instance.html) in the _Terraform Provider Documentation_