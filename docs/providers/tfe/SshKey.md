# Terraform::Tfe::SshKey

This resource represents an SSH key which includes a name and the SSH private
key. An organization can have multiple SSH keys available.

## Properties

`Name` - (Required) Name to identify the SSH key.

`Organization` - (Required) Name of the organization.

`Key` - (Required) The text of the SSH private key.


## See Also

* [tfe_ssh_key](https://www.terraform.io/docs/providers/tfe/r/ssh_key.html) in the _Terraform Provider Documentation_