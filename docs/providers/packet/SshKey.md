# Terraform::Packet::SshKey

Provides a Packet SSH key resource to allow you manage SSH
keys on your account. All SSH keys on your account are loaded on
all new devices, they do not have to be explicitly declared on
device creation.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The unique ID of the key.

`Name` - The name of the SSH key.

`PublicKey` - The text of the public key.

`Fingerprint` - The fingerprint of the SSH key.

`Created` - The timestamp for when the SSH key was created.

`Updated` - The timestamp for the last time the SSH key was updated.

## See Also

* [packet_ssh_key](https://www.terraform.io/docs/providers/packet/r/ssh_key.html) in the _Terraform Provider Documentation_