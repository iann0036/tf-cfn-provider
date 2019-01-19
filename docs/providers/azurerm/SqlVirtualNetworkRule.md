# Terraform::AzureRM::SqlVirtualNetworkRule

Allows you to add, update, or remove an Azure SQL server to a subnet of a virtual network.

## Properties

`Name` - (Required) The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.

`ResourceGroupName` - (Required) The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.

`ServerName` - (Required) The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.

`SubnetId` - (Required) The ID of the subnet that the SQL server will be connected to.

`IgnoreMissingVnetServiceEndpoint` - (Optional) Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.


## Return Values

### Fn::GetAtt

`Id` - The ID of the SQL virtual network rule.

## See Also

* [azurerm_sql_virtual_network_rule](https://www.terraform.io/docs/providers/azurerm/r/sql_virtual_network_rule.html) in the _Terraform Provider Documentation_