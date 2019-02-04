# Terraform::Triton::FirewallRule

The `Terraform::Triton::FirewallRule` resource represents a rule for the Triton cloud firewall.

## Properties

`Rule` - (string, Required)
The firewall rule described using the Cloud API rule syntax defined at https://docs.joyent.com/public-cloud/network/firewall/cloud-firewall-rules-reference.
Note: Cloud API will normalize rules based on case-sensitivity, parentheses,
ordering of IP addresses, etc. This can result in Terraform updating rules
repeatedly if the rule definition differs from the normalized value.

`Enabled` - (boolean, Optional)  Default: `false`
Whether the rule should be effective.

`Description` - (string, Optional)
Description of the firewall rule.


## See Also

* [triton_firewall_rule](https://www.terraform.io/docs/providers/triton/r/firewall_rule.html) in the _Terraform Provider Documentation_