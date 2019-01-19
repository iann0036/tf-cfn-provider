# Terraform::OneAndOne::SshKey

Manages SSH Keys on 1&1

## Properties

`Description` - (Optional) Description for the ssh key.

`Name` - (Required) The name of the storage.

`PublicKey` - (Optional) Public key to import. If not given, new SSH key pair will be created and the private key is returned in the response.


## See Also

* [oneandone_ssh_key](https://www.terraform.io/docs/providers/oneandone/r/ssh_key.html) in the _Terraform Provider Documentation_