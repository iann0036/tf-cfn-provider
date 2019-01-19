# Terraform::AzureAD::Application

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ApplicationId` - The Application ID.

## See Also

* [azuread_application](https://www.terraform.io/docs/providers/azuread/r/application.html) in the _Terraform Provider Documentation_