# Terraform::AzureRM::MysqlVirtualNetworkRule

Manages a MySQL Virtual Network Rule.

-> **NOTE:** MySQL Virtual Network Rules [can only be used with SKU Tiers of `GeneralPurpose` or `MemoryOptimized`](https://docs.microsoft.com/en-us/azure/mysql/concepts-data-access-and-security-vnet)

## Properties

`Name` - (Required) The name of the MySQL Virtual Network Rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group where the MySQL server resides. Changing this forces a new resource to be created.

`ServerName` - (Required) The name of the SQL Server to which this MySQL virtual network rule will be applied to. Changing this forces a new resource to be created.

`SubnetId` - (Required) The ID of the subnet that the MySQL server will be connected to.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MySQL Virtual Network Rule.

## See Also

* [azurerm_mysql_virtual_network_rule](https://www.terraform.io/docs/providers/azurerm/r/mysql_virtual_network_rule.html) in the _Terraform Provider Documentation_