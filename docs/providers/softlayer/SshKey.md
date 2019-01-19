# Terraform::SoftLayer::SshKey

Provides SSK keys. This allows SSH keys to be created, updated and deleted.
For additional details please refer to [API documentation](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Security_Ssh_Key).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the new SSH key.

`Fingerprint` - sequence of bytes to authenticate or lookup a longer SSH key.

## See Also

* [softlayer_ssh_key](https://www.terraform.io/docs/providers/softlayer/r/ssh_key.html) in the _Terraform Provider Documentation_