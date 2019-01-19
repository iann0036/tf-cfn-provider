# Terraform::Packet::VolumeAttachment

Provides attachment of Packet Block Storage Volume to Devices.

Device and volume must be in the same location (facility).

Once attached by Terraform, they must then be mounted using the `Terraform::Packet::BlockAttach` and `packetBlockDetach` scripts.

## Properties

`VolumeId` - (Required) The ID of the volume to attach.

`DeviceId` - (Required) The ID of the device to which the volume should be attached.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the volume attachment.

## See Also

* [packet_volume_attachment](https://www.terraform.io/docs/providers/packet/r/volume_attachment.html) in the _Terraform Provider Documentation_