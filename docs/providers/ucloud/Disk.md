# Terraform::UCloud::Disk

Provides a Cloud Disk resource.

## Properties

`AvailabilityZone` - (Required) The Zone to create the disk in.

`DiskSize` - (Required) Purchase the size of disk in GB. 1-8000 for a cloud disk, 1-4000 for SSD cloud disk.

`Name` - (Optional)  The name of disk, should have 6-63 characters and only support Chinese, English, numbers, '-', '_'. If not specified, terraform will autogenerate a name beginning with `tf-disk`.

`DiskType` - (Optional) The type of disk. Possible values are: `data_disk`as cloud disk, `ssd_data_disk` as ssd cloud disk. (Default: `data_disk`).

`ChargeType` - (Optional) Charge type of disk. Possible values are: `year` as pay by year, `month` as pay by month, `dynamic` as pay by hour. (Default: `month`).

`Duration` - (Optional) The duration that you will buy the resource. (Default: `1`). It is not required when `dynamic` (pay by hour), the value is `0` when `month`(pay by month) and the disk will be vaild till the last day of that month.

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).


## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation of disk, formatted in RFC3339 time string.

`ExpireTime` - The expiration time of disk, formatted in RFC3339 time string.

`Status` -  The status of disk. Possible values are: `Available`, `InUse`, `Detaching`, `Initializating`, `Failed`, `Cloning`, `Restoring`, `RestoreFailed`.

## See Also

* [ucloud_disk](https://www.terraform.io/docs/providers/ucloud/r/disk.html) in the _Terraform Provider Documentation_