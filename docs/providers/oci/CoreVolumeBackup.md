# Terraform::OCI::CoreVolumeBackup

This resource provides the Volume Backup resource in Oracle Cloud Infrastructure Core service.

Creates a new backup of the specified volume. For general information about volume backups,
see [Overview of Block Volume Service Backups](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm)

When the request is received, the backup object is in a REQUEST_RECEIVED state.
When the data is imaged, it goes into a CREATING state.
After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

## Properties

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Type` - (Optional) The type of backup to create. If omitted, defaults to INCREMENTAL.

`VolumeId` - (Required) The OCID of the volume that needs to be backed up.

`SourceDetails` - (Optional) Details of the volume backup source in the cloud. * `Region` - The region of the volume backup source. * `VolumeBackupId` - The OCID of the source volume backup.

`Region` - The region of the volume backup source. * `VolumeBackupId` - The OCID of the source volume backup.

`VolumeBackupId` - The OCID of the source volume backup.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment that contains the volume backup.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.

`ExpirationTime` - The date and time the volume backup will expire and be automatically deleted. Format defined by RFC3339. This parameter will always be present for backups that were created automatically by a scheduled-backup policy. For manually created backups, it will be absent, signifying that there is no expiration time and the backup will last forever until manually deleted.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the volume backup.

`SizeInGbs` - The size of the volume, in GBs.

`SizeInMbs` - The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Please use `size_in_gbs`.

`SourceType` - Specifies whether the backup was created manually, or via scheduled backup policy.

`SourceVolumeBackupId` - The OCID of the source volume backup.

`State` - The current state of a volume backup.

`TimeCreated` - The date and time the volume backup was created. This is the time the actual point-in-time image of the volume data was taken. Format defined by RFC3339.

`TimeRequestReceived` - The date and time the request to create the volume backup was received. Format defined by RFC3339.

`Type` - The type of a volume backup. Supported values are 'FULL' or 'INCREMENTAL'.

`UniqueSizeInGbs` - The size used by the backup, in GBs. It is typically smaller than `size_in_gbs`, depending on the space consumed on the volume and whether the backup is full or incremental.

`UniqueSizeInMbs` - The size used by the backup, in MBs. It is typically smaller than `size_in_mbs`, depending on the space consumed on the volume and whether the backup is full or incremental. This field is deprecated. Please use `unique_size_in_gbs`.

`VolumeId` - The OCID of the volume.

## See Also

* [oci_core_volume_backup](https://www.terraform.io/docs/providers/oci/r/core_volume_backup.html) in the _Terraform Provider Documentation_