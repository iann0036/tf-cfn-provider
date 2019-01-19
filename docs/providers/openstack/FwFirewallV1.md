# Terraform::OpenStack::FwFirewallV1

Manages a v1 firewall resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the v1 networking client. A networking client is needed to create a firewall. If omitted, the `Region` argument of the provider is used. Changing this creates a new firewall.

`PolicyId` - (Required) The policy resource id for the firewall. Changing this updates the `PolicyId` of an existing firewall.

`Name` - (Optional) A name for the firewall. Changing this updates the `Name` of an existing firewall.

`Description` - (Required) A description for the firewall. Changing this updates the `Description` of an existing firewall.

`AdminStateUp` - (Optional) Administrative up/down status for the firewall (must be "true" or "false" if provided - defaults to "true"). Changing this updates the `AdminStateUp` of an existing firewall.

`TenantId` - (Optional) The owner of the floating IP. Required if admin wants to create a firewall for another tenant. Changing this creates a new firewall.

`AssociatedRouters` - (Optional) Router(s) to associate this firewall instance with. Must be a list of strings. Changing this updates the associated routers of an existing firewall. Conflicts with `NoRouters`.

`NoRouters` - (Optional) Should this firewall not be associated with any routers (must be "true" or "false" if provide - defaults to "false"). Conflicts with `AssociatedRouters`.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`PolicyId` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`AdminStateUp` - See Properties above.

`TenantId` - See Properties above.

`AssociatedRouters` - See Properties above.

`NoRouters` - See Properties above.

## See Also

* [openstack_fw_firewall_v1](https://www.terraform.io/docs/providers/openstack/r/fw_firewall_v1.html) in the _Terraform Provider Documentation_