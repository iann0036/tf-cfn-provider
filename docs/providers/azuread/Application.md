# Terraform::AzureAD::Application

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Properties

`Name` - (Required) The display name for the application.

`Homepage` - (optional) The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.

`IdentifierUris` - (Optional) A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

`ReplyUrls` - (Optional) A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

`AvailableToOtherTenants` - (Optional) Is this Azure AD Application available to other tenants? Defaults to `false`.

`Oauth2AllowImplicitFlow` - (Optional) Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.


## Return Values

### Fn::GetAtt

`ApplicationId` - The Application ID.

## See Also

* [azuread_application](https://www.terraform.io/docs/providers/azuread/r/application.html) in the _Terraform Provider Documentation_