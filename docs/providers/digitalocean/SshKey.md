# Terraform::DigitalOcean::SshKey

Provides a DigitalOcean SSH key resource to allow you to manage SSH
keys for Droplet access. Keys created with this resource
can be referenced in your Droplet configuration via their ID or
fingerprint.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The unique ID of the key.

`Name` - The name of the SSH key.

`PublicKey` - The text of the public key.

`Fingerprint` - The fingerprint of the SSH key.

## See Also

* [digitalocean_ssh_key](https://www.terraform.io/docs/providers/digitalocean/r/ssh_key.html) in the _Terraform Provider Documentation_