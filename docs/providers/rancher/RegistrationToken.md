# Terraform::Rancher::RegistrationToken

Provides a Rancher Registration Token resource. This can be used to create registration tokens for rancher environments and retrieve their information.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - (Computed) The ID of the resource.

`Image` - (Computed).

`Command` - The command used to start a rancher agent for this environment.

`RegistrationUrl` - The URL to use to register new nodes to the environment.

`Token` - The token to use to register new nodes to the environment.

## See Also

* [rancher_registration_token](https://www.terraform.io/docs/providers/rancher/r/registration_token.html) in the _Terraform Provider Documentation_