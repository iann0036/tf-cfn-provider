# Terraform::AzureRM::DataLakeStoreFirewallRule

Manage a Azure Data Lake Store Firewall Rule.

## Properties

`Name` - (Required) Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Data Lake Store.

`AccountName` - (Required) Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.

`StartIpAddress` - (Required) The Start IP address for the firewall rule.

`EndIpAddress` - (Required) The End IP Address for the firewall rule.


## Return Values

### Fn::GetAtt

`Id` - The Date Lake Store Firewall Rule ID.

## See Also

* [azurerm_data_lake_store_firewall_rule](https://www.terraform.io/docs/providers/azurerm/r/data_lake_store_firewall_rule.html) in the _Terraform Provider Documentation_