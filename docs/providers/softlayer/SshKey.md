# Terraform::SoftLayer::SshKey

Provides SSK keys. This allows SSH keys to be created, updated and deleted.
For additional details please refer to [API documentation](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Security_Ssh_Key).

## Properties

`Name` - (Required) A descriptive name used to identify an SSH key.

`PublicKey` - (Required) The public SSH key.

`Notes` - (Optional) A small note about an SSH key to use at your discretion.


## Return Values

### Fn::GetAtt

`Id` - The ID of the new SSH key.

`Fingerprint` - sequence of bytes to authenticate or lookup a longer SSH key.

## See Also

* [softlayer_ssh_key](https://www.terraform.io/docs/providers/softlayer/r/ssh_key.html) in the _Terraform Provider Documentation_