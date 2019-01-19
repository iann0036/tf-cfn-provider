# Terraform::AzureRM::MariadbDatabase

Manages a MariaDB Database within a MariaDB Server

## Properties

`Name` - (Required) Specifies the name of the MariaDB Database, which needs [to be a valid MariaDB identifier](https://mariadb.com/kb/en/library/identifier-names/). Changing this forces a new resource to be created.

`ServerName` - (Required) Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.

`Charset` - (Required) Specifies the Charset for the MariaDB Database, which needs [to be a valid MariaDB Charset](https://mariadb.com/kb/en/library/setting-character-sets-and-collations). Changing this forces a new resource to be created.

`Collation` - (Required) Specifies the Collation for the MariaDB Database, which needs [to be a valid MariaDB Collation](https://mariadb.com/kb/en/library/setting-character-sets-and-collations). Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MariaDB Database.

## See Also

* [azurerm_mariadb_database](https://www.terraform.io/docs/providers/azurerm/r/mariadb_database.html) in the _Terraform Provider Documentation_