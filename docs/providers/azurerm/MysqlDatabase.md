# Terraform::AzureRM::MysqlDatabase

Manages a MySQL Database within a MySQL Server

## Properties

`Name` - (Required) Specifies the name of the MySQL Database, which needs [to be a valid MySQL identifier](https://dev.mysql.com/doc/refman/5.7/en/identifiers.html). Changing this forces a new resource to be created.

`ServerName` - (Required) Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

`Charset` - (Required) Specifies the Charset for the MySQL Database, which needs [to be a valid MySQL Charset](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html). Changing this forces a new resource to be created.

`Collation` - (Required) Specifies the Collation for the MySQL Database, which needs [to be a valid MySQL Collation](https://dev.mysql.com/doc/refman/5.7/en/charset-mysql.html). Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MySQL Database.

## See Also

* [azurerm_mysql_database](https://www.terraform.io/docs/providers/azurerm/r/mysql_database.html) in the _Terraform Provider Documentation_