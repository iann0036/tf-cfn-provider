# Terraform::AzureRM::FirewallApplicationRuleCollection

Manages an Application Rule Collection within an Azure Firewall.

## Properties

`Name` - (Required) Specifies the name of the rule.

`AzureFirewallName` - (Required) Specifies the name of the Firewall in which the Application Rule Collection should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.

`Priority` - (Required) Specifies the priority of the rule collection. Possible values are between `100` - `65000`.

`Action` - (Required) Specifies the action the rule will apply to matching traffic. Possible values are `Allow` and `Deny`.

`Rule` - (Required) One or more `Rule` blocks as defined below.

`Description` - (Optional) Specifies a description for the rule.

`SourceAddresses` - (Required) A list of source IP addresses and/or IP ranges.

`FqdnTags` - (Optional) A list of FQDN tags. Possible values are `AppServiceEnvironment`, `AzureBackup`, `MicrosoftActiveProtectionService`, `WindowsDiagnostics` and `WindowsUpdate`.

`TargetFqdns` - (Optional) A list of FQDNs.

`Protocol` - (Optional) One or more `Protocol` blocks as defined below.

`Port` - (Optional) Specify a port for the connection.

`Type` - (Required) Specifies the type of conection. Possible values are `Http` or `Https`.


## See Also

* [azurerm_firewall_application_rule_collection](https://www.terraform.io/docs/providers/azurerm/r/firewall_application_rule_collection.html) in the _Terraform Provider Documentation_