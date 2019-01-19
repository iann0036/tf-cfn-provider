# Terraform::HCloud::VolumeAttachment

Provides a Hetzner Cloud Volume attachment to attach a Volume to a Hetzner Cloud Server. Deleting a Volume Attachment will detach the Volume from the Server.

## Properties

`VolumeId` - (Required, int) ID of the Volume. - `ServerId` - (Required, int) Server to attach the Volume to. - `Automount` - (Optional, bool) Automount the volume upon attaching it.

`ServerId` - (Required, int) Server to attach the Volume to. - `Automount` - (Optional, bool) Automount the volume upon attaching it.

`Automount` - (Optional, bool) Automount the volume upon attaching it.


## See Also

* [hcloud_volume_attachment](https://www.terraform.io/docs/providers/hcloud/r/volume_attachment.html) in the _Terraform Provider Documentation_