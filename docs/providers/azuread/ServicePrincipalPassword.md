# Terraform::AzureAD::ServicePrincipalPassword

Manages a Password associated with a Service Principal within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Key ID for the Service Principal Password.

## See Also

* [azuread_service_principal_password](https://www.terraform.io/docs/providers/azuread/r/service_principal_password.html) in the _Terraform Provider Documentation_