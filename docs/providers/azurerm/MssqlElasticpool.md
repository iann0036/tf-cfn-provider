# Terraform::AzureRM::MssqlElasticpool

Allows you to manage an Azure SQL Elastic Pool via the `2017-10-01-preview` API which allows for `vCore` and `DTU` based configurations.

## Properties

`Name` - (Required) The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ServerName` - (Required) The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`PerDatabaseSettings` - (Required) A `PerDatabaseSettings` block as defined below.

`MaxSizeGb` - (Optional) The max data size of the elastic pool in gigabytes. Conflicts with `MaxSizeBytes`.

`MaxSizeBytes` - (Optional) The max data size of the elastic pool in bytes. Conflicts with `MaxSizeGb`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Sku Properties

`Name` - (Required) Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either `vCore` based `Tier` + `Family` pattern (e.g. GP_Gen4, BC_Gen5) or the `DTU` based `BasicPool`, `StandardPool`, or `PremiumPool` pattern.

`Capacity` - (Required) The scale up/out capacity, representing server's compute units. For more information see the documentation for your Elasticpool configuration: [vCore-based](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools) or [DTU-based](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools).

`Tier` - (Required) The tier of the particular SKU. Possible values are `GeneralPurpose`, `BusinessCritical`, `Basic`, `Standard`, or `Premium`. For more information see the documentation for your Elasticpool configuration: [vCore-based](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools) or [DTU-based](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools).

`Family` - (Optional) The `Family` of hardware `Gen4` or `Gen5`.

### PerDatabaseSettings Properties

`MinCapacity` - (Required) The minimum capacity all databases are guaranteed.

`MaxCapacity` - (Required) The maximum capacity any one database can consume.


## Return Values

### Fn::GetAtt

`Id` - The MsSQL Elastic Pool ID.

`ZoneRedundant` - Whether or not this elastic pool is zone redundant.

## See Also

* [azurerm_mssql_elasticpool](https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool.html) in the _Terraform Provider Documentation_