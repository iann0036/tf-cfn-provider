# Terraform::Vault::Audit



## Properties

`Type` - (Required) Type of the audit device, such as 'file'.

`Path` - (optional) The path to mount the audit device. This defaults to the type.

`Description` - (Optional) Human-friendly description of the audit device.

`Options` - (Required) Configuration options to pass to the audit device itself.


## See Also

* [vault_audit](https://www.terraform.io/docs/providers/vault/r/audit.html) in the _Terraform Provider Documentation_