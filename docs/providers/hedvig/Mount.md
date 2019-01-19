# Terraform::Hedvig::Mount

A Hedvig Mount mounts a vdisk resource with a particular controller. It can then be used to connect ACL access resources to the vdisk as well.

## Properties

`Cluster` - (Required) The name of the cluster hosting the Mount.

`Vdisk` - (Required) The name of the vdisk the Mount is on.

`Controller` - (Required) The fully qualified domain name for the controller that the Mount is to attach to.


## See Also

* [hedvig_mount](https://www.terraform.io/docs/providers/hedvig/r/mount.html) in the _Terraform Provider Documentation_