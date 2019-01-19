# Terraform::NSXT::NatRule

This resource provides a means to configure a NAT rule in NSX. NAT provides network address translation between one IP address space and another IP address space. NAT rules can be destination NAT or source NAT rules.

## Properties

`LogicalRouterId` - (Required) ID of the logical router.

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this NAT rule.

`Action` - (Required) NAT rule action type. Valid actions are: SNAT, DNAT, NO_NAT and REFLEXIVE. All rules in a logical router are either stateless or stateful. Mix is not supported. SNAT and DNAT are stateful, and can NOT be supported when the logical router is running at active-active HA mode. The REFLEXIVE action is stateless. The NO_NAT action has no translated_fields, only match fields.

`Enabled` - (Optional) enable/disable the rule.

`Logging` - (Optional) enable/disable the logging of rule.

`MatchDestinationNetwork` - (Required for action=DNAT, not allowed for action=REFLEXIVE) IP Address | CIDR. Omitting this field implies Any.

`MatchSourceNetwork` - (Required for action=NO_NAT or REFLEXIVE, Optional for the other actions) IP Address | CIDR. Omitting this field implies Any.

`NatPass` - (Optional) Enable/disable to bypass following firewall stage. The default is true, meaning that the following firewall stage will be skipped. Please note, if action is NO_NAT, then nat_pass must be set to true or omitted.

`TranslatedNetwork` - (Required for action=DNAT or SNAT) IP Address | IP Range | CIDR.

`TranslatedPorts` - (Optional) port number or port range. Allowed only when action=DNAT.


## Return Values

### Fn::GetAtt

`Id` - ID of the NAT rule.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`RulePriority` - The priority of the rule which is ascending, valid range [0-2147483647]. If multiple rules have the same priority, evaluation sequence is undefined.

## See Also

* [nsxt_nat_rule](https://www.terraform.io/docs/providers/nsxt/r/nat_rule.html) in the _Terraform Provider Documentation_