# Terraform::AzureAD::ServicePrincipal

Manages a Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Properties

`ApplicationId` - (Required) The ID of the Azure AD Application for which to create a Service Principal.

`Tags` - (Optional) A list of tags to apply to the Service Principal.


## Return Values

### Fn::GetAtt

`Id` - The Object ID for the Service Principal.

`DisplayName` - The Display Name of the Azure Active Directory Application associated with this Service Principal.

## See Also

* [azuread_service_principal](https://www.terraform.io/docs/providers/azuread/r/service_principal.html) in the _Terraform Provider Documentation_