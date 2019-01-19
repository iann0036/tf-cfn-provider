# Terraform::DigitalOcean::Volume

Provides a DigitalOcean Block Storage volume which can be attached to a Droplet in order to provide expanded storage.

## Properties

`Region` - (Required) The region that the block storage volume will be created in.

`Name` - (Required) A name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.

`Size` - (Required) The size of the block storage volume in GiB. If updated, can only be expanded.

`Description` - (Optional) A free-form text field up to a limit of 1024 bytes to describe a block storage volume.

`SnapshotId` - (Optional) The ID of an existing volume snapshot from which the new volume will be created. If supplied, the region and size will be limitied on creation to that of the referenced snapshot.

`InitialFilesystemType` - (Optional) Initial filesystem type (`xfs` or `ext4`) for the block storage volume.

`InitialFilesystemLabel` - (Optional) Initial filesystem label for the block storage volume.


## Return Values

### Fn::GetAtt

`Id` - The unique identifier for the block storage volume.

`FilesystemType` - Filesystem type (`xfs` or `ext4`) for the block storage volume.

`FilesystemLabel` - Filesystem label for the block storage volume.

`DropletIds` - A list of associated droplet ids.

## See Also

* [digitalocean_volume](https://www.terraform.io/docs/providers/digitalocean/r/volume.html) in the _Terraform Provider Documentation_