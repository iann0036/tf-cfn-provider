# Terraform::AzureRM::SignalrService

Manages an Azure SignalR service.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.

`Sku` - A `Sku` block as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Sku Properties

`Name` - (Required) Specifies which tier to use. Valid values are `Free_F1` and `Standard_S1`.

`Capacity` - (Required) Specifies the number of units associated with this SignalR service. Valid values are `1`, `2`, `5`, `10`, `20`, `50` and `100`.


## Return Values

### Fn::GetAtt

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