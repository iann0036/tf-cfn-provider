# Terraform::TelefonicaOpenCloud::FwRuleV2

Manages a v2 firewall rule resource within TelefonicaOpenCloud.

## Properties

`Region` - (Optional) The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
firewall rule.

`Name` - (Optional) A unique name for the firewall rule. Changing this
updates the `Name` of an existing firewall rule.

`Description` - (Optional) A description for the firewall rule. Changing this
updates the `Description` of an existing firewall rule.

`Protocol` - (Required) The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`Protocol` of an existing firewall rule.

`Action` - (Required) Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `Action` of an existing
firewall rule.

`IpVersion` - (Optional) IP version, either 4 (default) or 6. Changing this
updates the `IpVersion` of an existing firewall rule.

`SourceIpAddress` - (Optional) The source IP address on which the firewall
rule operates. Changing this updates the `SourceIpAddress` of an existing
firewall rule.

`DestinationIpAddress` - (Optional) The destination IP address on which the
firewall rule operates. Changing this updates the `DestinationIpAddress`
of an existing firewall rule.

`SourcePort` - (Optional) The source port on which the firewall
rule operates. Changing this updates the `SourcePort` of an existing
firewall rule.

`DestinationPort` - (Optional) The destination port on which the firewall
rule operates. Changing this updates the `DestinationPort` of an existing
firewall rule.

`Enabled` - (Optional) Enabled status for the firewall rule (must be "true"
or "false" if provided - defaults to "true"). Changing this updates the
`Enabled` status of an existing firewall rule.

`TenantId` - (Optional) The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Protocol` - See Properties above.

`Action` - See Properties above.

`IpVersion` - See Properties above.

`SourceIpAddress` - See Properties above.

`DestinationIpAddress` - See Properties above.

`SourcePort` - See Properties above.

`DestinationPort` - See Properties above.

`Enabled` - See Properties above.

`TenantId` - See Properties above.

## See Also

* [telefonicaopencloud_fw_rule_v2](https://www.terraform.io/docs/providers/telefonicaopencloud/r/fw_rule_v2.html) in the _Terraform Provider Documentation_