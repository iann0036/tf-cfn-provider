# Terraform::AzureRM::FunctionApp

Manages a Function App.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the Function App.

`DefaultHostname` - The default hostname associated with the Function App - such as `mysite.azurewebsites.net`.

`OutboundIpAddresses` - A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`.

`Identity` - An `identity` block as defined below, which contains the Managed Service Identity information for this App Service.

`SiteCredential` - A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

`PrincipalId` - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.

`TenantId` - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.

`Username` - The username which can be used to publish to this App Service.

`Password` - The password associated with the username, which can be used to publish to this App Service.

## See Also

* [azurerm_function_app](https://www.terraform.io/docs/providers/azurerm/r/function_app.html) in the _Terraform Provider Documentation_