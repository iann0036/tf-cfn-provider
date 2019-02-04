# Terraform::AzureRM::FunctionApp

Manages a Function App.

## Properties

`Name` - (Required) Specifies the name of the Function App. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Function App.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`AppServicePlanId` - (Required) The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.

`StorageConnectionString` - (Required) The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).

`AppSettings` - (Optional) A key-value pair of App Settings.

`EnableBuiltinLogging` - (Optional) Should the built-in logging of this Function App be enabled? Defaults to `true`.

`ConnectionString` - (Optional) An `ConnectionString` block as defined below.

`ClientAffinityEnabled` - (Optional) Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?.

`Enabled` - (Optional) Is the Function App enabled?.

`HttpsOnly` - (Optional) Can the Function App only be accessed via HTTPS? Defaults to `false`.

`Version` - (Optional) The runtime version associated with the Function App. Defaults to `~1`.

`SiteConfig` - (Optional) A `SiteConfig` object as defined below.

`Identity` - (Optional) An `Identity` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### ConnectionString Properties

`Name` - (Required) The name of the Connection String.

`Type` - (Required) The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.

`Value` - (Required) The value for the Connection String.

### SiteConfig Properties

`AlwaysOn` - (Optional) Should the Function App be loaded at all times? Defaults to `false`.

`Use32BitWorkerProcess` - (Optional) Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to `true`.

`WebsocketsEnabled` - (Optional) Should WebSockets be enabled?.

`LinuxFxVersion` - (Optional) Linux App Framework and version for the AppService, e.g. `DOCKER|(golang:latest)`.
---.

### Identity Properties

`Type` - (Required) Specifies the identity type of the App Service. At this time the only allowed value is `SystemAssigned`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Function App.

`DefaultHostname` - The default hostname associated with the Function App - such as `mysite.azurewebsites.net`.

`OutboundIpAddresses` - A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`.

`Identity` - An `Identity` block as defined below, which contains the Managed Service Identity information for this App Service.

`SiteCredential` - A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.

`Kind` - The Function App kind - such as `functionapp,linux,container`.

`PrincipalId` - The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.

`TenantId` - The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.

`Username` - The username which can be used to publish to this App Service.

`Password` - The password associated with the username, which can be used to publish to this App Service.

## See Also

* [azurerm_function_app](https://www.terraform.io/docs/providers/azurerm/r/function_app.html) in the _Terraform Provider Documentation_