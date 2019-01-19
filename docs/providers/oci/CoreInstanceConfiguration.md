# Terraform::OCI::CoreInstanceConfiguration

This resource provides the Instance Configuration resource in Oracle Cloud Infrastructure Core service.

Creates an instance configuration

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The OCID of the compartment.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the volume backup.

`IsReadOnly` - Whether the attachment should be created in read-only mode.

`Type` - The type can be one of these values: `volume`, `volumeBackup`.

`UseChap` - Whether to use CHAP authentication for the volume attachment. Defaults to false.

`AvailabilityDomain` - The availability domain of the instance.  Example: `Uocm:PHX-AD-1`.

`BackupPolicyId` - If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.

`SizeInGbs` - The size of the volume in GBs.

`SourceDetails` - Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.

`VolumeId` - The OCID of the volume.

`InstanceType` - The type of instance details. Supported instanceType is compute.

`CreateVnicDetails` - Details for creating a new VNIC.

`ExtendedMetadata` - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`IpxeScript` - This is an advanced option.

`Metadata` - Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

`Shape` - The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

`BootVolumeId` - The OCID of the boot volume used to boot the instance.

`ImageId` - The OCID of the image used to boot the instance.

`SourceType` - The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

`NicIndex` - Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`TimeCreated` - The date and time the instance configuration was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_instance_configuration](https://www.terraform.io/docs/providers/oci/r/core_instance_configuration.html) in the _Terraform Provider Documentation_