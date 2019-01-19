# Terraform::AzureRM::PostgresqlVirtualNetworkRule

Manages a PostgreSQL Virtual Network Rule.

-> **NOTE:** PostgreSQL Virtual Network Rules [can only be used with SKU Tiers of `GeneralPurpose` or `MemoryOptimized`](https://docs.microsoft.com/en-us/azure/postgresql/concepts-data-access-and-security-vnet)

## Properties

`Name` - (Required) The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.

`ServerName` - (Required) The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.

`SubnetId` - (Required) The ID of the subnet that the PostgreSQL server will be connected to.

`IgnoreMissingVnetServiceEndpoint` - (Optional) Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the PostgreSQL Virtual Network Rule.

## See Also

* [azurerm_postgresql_virtual_network_rule](https://www.terraform.io/docs/providers/azurerm/r/postgresql_virtual_network_rule.html) in the _Terraform Provider Documentation_