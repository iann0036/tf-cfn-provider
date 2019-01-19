# Terraform::UCloud::Instance

Provides an UHost Instance resource.

## Properties

TBC

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