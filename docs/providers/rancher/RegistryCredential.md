# Terraform::Rancher::RegistryCredential

Provides a Rancher Registy Credential resource. This can be used to create registry credentials for rancher environments and retrieve their information.

## Properties

`Name` - (Required) The name of the registry credential.

`Description` - (Optional) A registry credential description.

`RegistryId` - (Required) The ID of the registry to create the credential for.

`PublicValue` - (Required) The public value (user name) of the account.

`SecretValue` - (Required) The secret value (password) of the account.


## Return Values

### Fn::GetAtt

`Id` - (Computed) The ID of the resource.

## See Also

* [rancher_registry_credential](https://www.terraform.io/docs/providers/rancher/r/registry_credential.html) in the _Terraform Provider Documentation_