# Terraform::Linode::Sshkey

Provides a Linode SSH Key resource.  This can be used to create, modify, and delete Linodes SSH Keys.  Managed SSH Keys allow instances to be created with a list of Linode usernames, whose SSH keys will be automatically applied to the root account's `~/.ssh/authorized_keys` file.
For more information, see the [Linode APIv4 docs](https://developers.linode.com/api/v4#operation/getSSHKeys).

## Properties

`Label` - A label for the SSH Key.

`SshKey` - The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.


## See Also

* [linode_sshkey](https://www.terraform.io/docs/providers/linode/r/sshkey.html) in the _Terraform Provider Documentation_