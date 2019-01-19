# Terraform::TencentCloud::CbsStorage

Provides a CBS resource.

~> **NOTE:** At present, only 'PREPAID' storage is supported to create. 'PREPAID' storage cannot be deleted, once created, must wait it to be expired and release it automatically.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The storage ID, something looks like `disk-xxxxxx`.

`StorageType` - Type of CBS medium.

`StorageSize` - Size of the storage.

`Period` - The tenancy of the storage.

`AvailabilityZone` - The available zone that the CBS instance.

`StorageStatus` - The status of storage. The standard values are as follows, normal: Normal, toRecycle: To be terminated, attaching: Mounting, detaching: Unmounting.

`Attached` - The attach status of storage. 1 indicates that storage has been mounted, 0 indicates the storage unmounted.

## See Also

* [tencentcloud_cbs_storage](https://www.terraform.io/docs/providers/tencentcloud/r/cbs_storage.html) in the _Terraform Provider Documentation_