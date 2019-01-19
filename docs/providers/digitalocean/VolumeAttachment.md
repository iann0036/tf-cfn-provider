# Terraform::DigitalOcean::VolumeAttachment

Manages attaching a Volume to a Droplet.

~> **NOTE:** Volumes can be attached either directly on the `Terraform::DigitalOcean::Droplet` resource, or using the `digitaloceanVolumeAttachment` resource - but the two cannot be used together. If both are used against the same Droplet, the volume attachments will constantly drift.

## Properties

`DropletId` - (Required) ID of the Droplet to attach the volume to.

`VolumeId` - (Required) ID of the Volume to be attached to the Droplet.


## Return Values

### Fn::GetAtt

`Id` - The unique identifier for the volume attachment.

## See Also

* [digitalocean_volume_attachment](https://www.terraform.io/docs/providers/digitalocean/r/volume_attachment.html) in the _Terraform Provider Documentation_