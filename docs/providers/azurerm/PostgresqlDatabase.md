# Terraform::AzureRM::PostgresqlDatabase

Manages a PostgreSQL Database within a PostgreSQL Server

## Properties

`Name` - (Required) Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a new resource to be created.

`ServerName` - (Required) Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

`Charset` - (Required) Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.

`Collation` - (Required) Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the PostgreSQL Database.

## See Also

* [azurerm_postgresql_database](https://www.terraform.io/docs/providers/azurerm/r/postgresql_database.html) in the _Terraform Provider Documentation_