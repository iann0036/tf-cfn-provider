# Terraform::OCI::CoreVolumeAttachment

This resource provides the Volume Attachment resource in Oracle Cloud Infrastructure Core service.

Attaches the specified storage volume to the specified instance.

## Properties

`AttachmentType` - (Required) The type of volume. The only supported value are "iscsi" and "paravirtualized".

`Device` - (Optional) The device name.

`DisplayName` - (Optional) A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.

`InstanceId` - (Required) The OCID of the instance.

`IsPvEncryptionInTransitEnabled` - (Applicable when attachment_type=paravirtualized) Whether to enable encryption in transit for the PV data volume attachment. Defaults to false.

`IsReadOnly` - (Optional) Whether the attachment was created in read-only mode.

`UseChap` - (Applicable when attachment_type=iscsi) Whether to use CHAP authentication for the volume attachment. Defaults to false.

`VolumeId` - (Required) The OCID of the volume.


## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The availability domain of an instance.  Example: `Uocm:PHX-AD-1`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.  Example: `My volume attachment`.

`CompartmentId` - The OCID of the compartment.

`ChapUsername` - The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.  Example: `ocid1.volume.oc1.phx.abyhqljrgvttnlx73nmrwfaux7kcvzfs3s66izvxf2h4lgvyndsdsnoiwr5q`.

`Port` - The volume's iSCSI port.  Example: `3260`.

`IsPvEncryptionInTransitEnabled` - Whether the enable encryption in transit for the PV volume attachment is on or not.

`TimeCreated` - The date and time the volume was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`Id` - The OCID of the volume attachment.

`InstanceId` - The OCID of the instance the volume is attached to.

`State` - The current state of the volume attachment.

`Iqn` - The target volume's iSCSI Qualified Name in the format defined by RFC 3720.  Example: `iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9`.

`IsReadOnly` - Whether the attachment was created in read-only mode.

`Ipv4` - The volume's iSCSI IP address.  Example: `169.254.0.2`.

`VolumeId` - The OCID of the volume.

`Device` - The device name.

`AttachmentType` - The type of volume attachment.

`ChapSecret` - The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name. (Also called the "CHAP password".)  Example: `d6866c0d-298b-48ba-95af-309b4faux45e`.

## See Also

* [oci_core_volume_attachment](https://www.terraform.io/docs/providers/oci/r/core_volume_attachment.html) in the _Terraform Provider Documentation_