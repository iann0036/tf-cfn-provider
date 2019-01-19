# Terraform::Hedvig::Vdisk

Manages a Vdisk resource on a Hedvig cluster. For more information, visit [Hedvig's webpage](http://hedvig.io).

## Properties

`Cluster` - (Required) The name of the cluster hosting the Vdisk.

`Name` - (Required) The name to be used by the Vdisk for identification.

`Size` - (Required) The size of the disk in GB.

`Type` - (Required) The type of the disk; can be either `BLOCK` or `NFS`.


## See Also

* [hedvig_vdisk](https://www.terraform.io/docs/providers/hedvig/r/vdisk.html) in the _Terraform Provider Documentation_