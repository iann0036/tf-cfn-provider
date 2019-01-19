# Terraform::OCI::CoreInstance

This resource provides the Instance resource in Oracle Cloud Infrastructure Core service.

Creates a new instance in the specified compartment and the specified availability domain.
For general information about instances, see
[Overview of the Compute Service](https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm).

For information about access control and compartments, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

For information about availability domains, see
[Regions and Availability Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
To get a list of availability domains, use the `ListAvailabilityDomains` operation
in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned,
unique ID called an Oracle Cloud Identifier (OCID).
When you create a resource, you can find its OCID in the response. You can
also retrieve a resource's OCID by using a List API operation
on that resource type, or by viewing the resource in the Console.

To launch an instance using an image or a boot volume use the `sourceDetails` parameter in [LaunchInstanceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/LaunchInstanceDetails).

When you launch an instance, it is automatically attached to a virtual
network interface card (VNIC), called the *primary VNIC*. The VNIC
has a private IP address from the subnet's CIDR. You can either assign a
private IP address of your choice or let Oracle automatically assign one.
You can choose whether the instance has a public IP address. To retrieve the
addresses, use the [ListVnicAttachments](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/VnicAttachment/ListVnicAttachments)
operation to get the VNIC ID for the instance, and then call
[GetVnic](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Vnic/GetVnic) with the VNIC ID.

You can later add secondary VNICs to an instance. For more information, see
[Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

## Properties

`AvailabilityDomain` - (Required) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - (Required) The OCID of the compartment.

`CreateVnicDetails` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched. * `AssignPublicIp` - (Optional) Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the [Subnet](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Subnet/)), then no public IP address is assigned. If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then a public IP address is assigned. If set to true and `prohibitPublicIpOnVnic` = true, an error is returned.

`AssignPublicIp` - (Optional) Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the [Subnet](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Subnet/)), then no public IP address is assigned. If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then a public IP address is assigned. If set to true and `prohibitPublicIpOnVnic` = true, an error is returned.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`HostnameLabel` - (Optional) Deprecated. Instead use `hostnameLabel` in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/). If you provide both, the values must match.

`PrivateIp` - (Optional) A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC's *primary* private IP address. The value appears in the [Vnic](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Vnic/) object and also the [PrivateIp](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/) object returned by [ListPrivateIps](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/ListPrivateIps) and [GetPrivateIp](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/PrivateIp/GetPrivateIp).  Example: `10.0.3.3` * `SkipSourceDestCheck` - (Optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see [Using a Private IP as a Route Target](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).  Example: `true` * `SubnetId` - (Required) The OCID of the subnet to create the VNIC in. When launching an instance, use this `subnetId` instead of the deprecated `subnetId` in [LaunchInstanceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/requests/LaunchInstanceDetails). At least one of them is required; if you provide both, the values must match.

`SkipSourceDestCheck` - (Optional) Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see [Using a Private IP as a Route Target](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).  Example: `true` * `SubnetId` - (Required) The OCID of the subnet to create the VNIC in. When launching an instance, use this `subnetId` instead of the deprecated `subnetId` in [LaunchInstanceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/requests/LaunchInstanceDetails). At least one of them is required; if you provide both, the values must match.

`SubnetId` - (Optional) Deprecated. Instead use `subnetId` in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/). At least one of them is required; if you provide both, the values must match.

`ExtendedMetadata` - (Optional) (Updatable) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`FaultDomain` - (Optional) A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.

`Image` - (Optional) Deprecated. Use `sourceDetails` with [InstanceSourceViaImageDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/InstanceSourceViaImageDetails) source type instead. If you specify values for both, the values must match.

`IpxeScript` - (Optional) This is an advanced option.

`IsPvEncryptionInTransitEnabled` - (Optional) Whether to enable encryption in transit for the PV boot volume attachment. Defaults to false.

`Metadata` - (Optional) (Updatable) Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.

`PreserveBootVolume` - (Optional) Specifies whether to delete or preserve the boot volume when terminating an instance. The default value is false. Note: This value only applies to destroy operations initiated by Terraform.

`Shape` - (Required) The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.

