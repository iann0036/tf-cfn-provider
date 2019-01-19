# Terraform::AzureRM::SqlActiveDirectoryAdministrator

Allows you to set a user or group as the AD administrator for an Azure SQL server

## Properties

`ServerName` - (Required) The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group for the SQL server. Changing this forces a new resource to be created.

`Login` - (Required) The login name of the principal to set as the server administrator.

`ObjectId` - (Required) The ID of the principal to set as the server administrator.

`TenantId` - (Required) The Azure Tenant ID.


## Return Values

### Fn::GetAtt

`Id` - The SQL Active Directory Administrator ID.

## See Also

* [azurerm_sql_active_directory_administrator](https://www.terraform.io/docs/providers/azurerm/r/sql_active_directory_administrator.html) in the _Terraform Provider Documentation_