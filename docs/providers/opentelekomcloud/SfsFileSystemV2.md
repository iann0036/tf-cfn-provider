# Terraform::OpenTelekomCloud::SfsFileSystemV2

Provides an Shared File System (SFS) resource.

## Properties

`Size` - (Required) The size (GB) of the shared file system.

`ShareProto` - (Optional) The protocol for sharing file systems. The default value is NFS.

`Name` - (Optional) The name of the shared file system.

`Description` - (Optional) Describes the shared file system.

`IsPublic` - (Optional) The level of visibility for the shared file system.

`Metadata` - (Optional) Metadata key and value pairs as a dictionary of strings.Changing this will create a new resource.

`AvailabilityZone` - (Optional) The availability zone name.Changing this parameter will create a new resource.

`AccessLevel` - (Required) The access level of the shared file system. Changing this will create a new access rule.

`AccessType` - (Optional) The type of the share access rule. Changing this will create a new access rule.

`AccessTo` - (Required) The access that the back end grants or denies. Changing this will create a new access rule.


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