# Terraform::OCI::CoreInstanceConfiguration

This resource provides the Instance Configuration resource in Oracle Cloud Infrastructure Core service.

Creates an instance configuration

## Properties

`CompartmentId` - (Required) The OCID of the compartment containing the instance configuration.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name for the instance configuration.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`InstanceDetails` - (Required)
* `BlockVolumes` - (Optional)
* `AttachDetails` - (Optional)
* `DisplayName` - (Applicable when instance_type=compute) A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
* `IsReadOnly` - (Applicable when instance_type=compute) Whether the attachment should be created in read-only mode.
* `Type` - (Required) The type of volume. The only supported values are "iscsi" and "paravirtualized".
* `UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`BlockVolumes` - (Optional)
* `AttachDetails` - (Optional)
* `DisplayName` - (Applicable when instance_type=compute) A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
* `IsReadOnly` - (Applicable when instance_type=compute) Whether the attachment should be created in read-only mode.
* `Type` - (Required) The type of volume. The only supported values are "iscsi" and "paravirtualized".
* `UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`AttachDetails` - (Optional)
* `DisplayName` - (Applicable when instance_type=compute) A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
* `IsReadOnly` - (Applicable when instance_type=compute) Whether the attachment should be created in read-only mode.
* `Type` - (Required) The type of volume. The only supported values are "iscsi" and "paravirtualized".
* `UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`DisplayName` - (Applicable when instance_type=compute) A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.
* `IsReadOnly` - (Applicable when instance_type=compute) Whether the attachment should be created in read-only mode.
* `Type` - (Required) The type of volume. The only supported values are "iscsi" and "paravirtualized".
* `UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`IsReadOnly` - (Applicable when instance_type=compute) Whether the attachment should be created in read-only mode.
* `Type` - (Required) The type of volume. The only supported values are "iscsi" and "paravirtualized".
* `UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`Type` - (Required) The type of volume. The only supported values are "iscsi" and "paravirtualized".
* `UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`UseChap` - (Applicable when type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.
* `CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`CreateDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`AvailabilityDomain` - (Optional) The availability domain of the volume.  Example: `Uocm:PHX-AD-1`
* `BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`BackupPolicyId` - (Optional) If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.
* `CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`CompartmentId` - (Optional) The OCID of the compartment that contains the volume.
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
* `FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`SizeInGbs` - (Optional) The size of the volume in GBs.
* `SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`SourceDetails` - (Optional) Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same availability domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.
* `Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`Id` - (Optional) The OCID of the volume backup.
* `Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`Type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`VolumeId` - (Optional) The OCID of the volume.
* `InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`InstanceType` - (Required) The type of instance details. Supported instanceType is compute
* `LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`LaunchDetails` - (Optional)
* `AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`AvailabilityDomain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`CompartmentId` - (Optional) The OCID of the compartment.
* `CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`SubnetId` - (Optional)
* `DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`DefinedTags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`ExtendedMetadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`FreeformTags` - (Optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `IpxeScript` - (Optional) This is an advanced option.

`IpxeScript` - (Optional) This is an advanced option.

`Metadata` - (Optional) Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

`Shape` - (Optional) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

`SourceDetails` - (Optional) Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.
* `BootVolumeId` - (Applicable when source_type=bootVolume) The OCID of the boot volume used to boot the instance.
* `ImageId` - (Applicable when source_type=image) The OCID of the image used to boot the instance.
* `SourceType` - (Required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.
* `SecondaryVnics` - (Optional)
* `CreateVnicDetails` - (Optional) Details for creating a new VNIC.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`BootVolumeId` - (Applicable when source_type=bootVolume) The OCID of the boot volume used to boot the instance.
* `ImageId` - (Applicable when source_type=image) The OCID of the image used to boot the instance.
* `SourceType` - (Required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.
* `SecondaryVnics` - (Optional)
* `CreateVnicDetails` - (Optional) Details for creating a new VNIC.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`ImageId` - (Applicable when source_type=image) The OCID of the image used to boot the instance.
* `SourceType` - (Required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.
* `SecondaryVnics` - (Optional)
* `CreateVnicDetails` - (Optional) Details for creating a new VNIC.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`SourceType` - (Required) The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.
* `SecondaryVnics` - (Optional)
* `CreateVnicDetails` - (Optional) Details for creating a new VNIC.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`SecondaryVnics` - (Optional)
* `CreateVnicDetails` - (Optional) Details for creating a new VNIC.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`CreateVnicDetails` - (Optional) Details for creating a new VNIC.
* `AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`AssignPublicIp` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`DisplayName` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`HostnameLabel` - (Optional)
* `PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`PrivateIp` - (Optional)
* `SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`SkipSourceDestCheck` - (Optional)
* `SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`SubnetId` - (Optional)
* `DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`DisplayName` - (Optional) A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`NicIndex` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).


## Return Values

### Fn::GetAtt

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