`SourceDetails` - (Optional) Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance. * `BootVolumeSizeInGbs` - (Applicable when source_type=image) The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB). * `KmsKeyId` - (Applicable when source_type=image) The OCID of the KMS key to be used as the master encryption key for the boot volume. * `SourceId` - (Required) The OCID of an image or a boot volume to use, depending on the value of `SourceType`. * `SourceType` - (Required) The source type for the instance. Use `Image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

`BootVolumeSizeInGbs` - (Applicable when source_type=image) The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB). * `KmsKeyId` - (Applicable when source_type=image) The OCID of the KMS key to be used as the master encryption key for the boot volume. * `SourceId` - (Required) The OCID of an image or a boot volume to use, depending on the value of `SourceType`. * `SourceType` - (Required) The source type for the instance. Use `Image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

`KmsKeyId` - (Applicable when source_type=image) The OCID of the KMS key to be used as the master encryption key for the boot volume. * `SourceId` - (Required) The OCID of an image or a boot volume to use, depending on the value of `SourceType`. * `SourceType` - (Required) The source type for the instance. Use `Image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

`SourceId` - (Required) The OCID of an image or a boot volume to use, depending on the value of `SourceType`. * `SourceType` - (Required) The source type for the instance. Use `Image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

`SourceType` - (Required) The source type for the instance. Use `Image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.


## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The availability domain the instance is running in.  Example: `Uocm:PHX-AD-1`.

`BootVolumeId` - The OCID of the attached boot volume. If the `SourceType` is `bootVolume`, this will be the same OCID as the `SourceId`.

`CompartmentId` - The OCID of the compartment that contains the instance.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`.

`ExtendedMetadata` - Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

`FaultDomain` - The name of the fault domain the instance is running in.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The OCID of the instance.

`Image` - Deprecated. Use `sourceDetails` instead.

`IpxeScript` - When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.

`LaunchMode` - Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:.

`NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.

`EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.

`PARAVIRTUALIZED` - Paravirtualized disk.

`CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

`BootVolumeType` - Emulation type for volume.

`ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block Storage volumes on Oracle provided images.

`SCSI` - Emulated SCSI disk.

`IDE` - Emulated IDE disk.

`VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data volumes on Oracle provided images.

`Firmware` - Firmware used to boot VM.  Select the option that matches your operating system.

`BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders.

`UEFI64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the default for Oracle provided images.

`IsConsistentVolumeNamingEnabled` - Whether to enable consistent volume naming feature. Defaults to false.

`IsPvEncryptionInTransitEnabled` - Whether to enable encryption in transit for the PV boot volume attachment. Defaults to false.

`NetworkType` - Emulation type for NIC.

`E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.

`RemoteDataVolumeType` - Emulation type for volume.

`Metadata` - Custom metadata that you provide.

`PreserveBootVolume` - Specifies whether to delete or preserve the boot volume when terminating an instance. The default value is false. Note: This value only applies to destroy operations initiated by Terraform.

`PrivateIp` - The private IP address of instance VNIC. To set the private IP address, use the `PrivateIp` argument in create_vnic_details.

`PublicIp` - The public IP address of instance VNIC (if enabled).

`Region` - The region that contains the availability domain the instance is running in.  Example: `phx`.

`Shape` - The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. You can enumerate all available shapes by calling [ListShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Shape/ListShapes).

`SourceDetails` - Details for creating an instance.

`BootVolumeSizeInGbs` - The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB). This should only be specified when `SourceType` is `Image`.

`KmsKeyId` - The OCID of the KMS key to be used as the master encryption key for the boot volume.

`SourceId` - The OCID of an image or a boot volume to use, depending on the value of `SourceType`.

`SourceType` - The source type for the instance. Use `Image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.

`State` - The current state of the instance.

`TimeCreated` - The date and time the instance was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`TimeMaintenanceRebootDue` - The date and time the instance is expected to be stopped / started,  in the format defined by RFC3339. After that time if instance hasn't been rebooted, Oracle will reboot the instance within 24 hours of the due time. Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state. Example: `2018-05-25T21:10:29.600Z`.

## See Also

* [oci_core_instance](https://www.terraform.io/docs/providers/oci/r/core_instance.html) in the _Terraform Provider Documentation_