# Terraform::TencentCloud::CbsStorage

Provides a CBS resource.

~> **NOTE:** At present, only 'PREPAID' storage is supported to create. 'PREPAID' storage cannot be deleted, once created, must wait it to be expired and release it automatically.

## Properties

`StorageType` - (Required) Type of CBS medium. cloudBasic refers to a HDD cloud storage, cloudPremium refers to a Premium cloud storage, cloudSSD refers to a SSD cloud storage. **NOTE**, `StorageType` do not support modification.

`StorageSize` - (Required) Size of the storage (GB). The value range is 10GB - 4,000GB (HDD cloud storages), 500GB - 4,000GB (Premium cloud storages), 100GB - 4,000GB (SSD cloud storages). The increment is 10GB. **NOTE**,  `StorageSize` do not support modification.

`Period` - (Required) The tenancy (time unit is month) of the perpaid storage, the legal values are [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60]. **NOTE**, `Period` do not support modification.

`AvailabilityZone` - (Required) The available zone that the CBS instance locates at. **NOTE**, `AvailabilityZone` do not support modification.

`StorageName` - (Optional) The name of the CBS. This storage_name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_". If not specified, the default name is `CBS-Instance`. It is supported to modify `StorageName` after the storage is created.

`SnapshotId` - (Optional) For a new storage, this indicate which snapshot to use to create the new storage. **For a exist storage, change this field whill case a rollback operation: your storage will rollback to the moment the snapshot created, your must change this filed carefully, please ensure your data in this storage is saved or out of use.**.


## Return Values

### Fn::GetAtt

`Id` - The storage ID, something looks like `disk-xxxxxx`.

`StorageType` - Type of CBS medium.

`StorageSize` - Size of the storage.

`Period` - The tenancy of the storage.

`AvailabilityZone` - The available zone that the CBS instance.

`StorageStatus` - The status of storage. The standard values are as follows, normal: Normal, toRecycle: To be terminated, attaching: Mounting, detaching: Unmounting.

`Attached` - The attach status of storage. 1 indicates that storage has been mounted, 0 indicates the storage unmounted.

## See Also

* [tencentcloud_cbs_storage](https://www.terraform.io/docs/providers/tencentcloud/r/cbs_storage.html) in the _Terraform Provider Documentation_