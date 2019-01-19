# Terraform::OCI::CoreBootVolume

This resource provides the Boot Volume resource in Oracle Cloud Infrastructure Core service.

Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup.
For general information about boot volumes, see [Boot Volumes](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm).
You may optionally specify a *display name* for the volume, which is simply a friendly name or
description. It does not have to be unique, and you can change it. Avoid entering confidential information.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailabilityDomain` - The availability domain of the boot volume.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - The OCID of the compartment that contains the boot volume.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the boot volume or boot volume backup.

`ImageId` - The image OCID used to create the boot volume.

`IsHydrated` - Specifies whether the boot volume's data has finished copying from the source boot volume or boot volume backup.

`KmsKeyId` - The OCID of the KMS key which is the master encryption key for the boot volume.

`SizeInGbs` - The size of the boot volume in GBs.

`SizeInMbs` - The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Please use `size_in_gbs`.

`SourceDetails` - The boot volume source, either an existing boot volume in the same availability domain or a boot volume backup. If null, this means that the boot volume was created from an image.

`Type` - The type can be one of these values: `bootVolume`, `bootVolumeBackup`.

`State` - The current state of a boot volume.

`TimeCreated` - The date and time the boot volume was created. Format defined by RFC3339.

`VolumeGroupId` - The OCID of the source volume group.

## See Also

* [oci_core_boot_volume](https://www.terraform.io/docs/providers/oci/r/core_boot_volume.html) in the _Terraform Provider Documentation_