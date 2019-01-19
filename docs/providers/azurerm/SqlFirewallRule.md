# Terraform::AzureRM::SqlFirewallRule

Allows you to manage an Azure SQL Firewall Rule

## Properties

`Name` - (Required) The name of the firewall rule.

`ResourceGroupName` - (Required) The name of the resource group in which to create the sql server.

`ServerName` - (Required) The name of the SQL Server on which to create the Firewall Rule.

`StartIpAddress` - (Required) The starting IP address to allow through the firewall for this rule.

`EndIpAddress` - (Required) The ending IP address to allow through the firewall for this rule.


## Return Values

### Fn::GetAtt

`Id` - The SQL Firewall Rule ID.

## See Also

* [azurerm_sql_firewall_rule](https://www.terraform.io/docs/providers/azurerm/r/sql_firewall_rule.html) in the _Terraform Provider Documentation_