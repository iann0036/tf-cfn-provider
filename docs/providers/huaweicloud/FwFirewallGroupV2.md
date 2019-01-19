# Terraform::HuaweiCloud::FwFirewallGroupV2

Manages a v2 firewall group resource within HuaweiCloud.

## Properties

`Region` - (Optional) The region in which to obtain the v2 networking client. A networking client is needed to create a firewall group. If omitted, the `Region` argument of the provider is used. Changing this creates a new firewall group.

`IngressPolicyId` - The ingress policy resource id for the firewall group. Changing this updates the `IngressPolicyId` of an existing firewall group.

`EgressPolicyId` - The egress policy resource id for the firewall group. Changing this updates the `EgressPolicyId` of an existing firewall group.

`Name` - (Optional) A name for the firewall group. Changing this updates the `Name` of an existing firewall group.

`Description` - (Required) A description for the firewall group. Changing this updates the `Description` of an existing firewall group.

`AdminStateUp` - (Optional) Administrative up/down status for the firewall group (must be "true" or "false" if provided - defaults to "true"). Changing this updates the `AdminStateUp` of an existing firewall group.

`TenantId` - (Optional) The owner of the floating IP. Required if admin wants to create a firewall group for another tenant. Changing this creates a new firewall group.

`Ports` - (Optional) Port(s) to associate this firewall group instance with. Must be a list of strings. Changing this updates the associated routers of an existing firewall group.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`PolicyId` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`AdminStateUp` - See Properties above.

`TenantId` - See Properties above.

`Ports` - See Properties above.

## See Also

* [huaweicloud_fw_firewall_group_v2](https://www.terraform.io/docs/providers/huaweicloud/r/fw_firewall_group_v2.html) in the _Terraform Provider Documentation_