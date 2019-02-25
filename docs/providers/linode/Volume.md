# Terraform::Linode::Volume

Provides a Linode Volume resource.  This can be used to create, modify, and delete Linodes Block Storage Volumes.  Block Storage Volumes are removable storage disks that persist outside the life-cycle of Linode Instances. These volumes can be attached to and detached from Linode instances throughout a region.

For more information, see [How to Use Block Storage with Your Linode](https://www.linode.com/docs/platform/block-storage/how-to-use-block-storage-with-your-linode/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createVolume).

## Properties

`Label` - (Required) The label of the Linode Volume.

`Region` - (Required) The region where this volume will be deployed.  Examples are `"us-east"`, `"us-west"`, `"ap-south"`, etc.  *Changing `Region` forces the creation of a new Linode Volume.*.

`Size` - (Optional) Size of the Volume in GB.

`LinodeId` - (Optional) The ID of a Linode Instance where the the Volume should be attached.

`Tags` - (Optional) A list of tags applied to this object. Tags are for organizational purposes only.


## See Also

* [linode_volume](https://www.terraform.io/docs/providers/linode/r/volume.html) in the _Terraform Provider Documentation_