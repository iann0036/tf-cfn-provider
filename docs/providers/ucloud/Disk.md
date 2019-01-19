# Terraform::UCloud::Disk

Provides a Cloud Disk resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CreateTime` - The time of creation of disk, formatted in RFC3339 time string.

`ExpireTime` - The expiration time of disk, formatted in RFC3339 time string.

`Status` -  The status of disk. Possible values are: `Available`, `InUse`, `Detaching`, `Initializating`, `Failed`, `Cloning`, `Restoring`, `RestoreFailed`.

## See Also

* [ucloud_disk](https://www.terraform.io/docs/providers/ucloud/r/disk.html) in the _Terraform Provider Documentation_