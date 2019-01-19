# Terraform::AzureRM::MysqlFirewallRule

Manages a Firewall Rule for a MySQL Server

## Properties

`Name` - (Required) Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.

`ServerName` - (Required) Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

`StartIpAddress` - (Required) Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

`EndIpAddress` - (Required) Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the MySQL Firewall Rule.

## See Also

* [azurerm_mysql_firewall_rule](https://www.terraform.io/docs/providers/azurerm/r/mysql_firewall_rule.html) in the _Terraform Provider Documentation_