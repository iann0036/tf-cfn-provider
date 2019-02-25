# Terraform::Packet::SshKey

Provides a resource to manage User SSH keys on your Packet user account. If you create a new device in a project, all the keys of the project's collaborators will be injected to the device.

The link between User SSH key and device is implicit. If you want to make sure that a key will be copied to a device, you must ensure that the device resource `depends_on` the key resource.

## Properties

`Name` - (Required) The name of the SSH key for identification.

`PublicKey` - (Required) The public key. If this is a file, it
can be read using the file interpolation function.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the key.

`Name` - The name of the SSH key.

`PublicKey` - The text of the public key.

`Fingerprint` - The fingerprint of the SSH key.

`Created` - The timestamp for when the SSH key was created.

`Updated` - The timestamp for the last time the SSH key was updated.

## See Also

* [packet_ssh_key](https://www.terraform.io/docs/providers/packet/r/ssh_key.html) in the _Terraform Provider Documentation_