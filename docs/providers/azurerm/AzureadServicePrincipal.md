# Terraform::AzureRM::AzureadServicePrincipal

Manages a Service Principal associated with an Application within Azure Active Directory.

~> **NOTE:** The Azure Active Directory resources have been split out into [a new AzureAD Provider](http://terraform.io/docs/providers/azuread/index.html) - as such the AzureAD resources within the AzureRM Provider are deprecated and will be removed in the next major version (2.0). Information on how to migrate from the existing resources to the new AzureAD Provider [can be found here](../guides/migrating-to-azuread.html).

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Object ID for the Service Principal.

`DisplayName` - The Display Name of the Azure Active Directory Application associated with this Service Principal.

## See Also

* [azurerm_azuread_service_principal](https://www.terraform.io/docs/providers/azurerm/r/azuread_service_principal.html) in the _Terraform Provider Documentation_