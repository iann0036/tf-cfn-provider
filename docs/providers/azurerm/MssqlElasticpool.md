# Terraform::AzureRM::MssqlElasticpool

Allows you to manage an Azure SQL Elastic Pool via the `2017-10-01-preview` API which allows for `vCore` and `DTU` based configurations.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The MsSQL Elastic Pool ID.

`ZoneRedundant` - Whether or not this elastic pool is zone redundant.

## See Also

* [azurerm_mssql_elasticpool](https://www.terraform.io/docs/providers/azurerm/r/mssql_elasticpool.html) in the _Terraform Provider Documentation_