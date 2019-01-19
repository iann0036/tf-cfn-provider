# Terraform::DigitalOcean::Volume

Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The unique identifier for the block storage volume.

`FilesystemType` - Filesystem type (`xfs` or `ext4`) for the block storage volume.

`FilesystemLabel` - Filesystem label for the block storage volume.

`DropletIds` - A list of associated droplet ids.

## See Also

* [digitalocean_volume](https://www.terraform.io/docs/providers/digitalocean/r/volume.html) in the _Terraform Provider Documentation_