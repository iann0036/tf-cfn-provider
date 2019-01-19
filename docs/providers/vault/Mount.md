# Terraform::Vault::Mount



## Properties

`Path` - (Required) Where the secret backend will be mounted.

`Type` - (Required) Type of the backend, such as "aws".

`Description` - (Optional) Human-friendly description of the mount.

`DefaultLeaseTtlSeconds` - (Optional) Default lease duration for tokens and secrets in seconds.

`MaxLeaseTtlSeconds` - (Optional) Maximum possible lease duration for tokens and secrets in seconds.

`Options` - (Optional) Specifies mount type specific options that are passed to the backend.


## Return Values

### Fn::GetAtt

`Accessor` - The accessor for this mount.

## See Also

* [vault_mount](https://www.terraform.io/docs/providers/vault/r/mount.html) in the _Terraform Provider Documentation_