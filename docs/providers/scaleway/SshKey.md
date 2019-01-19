# Terraform::Scaleway::SshKey

Manages user SSH Keys to access servers provisioned on scaleway.
For additional details please refer to [API documentation](https://developer.scaleway.com/#users-user-get).

## Properties

`Key` - (Required) public key of the SSH key to be added.


## Return Values

### Fn::GetAtt

`Id` - fingerprint of the SSH key.

## See Also

* [scaleway_ssh_key](https://www.terraform.io/docs/providers/scaleway/r/ssh_key.html) in the _Terraform Provider Documentation_