# Terraform::AzureRM::AzureadServicePrincipalPassword

Manages a Password associated with a Service Principal within Azure Active Directory.

~> **NOTE:** The Azure Active Directory resources have been split out into [a new AzureAD Provider](http://terraform.io/docs/providers/azuread/index.html) - as such the AzureAD resources within the AzureRM Provider are deprecated and will be removed in the next major version (2.0). Information on how to migrate from the existing resources to the new AzureAD Provider [can be found here](../guides/migrating-to-azuread.html).

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Key ID for the Service Principal Password.

## See Also

* [azurerm_azuread_service_principal_password](https://www.terraform.io/docs/providers/azurerm/r/azuread_service_principal_password.html) in the _Terraform Provider Documentation_