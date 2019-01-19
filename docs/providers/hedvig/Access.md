# Terraform::Hedvig::Access

A Hedvig Access adds an address to an ACL of a controller of a vdisk. This allows for management of access resources.

## Properties

`Cluster` - (Required) The name of the cluster hosting the Access.

`Vdisk` - (Required) The name of the Vdisk that this Access is associated with.

`Host` - (Required) The fully qualified domain name of the controller this Access is associated with.

`Address` - (Required) The actual address that this Access is providing access to.

`Type` - (Required) The type of address provided in `Address`. Can be `Host`, `ip` or `iqn`.


## See Also

* [hedvig_access](https://www.terraform.io/docs/providers/hedvig/r/access.html) in the _Terraform Provider Documentation_