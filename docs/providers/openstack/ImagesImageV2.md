# Terraform::OpenStack::ImagesImageV2

Manages a V2 Image resource within OpenStack Glance.

## Properties

`ContainerFormat` - (Required) The container format. Must be one of "ami", "ari", "aki", "bare", "ovf".

`DiskFormat` - (Required) The disk format. Must be one of "ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".

`LocalFilePath` - (Optional) This is the filepath of the raw image file that will be uploaded to Glance. Conflicts with `ImageSourceUrl`.

`ImageCachePath` - (Optional) This is the directory where the images will be downloaded. Images will be stored with a filename corresponding to the url's md5 hash. Defaults to "$HOME/.terraform/image_cache".

`ImageSourceUrl` - (Optional) This is the url of the raw image that will be downloaded in the `ImageCachePath` before being uploaded to Glance. Glance is able to download image from internet but the `gophercloud` library does not yet provide a way to do so. Conflicts with `LocalFilePath`.

`MinDiskGb` - (Optional) Amount of disk space (in GB) required to boot image. Defaults to 0.

`MinRamMb` - (Optional) Amount of ram (in MB) required to boot image. Defauts to 0.

`Name` - (Required) The name of the image.

`Properties` - (Optional) A map of key/value pairs to set freeform information about an image. See the "Notes" section for further information about properties.

`Protected` - (Optional) If true, image will not be deletable. Defaults to false.

`Region` - (Optional) The region in which to obtain the V2 Glance client. A Glance client is needed to create an Image that can be used with a compute instance. If omitted, the `Region` argument of the provider is used. Changing this creates a new Image.

`Tags` - (Optional) The tags of the image. It must be a list of strings. At this time, it is not possible to delete all tags of an image.

`VerifyChecksum` - (Optional) If false, the checksum will not be verified once the image is finished uploading. Defaults to true.

`Visibility` - (Optional) The visibility of the image. Must be one of "public", "private", "community", or "shared". The ability to set the visibility depends upon the configuration of the OpenStack cloud.


## Return Values

### Fn::GetAtt

`Checksum` - The checksum of the data associated with the image.

`ContainerFormat` - See Properties above.

`CreatedAt` - The date the image was created.

`DiskFormat` - See Properties above.

`File` - the trailing path after the glance.

`Id` - A unique ID assigned by Glance.

`Metadata` - The metadata associated with the image.

`MinDiskGb` - See Properties above.

`MinRamMb` - See Properties above.

`Name` - See Properties above.

`Owner` - The id of the openstack user who owns the image.

`Properties` - See Properties above.

`Protected` - See Properties above.

`Region` - See Properties above.

`Schema` - The path to the JSON-schema that represent.

`SizeBytes` - The size in bytes of the data associated with the image.

`Status` - The status of the image. It can be "queued", "active".

`Tags` - See Properties above.

`UpdateAt` - The date the image was last updated.

`Visibility` - See Properties above.

## See Also

* [openstack_images_image_v2](https://www.terraform.io/docs/providers/openstack/r/images_image_v2.html) in the _Terraform Provider Documentation_