# Terraform::Packet::ProjectSshKey

Provides a Packet project SSH key resource to manage project-specific SSH keys. On contrary to user SSH keys, project SSH keys are used to exclusively populate `authorized_keys` in new devices.

If you supply a list of project SSH keys when creating a new device, only the listed keys are used; user SSH keys are ignored.

## Properties

`Name` - (Required) The name of the SSH key for identification.

`PublicKey` - (Required) The public key. If this is a file, it can be read using the file interpolation function.

`ProjectId` - (Required) The ID of parent project.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the key.

`Name` - The name of the SSH key.

`PublicKey` - The text of the public key.

`ProjectId` - The ID of parent project.

`Fingerprint` - The fingerprint of the SSH key.

`Created` - The timestamp for when the SSH key was created.

`Updated` - The timestamp for the last time the SSH key was updated.

## See Also

* [packet_project_ssh_key](https://www.terraform.io/docs/providers/packet/r/project_ssh_key.html) in the _Terraform Provider Documentation_