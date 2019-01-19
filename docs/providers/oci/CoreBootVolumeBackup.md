# Terraform::OCI::CoreBootVolumeBackup

This resource provides the Boot Volume Backup resource in Oracle Cloud Infrastructure Core service.

Creates a new boot volume backup of the specified boot volume. For general information about boot volume backups,
see [Overview of Boot Volume Backups](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm)

When the request is received, the backup object is in a REQUEST_RECEIVED state.
When the data is imaged, it goes into a CREATING state.
After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`BootVolumeId` - The OCID of the boot volume.

`CompartmentId` - The OCID of the compartment that contains the boot volume backup.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.

`ExpirationTime` - The date and time the volume backup will expire and be automatically deleted. Format defined by RFC3339. This parameter will always be present for backups that were created automatically by a scheduled-backup policy. For manually created backups, it will be absent, signifying that there is no expiration time and the backup will last forever until manually deleted.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the boot volume backup.

`ImageId` - The image OCID used to create the boot volume the backup is taken from.

`SizeInGbs` - The size of the boot volume, in GBs.

`SourceType` - Specifies whether the backup was created manually, or via scheduled backup policy.

`State` - The current state of a boot volume backup.

`TimeCreated` - The date and time the boot volume backup was created. This is the time the actual point-in-time image of the volume data was taken. Format defined by RFC3339.

`TimeRequestReceived` - The date and time the request to create the boot volume backup was received. Format defined by RFC3339.

`Type` - The type of a volume backup. Supported values are 'FULL' or 'INCREMENTAL'.

`UniqueSizeInGbs` - The size used by the backup, in GBs. It is typically smaller than `size_in_gbs`, depending on the space consumed on the boot volume and whether the backup is full or incremental.

## See Also

* [oci_core_boot_volume_backup](https://www.terraform.io/docs/providers/oci/r/core_boot_volume_backup.html) in the _Terraform Provider Documentation_