# Terraform::AzureRM::SqlServer

Manages a SQL Azure Database Server.

~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) The name of the SQL Server. This needs to be globally unique within Azure.

`ResourceGroupName` - (Required) The name of the resource group in which to create the SQL Server.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Version` - (Required) The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).

`AdministratorLogin` - (Required) The administrator login name for the new server. Changing this forces a new resource to be created.

`AdministratorLoginPassword` - (Required) The password associated with the `AdministratorLogin` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx).

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The SQL Server ID.

`FullyQualifiedDomainName` - The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net).

## See Also

* [azurerm_sql_server](https://www.terraform.io/docs/providers/azurerm/r/sql_server.html) in the _Terraform Provider Documentation_