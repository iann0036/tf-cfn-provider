# Terraform::OCI::CoreVolumeGroup

This resource provides the Volume Group resource in Oracle Cloud Infrastructure Core service.

Creates a new volume group in the specified compartment.
A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing
volume group, or by restoring a volume group backup. A volume group can contain up to 64 volumes.
You may optionally specify a *display name* for the volume group, which is simply a friendly name or
description. It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information, see [Volume Groups](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).

## Properties

`AvailabilityDomain` - (Required) The availability domain of the volume group.

`CompartmentId` - (Required) The OCID of the compartment that contains the volume group.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name for the volume group. Does not have to be unique, and it's changeable.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`SourceDetails` - (Required) Specifies the volume group source details for a new volume group. The volume source is either another a list of volume ids in the same availability domain, another volume group or a volume group backup.
* `Type` - (Required) The type can be one of these values: `volumeGroupBackupId`, `volumeGroupId`, `volumeIds`
* `VolumeGroupBackupId` - (Required when type=volumeGroupBackupId) The OCID of the volume group backup to restore from.
* `VolumeGroupId` - (Required when type=volumeGroupId) The OCID of the volume group to clone from.
* `VolumeIds` - (Required when type=volumeIds) OCIDs for the volumes in this volume group.

`Type` - (Required) The type can be one of these values: `volumeGroupBackupId`, `volumeGroupId`, `volumeIds`
* `VolumeGroupBackupId` - (Required when type=volumeGroupBackupId) The OCID of the volume group backup to restore from.
* `VolumeGroupId` - (Required when type=volumeGroupId) The OCID of the volume group to clone from.
* `VolumeIds` - (Required when type=volumeIds) OCIDs for the volumes in this volume group.

`VolumeGroupBackupId` - (Required when type=volumeGroupBackupId) The OCID of the volume group backup to restore from.
* `VolumeGroupId` - (Required when type=volumeGroupId) The OCID of the volume group to clone from.
* `VolumeIds` - (Required when type=volumeIds) OCIDs for the volumes in this volume group.

`VolumeGroupId` - (Required when type=volumeGroupId) The OCID of the volume group to clone from.
* `VolumeIds` - (Required when type=volumeIds) OCIDs for the volumes in this volume group.

`VolumeIds` - (Required when type=volumeIds) OCIDs for the volumes in this volume group.


## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The availability domain of the volume group.

`DisplayName` - A user-friendly name for the volume group. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`VolumeGroupId` - The OCID of the volume group to clone from.

`CompartmentId` - The OCID of the compartment that contains the volume group.

`State` - The current state of a volume group.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`VolumeGroupBackupId` - The OCID of the volume group backup to restore from.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`TimeCreated` - The date and time the volume group was created. Format defined by RFC3339.

`SourceDetails` - The volume group source. The source is either another a list of volume IDs in the same availability domain, another volume group, or a volume group backup.

`SizeInGbs` - The aggregate size of the volume group in GBs.

`VolumeIds` - OCIDs for the volumes in this volume group.

`SizeInMbs` - The aggregate size of the volume group in MBs.

`IsHydrated` - Specifies whether the newly created cloned volume group's data has finished copying from the source volume group or backup.

`Type` - The type can be one of these values: `volumeGroupBackupId`, `volumeGroupId`, `volumeIds`.

`Id` - The OCID for the volume group.

## See Also

* [oci_core_volume_group](https://www.terraform.io/docs/providers/oci/r/core_volume_group.html) in the _Terraform Provider Documentation_