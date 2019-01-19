# Terraform::Rundeck::PublicKey

The public key resource allows SSH public keys to be stored into Rundeck's key store.
The key store is where Rundeck keeps credentials that are needed to access the nodes on which
it runs commands.

This resource also allows the retrieval of an existing public key from the store, so that it
may be used in the configuration of other resources such as ``aws_key_pair``.

## Properties

`Delete` - (Computed) True if the key should be deleted when the resource is deleted. Defaults to true if key_material is provided in the configuration.

`Path` - (Required) The path within the key store where the key will be stored. By convention this path name normally ends with ".pub" and otherwise has the same name as the associated private key.

`KeyMaterial` - (Optional) The public key string to store, serialized in any way that is accepted by OpenSSH. If this is not included, ``KeyMaterial`` becomes an attribute that can be used to read the already-existing key material in the Rundeck store.


## Return Values

### Fn::GetAtt

`Url` - The URL at which the key material can be retrieved from the key store by other clients.

`KeyMaterial` - If `KeyMaterial` is omitted in the configuration, it becomes an attribute that.

## See Also

* [rundeck_public_key](https://www.terraform.io/docs/providers/rundeck/r/public_key.html) in the _Terraform Provider Documentation_