# Terraform::AzureRM::SqlServer

Manages a SQL Azure Database Server.

~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The SQL Server ID.

`FullyQualifiedDomainName` - The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net).

## See Also

* [azurerm_sql_server](https://www.terraform.io/docs/providers/azurerm/r/sql_server.html) in the _Terraform Provider Documentation_