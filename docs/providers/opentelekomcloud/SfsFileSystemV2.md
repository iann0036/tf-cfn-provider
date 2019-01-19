# Terraform::OpenTelekomCloud::SfsFileSystemV2

Provides an Shared File System (SFS) resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The UUID of the shared file system.

`Status` - The status of the shared file system.

`ShareType` - The storage service type assigned for the shared file system, such as high-performance storage (composed of SSDs) and large-capacity storage (composed of SATA disks).

`VolumeType` - The volume type.

`ExportLocation` - The address for accessing the shared file system.

`Host` - The host name of the shared file system.

`ShareAccessId` - The UUID of the share access rule.

`AccessRulesStatus` - The status of the share access rule.

## See Also

* [opentelekomcloud_sfs_file_system_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_file_system_v2.html) in the _Terraform Provider Documentation_