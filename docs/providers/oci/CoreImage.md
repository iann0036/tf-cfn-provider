# Terraform::OCI::CoreImage

This resource provides the Image resource in Oracle Cloud Infrastructure Core service.

Creates a boot disk image for the specified instance or imports an exported image from the Oracle Cloud Infrastructure Object Storage service.

When creating a new image, you must provide the OCID of the instance you want to use as the basis for the image, and
the OCID of the compartment containing that instance. For more information about images,
see [Managing Custom Images](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm).

When importing an exported image from Object Storage, you specify the source information
in [ImageSourceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails).

When importing an image based on the namespace, bucket name, and object name,
use [ImageSourceViaObjectStorageTupleDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageTupleDetails).

When importing an image based on the Object Storage URL, use
[ImageSourceViaObjectStorageUriDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceViaObjectStorageUriDetails).
See [Object Storage URLs](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) and [pre-authenticated requests](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingaccess.htm#pre-auth)
for constructing URLs for image import/export.

For more information about importing exported images, see
[Image Import/Export](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/imageimportexport.htm).

You may optionally specify a *display name* for the image, which is simply a friendly name or description.
It does not have to be unique, and you can change it. See [UpdateImage](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Image/UpdateImage).
Avoid entering confidential information.

## Properties

`CompartmentId` - (Required) The OCID of the compartment containing the instance you want to use as the basis for the image.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`ImageSourceDetails` - (Optional) Details for creating an image through import
* `BucketName` - (Required when source_type=objectStorageTuple) The Object Storage bucket for the image.
* `NamespaceName` - (Required when source_type=objectStorageTuple) The Object Storage namespace for the image.
* `ObjectName` - (Required when source_type=objectStorageTuple) The Object Storage name for the image.
* `SourceImageType` - (Optional) The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic images are supported. Allowed values are:
* `QCOW2`
* `VMDK`
* `SourceType` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`BucketName` - (Required when source_type=objectStorageTuple) The Object Storage bucket for the image.
* `NamespaceName` - (Required when source_type=objectStorageTuple) The Object Storage namespace for the image.
* `ObjectName` - (Required when source_type=objectStorageTuple) The Object Storage name for the image.
* `SourceImageType` - (Optional) The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic images are supported. Allowed values are:
* `QCOW2`
* `VMDK`
* `SourceType` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`NamespaceName` - (Required when source_type=objectStorageTuple) The Object Storage namespace for the image.
* `ObjectName` - (Required when source_type=objectStorageTuple) The Object Storage name for the image.
* `SourceImageType` - (Optional) The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic images are supported. Allowed values are:
* `QCOW2`
* `VMDK`
* `SourceType` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`ObjectName` - (Required when source_type=objectStorageTuple) The Object Storage name for the image.
* `SourceImageType` - (Optional) The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic images are supported. Allowed values are:
* `QCOW2`
* `VMDK`
* `SourceType` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`SourceImageType` - (Optional) The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic images are supported. Allowed values are:
* `QCOW2`
* `VMDK`
* `SourceType` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`SourceType` - (Required) The source type for the image. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.
* `SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`SourceUri` - (Required when source_type=objectStorageUri) The Object Storage URL for the image.

`InstanceId` - (Optional -- required when not specifying `ImageSourceDetails`) The OCID of the instance you want to use as the basis for the image.

`LaunchMode` - (Optional) Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
* `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
* `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
* `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.
* `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

`NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
* `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
* `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.
* `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

`EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
* `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.
* `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

`PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.
* `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

`CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.


## Return Values

### Fn::GetAtt

`VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data volumes on Oracle provided images.

`UEFI64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the default for Oracle provided images.

`ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block Storage volumes on Oracle provided images.

`TimeCreated` - The date and time the image was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`IDE` - Emulated IDE disk.

`Id` - The OCID of the image.

`NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.

`CreateImageAllowed` - Whether instances launched with this image can be used to create new images. For example, you cannot create an image of an Oracle Database instance. Example: `true`.

`DisplayName` - A user-friendly name for the image. It does not have to be unique, and it's changeable. Avoid entering confidential information. You cannot use an Oracle-provided image name as a custom image name.  Example: `My custom Oracle Linux image`.

`CompartmentId` - The OCID of the compartment containing the instance you want to use as the basis for the image.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`Firmware` - Firmware used to boot VM.  Select the option that matches your operating system.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

`BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders.

`State` - The current state of the image.

`SCSI` - Emulated SCSI disk.

`IsPvEncryptionInTransitEnabled` - Whether to enable encryption in transit for the PV boot volume attachment. Defaults to false.

`E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver.

`EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.

`OperatingSystemVersion` - The image's operating system version.  Example: `7.2`.

`RemoteDataVolumeType` - Emulation type for volume.

`BaseImageId` - The OCID of the image originally used to launch the instance.

`IsConsistentVolumeNamingEnabled` - Whether to enable consistent volume naming feature. Defaults to false.

`OperatingSystem` - The image's operating system.  Example: `Oracle Linux`.

`PARAVIRTUALIZED` - Paravirtualized disk.

`LaunchMode` - Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:.

`SizeInMbs` - Image size (1 MB = 1048576 bytes)  Example: `47694`.

`BootVolumeType` - Emulation type for volume.

`NetworkType` - Emulation type for NIC.

## See Also

* [oci_core_image](https://www.terraform.io/docs/providers/oci/r/core_image.html) in the _Terraform Provider Documentation_