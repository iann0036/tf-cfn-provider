# Terraform::AzureRM::RelayNamespace

Manages an Azure Relay Namespace.

## Properties

`Name` - (Required) The name of the SKU to use. At this time the only supported value is `Standard`.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Azure Relay Namespace.

`Location` - (Required) Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Azure Relay Namespace ID.

`PrimaryConnectionString` - The primary connection string for the authorization rule `RootManageSharedAccessKey`.

`SecondaryConnectionString` - The secondary connection string for the authorization rule `RootManageSharedAccessKey`.

`PrimaryKey` - The primary access key for the authorization rule `RootManageSharedAccessKey`.

`SecondaryKey` - The secondary access key for the authorization rule `RootManageSharedAccessKey`.

`MetricId` - The Identifier for Azure Insights metrics.

## See Also

* [azurerm_relay_namespace](https://www.terraform.io/docs/providers/azurerm/r/relay_namespace.html) in the _Terraform Provider Documentation_