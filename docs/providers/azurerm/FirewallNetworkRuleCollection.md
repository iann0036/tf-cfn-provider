# Terraform::AzureRM::FirewallNetworkRuleCollection

Manages a Network Rule Collection within an Azure Firewall.

## Properties

`AzureFirewallName` - (Required) Specifies the name of the Firewall in which the Network Rule Collection should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.

`Priority` - (Required) Specifies the priority of the rule collection. Possible values are between `100` - `65000`.

`Action` - (Required) Specifies the action the rule will apply to matching traffic. Possible values are `Allow` and `Deny`.

`Rule` - (Required) One or more `Rule` blocks as defined below.

### Rule Properties

`Name` - (Required) Specifies the name of the rule.

`Description` - (Optional) Specifies a description for the rule.

`SourceAddresses` - (Required) A list of source IP addresses and/or IP ranges.

`DestinationAddresses` - (Required) A list of destination IP addresses and/or IP ranges.

`DestinationPorts` - (Required) A list of destination ports.

`Protocols` - (Required) A list of protocols. Possible values are `Any`, `ICMP`, `TCP` and `UDP`.


## See Also

* [azurerm_firewall_network_rule_collection](https://www.terraform.io/docs/providers/azurerm/r/firewall_network_rule_collection.html) in the _Terraform Provider Documentation_