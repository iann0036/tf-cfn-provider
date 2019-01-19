# Terraform::AzureRM::SignalrService

Manages an Azure SignalR service.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the SignalR service.

`Hostname` - The FQDN of the SignalR service.

`IpAddress` - The publicly accessible IP of the SignalR service.

`PublicPort` - The publicly accessible port of the SignalR service which is designed for browser/client use.

`ServerPort` - The publicly accessible port of the SignalR service which is designed for customer server side use.

`PrimaryAccessKey` - The primary access key for the SignalR service.

`PrimaryConnectionString` - The primary connection string for the SignalR service.

`SecondaryAccessKey` - The secondary access key for the SignalR service.

`SecondaryConnectionString` - The secondary connection string for the SignalR service.

## See Also

* [azurerm_signalr_service](https://www.terraform.io/docs/providers/azurerm/r/signalr_service.html) in the _Terraform Provider Documentation_