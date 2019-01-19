# Terraform::AzureRM::PostgresqlConfiguration

Sets a PostgreSQL Configuration value on a PostgreSQL Server.

## Properties

`Name` - (Required) Specifies the name of the PostgreSQL Configuration, which needs [to be a valid PostgreSQL configuration name](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER). Changing this forces a new resource to be created.

`ServerName` - (Required) Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

`Value` - (Required) Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.


## Return Values

### Fn::GetAtt

`Id` - The ID of the PostgreSQL Configuration.

## See Also

* [azurerm_postgresql_configuration](https://www.terraform.io/docs/providers/azurerm/r/postgresql_configuration.html) in the _Terraform Provider Documentation_