# Terraform::HCloud::SshKey

Provides a Hetzner Cloud SSH key resource to manage SSH keys for server access.

## Properties

`Name` - (Required, string) Name of the SSH key. - `PublicKey` - (Required, string) The public key. If this is a file, it can be read using the file interpolation function.

`PublicKey` - (Required, string) The public key. If this is a file, it can be read using the file interpolation function.


## See Also

* [hcloud_ssh_key](https://www.terraform.io/docs/providers/hcloud/r/ssh_key.html) in the _Terraform Provider Documentation_