# Terraform::Linode::Image

Provides a Linode Image resource.  This can be used to create, modify, and delete Linodes Images.  Linode Images are snapshots of a Linode Instance Disk which can then be used to provision more Linode Instances.  Images can be used across regions.

For more information, see [Linode's documentation on Images](https://www.linode.com/docs/platform/disk-images/linode-images/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/createImage).

## Properties

`Label` - (Required) A short description of the Image. Labels cannot contain special characters.

`DiskId` - (Required) The ID of the Linode Disk that this Image will be created from.

`LinodeId` - (Required) The ID of the Linode that this Image will be created from.

`Description` - (Optional) A detailed description of this Image.


## See Also

* [linode_image](https://www.terraform.io/docs/providers/linode/r/image.html) in the _Terraform Provider Documentation_