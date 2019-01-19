# Terraform::AzureRM::MysqlVirtualNetworkRule

Manages a MySQL Virtual Network Rule.

-> **NOTE:** MySQL Virtual Network Rules [can only be used with SKU Tiers of `GeneralPurpose` or `MemoryOptimized`](https://docs.microsoft.com/en-us/azure/mysql/concepts-data-access-and-security-vnet)

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the MySQL Virtual Network Rule.

## See Also

* [azurerm_mysql_virtual_network_rule](https://www.terraform.io/docs/providers/azurerm/r/mysql_virtual_network_rule.html) in the _Terraform Provider Documentation_