# Terraform::Hedvig::Lun

A Hedvig Lun adds a vdisk resource to a particular controller, enabling the addition of ACL access resources to the vdisk.

## Properties

`Cluster` - (Required) The name of the cluster hosting the LUN.

`Vdisk` - (Required) The name of the vdisk the LUN is on.

`Controller` - (Required) The fully qualified domain name for the controller that the LUN is to attach to.


## See Also

* [hedvig_lun](https://www.terraform.io/docs/providers/hedvig/r/lun.html) in the _Terraform Provider Documentation_