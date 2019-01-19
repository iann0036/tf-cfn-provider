# Terraform::AzureRM::AzureadApplication

Manages an Application within Azure Active Directory.

~> **NOTE:** The Azure Active Directory resources have been split out into [a new AzureAD Provider](http://terraform.io/docs/providers/azuread/index.html) - as such the AzureAD resources within the AzureRM Provider are deprecated and will be removed in the next major version (2.0). Information on how to migrate from the existing resources to the new AzureAD Provider [can be found here](../guides/migrating-to-azuread.html).

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

* [azurerm_azuread_application](https://www.terraform.io/docs/providers/azurerm/r/azuread_application.html) in the _Terraform Provider Documentation_