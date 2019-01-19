# Terraform::AzureRM::AppService

Manages an App Service (within an App Service Plan).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the App Service.

`DefaultSiteHostname` - The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`.

`OutboundIpAddresses` - A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`.

`PossibleOutboundIpAddresses` - A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.

`SourceControl` - A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.

`SiteCredential` - A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

`Identity` - An `identity` block as defined below, which contains the Managed Service Identity information for this App Service.

`PrincipalId` - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.

`TenantId` - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.

`Username` - The username which can be used to publish to this App Service.

`Password` - The password associated with the username, which can be used to publish to this App Service.

`RepoUrl` - URL of the Git repository for this App Service.

`Branch` - Branch name of the Git repository for this App Service.

## See Also

* [azurerm_app_service](https://www.terraform.io/docs/providers/azurerm/r/app_service.html) in the _Terraform Provider Documentation_