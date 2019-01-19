# Terraform::AzureRM::AppServiceSlot

Manages an App Service Slot (within an App Service).

-> **Note:** When using Slots - the `AppSettings`, `ConnectionString` and `SiteConfig` blocks on the `Terraform::AzureRM::AppService` resource will be overwritten when promoting a Slot using the `azurermAppServiceActiveSlot` resource.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the App Service Slot component.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`AppServicePlanId` - (Required) The ID of the App Service Plan within which to create this App Service Slot. Changing this forces a new resource to be created.

`AppServiceName` - (Required) The name of the App Service within which to create the App Service Slot.  Changing this forces a new resource to be created.

`AppSettings` - (Optional) A key-value pair of App Settings.

`ConnectionString` - (Optional) An `ConnectionString` block as defined below.

`ClientAffinityEnabled` - (Optional) Should the App Service Slot send session affinity cookies, which route client requests in the same session to the same instance?.

`Enabled` - (Optional) Is the App Service Slot Enabled?.

`HttpsOnly` - (Optional) Can the App Service Slot only be accessed via HTTPS? Defaults to `false`.

`SiteConfig` - (Optional) A `SiteConfig` object as defined below.

`Identity` - (Optional) A Managed Service Identity block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Identity Properties

`Type` - (Required) Specifies the identity type of the App Service. At this time the only allowed value is `SystemAssigned`.

### ConnectionString Properties

`Name` - (Required) The name of the Connection String.

`Value` - (Required) The value for the Connection String.

### SiteConfig Properties

`AlwaysOn` - (Optional) Should the app be loaded at all times? Defaults to `false`.

`AppCommandLine` - (Optional) App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.

`DefaultDocuments` - (Optional) The ordering of default documents to load, if an address isn't specified.

`DotnetFrameworkVersion` - (Optional) The version of the .net framework's CLR used in this App Service Slot. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.

`Http2Enabled` - (Optional) Is HTTP2 Enabled on this App Service? Defaults to `false`.

`IpRestriction` - (Optional) One or more `IpRestriction` blocks as defined below.

`JavaVersion` - (Optional) The version of Java to use. If specified `JavaContainer` and `JavaContainerVersion` must also be specified. Possible values are `1.7` and `1.8`.

`JavaContainer` - (Optional) The Java Container to use. If specified `JavaVersion` and `JavaContainerVersion` must also be specified. Possible values are `JETTY` and `TOMCAT`.

`JavaContainerVersion` - (Optional) The version of the Java Container to use. If specified `JavaVersion` and `JavaContainer` must also be specified.

`LocalMysqlEnabled` - (Optional) Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.

`ManagedPipelineMode` - (Optional) The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.

`MinTlsVersion` - (Optional) The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.

`PhpVersion` - (Optional) The version of PHP to use in this App Service Slot. Possible values are `5.5`, `5.6`, `7.0`, `7.1` and `7.2`.

`PythonVersion` - (Optional) The version of Python to use in this App Service Slot. Possible values are `2.7` and `3.4`.

`RemoteDebuggingEnabled` - (Optional) Is Remote Debugging Enabled? Defaults to `false`.

`RemoteDebuggingVersion` - (Optional) Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.

`Use32BitWorkerProcess` - (Optional) Should the App Service Slot run in 32 bit mode, rather than 64 bit mode?.

`VirtualNetworkName` - (Optional) The name of the Virtual Network which this App Service Slot should be attached to.

`WebsocketsEnabled` - (Optional) Should WebSockets be enabled?.

### IpRestriction Properties

`IpAddress` - (Required) The IP Address used for this IP Restriction.

`SubnetMask` - (Optional) The Subnet mask used for this IP Restriction. Defaults to `255.255.255.255`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the App Service Slot.

`DefaultSiteHostname` - The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`.

## See Also

* [azurerm_app_service_slot](https://www.terraform.io/docs/providers/azurerm/r/app_service_slot.html) in the _Terraform Provider Documentation_