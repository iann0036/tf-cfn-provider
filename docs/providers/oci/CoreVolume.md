# Terraform::OCI::CoreVolume

This resource provides the Volume resource in Oracle Cloud Infrastructure Core service.

Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from
50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB).
For general information about block volumes, see
[Overview of Block Volume Service](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/overview.htm).

A volume and instance can be in separate compartments but must be in the same availability domain.
For information about access control and compartments, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about
availability domains, see [Regions and Availability Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
To get a list of availability domains, use the `ListAvailabilityDomains` operation
in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or
description. It does not have to be unique, and you can change it. Avoid entering confidential information.

## Properties

`AvailabilityDomain` - (Required) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`.

`BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.

`CompartmentId` - (Required) The OCID of the compartment that contains the volume.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`KmsKeyId` - (Optional) (Updatable) The OCID of the KMS key to be used as the master encryption key for the volume.

`SizeInGbs` - (Optional) (Updatable) The size of the volume in GBs.

`SizeInMbs` - (Optional) The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use `SizeInGbs` instead.

`SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Required) The OCID of the volume or volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`.

`Id` - (Required) The OCID of the volume or volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`.

`Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`.

`VolumeBackupId` - (Optional) The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the `SourceDetails` field instead to specify the backup for the volume.


## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The availability domain of the volume.  Example: `Uocm:PHX-AD-1`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`VolumeGroupId` - The OCID of the source volume group.

`CompartmentId` - The OCID of the compartment that contains the volume.

`State` - The current state of a volume.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`KmsKeyId` - The OCID of the KMS key which is the master encryption key for the volume.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`TimeCreated` - The date and time the volume was created. Format defined by RFC3339.

`SourceDetails` - The volume source, either an existing volume in the same availability domain or a volume backup. If null, an empty volume is created.

`SizeInGbs` - The size of the volume in GBs.

`SizeInMbs` - The size of the volume in MBs. This field is deprecated. Use `SizeInGbs` instead.

`IsHydrated` - Specifies whether the cloned volume's data has finished copying from the source volume or backup.

`Type` - The type can be one of these values: `volume`, `volumeBackup`.

`Id` - The OCID of the volume or volume backup.

## See Also

* [oci_core_volume](https://www.terraform.io/docs/providers/oci/r/core_volume.html) in the _Terraform Provider Documentation_