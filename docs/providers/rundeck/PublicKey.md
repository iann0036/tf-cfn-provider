# Terraform::Rundeck::PublicKey

The public key resource allows SSH public keys to be stored into Rundeck's key store.
The key store is where Rundeck keeps credentials that are needed to access the nodes on which
it runs commands.

This resource also allows the retrieval of an existing public key from the store, so that it
may be used in the configuration of other resources such as ``aws_key_pair``.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Url` - The URL at which the key material can be retrieved from the key store by other clients.

`KeyMaterial` - If `key_material` is omitted in the configuration, it becomes an attribute that.

## See Also

* [rundeck_public_key](https://www.terraform.io/docs/providers/rundeck/r/public_key.html) in the _Terraform Provider Documentation_