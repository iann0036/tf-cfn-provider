# Terraform::DigitalOcean::Volume

Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The unique identifier for the block storage volume.

`FilesystemType` - Filesystem type (`xfs` or `ext4`) for the block storage volume.

`FilesystemLabel` - Filesystem label for the block storage volume.

`DropletIds` - A list of associated droplet ids.

## See Also

* [digitalocean_volume](https://www.terraform.io/docs/providers/digitalocean/r/volume.html) in the _Terraform Provider Documentation_