# Terraform::AzureAD::ServicePrincipal

Manages a Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Object ID for the Service Principal.

`DisplayName` - The Display Name of the Azure Active Directory Application associated with this Service Principal.

## See Also

* [azuread_service_principal](https://www.terraform.io/docs/providers/azuread/r/service_principal.html) in the _Terraform Provider Documentation_