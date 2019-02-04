# Terraform::Rundeck::PrivateKey

The private key resource allows SSH private keys to be stored into Rundeck's key store.
The key store is where Rundeck keeps credentials that are needed to access the nodes on which
it runs commands.

## Properties

`Path` - (Required) The path within the key store where the key will be stored.

`KeyMaterial` - (Required) The private key material to store, serialized in any way that is
accepted by OpenSSH.


## See Also

* [rundeck_private_key](https://www.terraform.io/docs/providers/rundeck/r/private_key.html) in the _Terraform Provider Documentation_