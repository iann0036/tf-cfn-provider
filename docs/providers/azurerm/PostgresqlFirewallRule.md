# Terraform::AzureRM::PostgresqlFirewallRule

Manages a Firewall Rule for a PostgreSQL Server

## Properties

`Name` - (Required) Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.

`ServerName` - (Required) Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

`StartIpAddress` - (Required) Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

`EndIpAddress` - (Required) Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the PostgreSQL Firewall Rule.

## See Also

* [azurerm_postgresql_firewall_rule](https://www.terraform.io/docs/providers/azurerm/r/postgresql_firewall_rule.html) in the _Terraform Provider Documentation_