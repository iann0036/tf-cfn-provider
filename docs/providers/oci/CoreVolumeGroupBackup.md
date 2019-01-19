# Terraform::OCI::CoreVolumeGroupBackup

This resource provides the Volume Group Backup resource in Oracle Cloud Infrastructure Core service.

Creates a new backup volume group of the specified volume group.
For more information, see [Volume Groups](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment that contains the volume group backup.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name for the volume group backup. Does not have to be unique and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the volume group backup.

`SizeInGbs` - The aggregate size of the volume group backup, in GBs.

`SizeInMbs` - The aggregate size of the volume group backup, in MBs.

`State` - The current state of a volume group backup.

`TimeCreated` - The date and time the volume group backup was created. This is the time the actual point-in-time image of the volume group data was taken. Format defined by RFC3339.

`TimeRequestReceived` - The date and time the request to create the volume group backup was received. Format defined by RFC3339.

`Type` - The type of backup.

`UniqueSizeInGbs` - The aggregate size used by the volume group backup, in GBs.  It is typically smaller than `size_in_gbs`, depending on the space consumed on the volume group and whether the volume backup is full or incremental.

`UniqueSizeInMbs` - The aggregate size used by the volume group backup, in MBs.  It is typically smaller than `size_in_mbs`, depending on the space consumed on the volume group and whether the volume backup is full or incremental.

`VolumeBackupIds` - OCIDs for the volume backups in this volume group backup.

`VolumeGroupId` - The OCID of the source volume group.

## See Also

* [oci_core_volume_group_backup](https://www.terraform.io/docs/providers/oci/r/core_volume_group_backup.html) in the _Terraform Provider Documentation_