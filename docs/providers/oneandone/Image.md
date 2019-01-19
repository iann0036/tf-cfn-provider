# Terraform::OneAndOne::Image

Manages Images on 1&1

## Properties

`Datacenter` - (Optional) Country code of the datacenter where the image will be created (`US`, `DE`, `GB`, and `ES`).

`Description` - (Optional) Image description.

`Frequency` - (Optional) Creation policy frequency. Frecuency policy is only allowed in default datacenter. (`ONCE`, `DAILY`, `WEEKLY`).

`Name` - (Required) The name of the image.

`NumImages` - (Optional) Maximum number of images. Required when image is created with frequency policy.

`OsId` - (Optional) ID of the Operating System to import.

`ServerId` - (Optional) Server ID - Required when image `Source` is `server`.

`Source` - (Optional) Source of the new image: `server` (from an existing server), `image` (from an imported image) or `iso` (from an imported iso).

`Type` - (Optional) Type of the ISO to import: `os` (Operating System) or `app` (Application). It is required when the source is iso.

`Url` - (Optional) URL where the image can be downloaded. It is required when the source is image or iso.


## See Also

* [oneandone_image](https://www.terraform.io/docs/providers/oneandone/r/image.html) in the _Terraform Provider Documentation_