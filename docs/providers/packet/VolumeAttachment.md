# Terraform::Packet::VolumeAttachment

Provides attachment of Packet Block Storage Volume to Devices.

Device and volume must be in the same location (facility).

Once attached by Terraform, they must then be mounted using the `packet_block_attach` and `packet_block_detach` scripts.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The unique ID of the volume attachment.

## See Also

* [packet_volume_attachment](https://www.terraform.io/docs/providers/packet/r/volume_attachment.html) in the _Terraform Provider Documentation_