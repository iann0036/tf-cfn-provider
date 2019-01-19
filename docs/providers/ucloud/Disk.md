# Terraform::UCloud::Disk

Provides a Cloud Disk resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation of disk, formatted in RFC3339 time string.

`ExpireTime` - The expiration time of disk, formatted in RFC3339 time string.

`Status` -  The status of disk. Possible values are: `Available`, `InUse`, `Detaching`, `Initializating`, `Failed`, `Cloning`, `Restoring`, `RestoreFailed`.

## See Also

* [ucloud_disk](https://www.terraform.io/docs/providers/ucloud/r/disk.html) in the _Terraform Provider Documentation_