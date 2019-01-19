# Terraform::AzureRM::MysqlConfiguration

Sets a MySQL Configuration value on a MySQL Server.

## Properties

`Name` - (Required) Specifies the name of the MySQL Configuration, which needs [to be a valid MySQL configuration name](https://dev.mysql.com/doc/refman/5.7/en/server-configuration.html). Changing this forces a new resource to be created.

`ServerName` - (Required) Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

`Value` - (Required) Specifies the value of the MySQL Configuration. See the MySQL documentation for valid values.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MySQL Configuration.

## See Also

* [azurerm_mysql_configuration](https://www.terraform.io/docs/providers/azurerm/r/mysql_configuration.html) in the _Terraform Provider Documentation_