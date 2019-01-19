# Terraform::AzureRM::RelayNamespace

Manages an Azure Relay Namespace.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Azure Relay Namespace ID.

`PrimaryConnectionString` - The primary connection string for the authorization rule `RootManageSharedAccessKey`.

`SecondaryConnectionString` - The secondary connection string for the authorization rule `RootManageSharedAccessKey`.

`PrimaryKey` - The primary access key for the authorization rule `RootManageSharedAccessKey`.

`SecondaryKey` - The secondary access key for the authorization rule `RootManageSharedAccessKey`.

`MetricId` - The Identifier for Azure Insights metrics.

## See Also

* [azurerm_relay_namespace](https://www.terraform.io/docs/providers/azurerm/r/relay_namespace.html) in the _Terraform Provider Documentation_