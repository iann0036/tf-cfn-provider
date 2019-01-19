# Terraform::AzureRM::ApiManagement

Manages an API Management Service.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the API Management Service.

`GatewayUrl` - The URL of the Gateway for the API Management Service.

`GatewayRegionalUrl` - The URL of the Regional Gateway for the API Management Service in the specified region.

`ManagementApiUrl` - The URL for the Management API associated with this API Management service.

`PortalUrl` - The URL for the Publisher Portal associated with this API Management service.

`PublicIpAddresses` - Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.

`ScmUrl` - The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.

`Identity` - An `identity` block as defined below.

`AdditionalLocation` - One or more `additional_location` blocks as documented below.

`PrincipalId` - The Principal ID associated with this Managed Service Identity.

`TenantId` - The Tenant ID associated with this Managed Service Identity.

## See Also

* [azurerm_api_management](https://www.terraform.io/docs/providers/azurerm/r/api_management.html) in the _Terraform Provider Documentation_