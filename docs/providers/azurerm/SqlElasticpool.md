# Terraform::AzureRM::SqlElasticpool

Allows you to manage an Azure SQL Elastic Pool.

~> **NOTE:** -  This version of the `Elasticpool` resource is being **deprecated** and should no longer be used. Please use the [azurerm_mssql_elasticpool](./mssql_elasticpool.html) version instead.

## Properties

`Name` - (Required) The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ServerName` - (Required) The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.

`Edition` - (Required) The edition of the elastic pool to be created. Valid values are `Basic`, `Standard`, and `Premium`. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for details. Changing this forces a new resource to be created.

`Dtu` - (Required) The total shared DTU for the elastic pool. Valid values depend on the `Edition` which has been defined. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for valid combinations.

`DbDtuMin` - (Optional) The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.

`DbDtuMax` - (Optional) The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.

`PoolSize` - (Optional) The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of `Edition` and `Dtu` and the limits documented in [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus). If not defined when creating an elastic pool, the value is set to the size implied by `Edition` and `Dtu`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The SQL Elastic Pool ID.

`CreationDate` - The creation date of the SQL Elastic Pool.

## See Also

* [azurerm_sql_elasticpool](https://www.terraform.io/docs/providers/azurerm/r/sql_elasticpool.html) in the _Terraform Provider Documentation_