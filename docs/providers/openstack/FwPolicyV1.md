# Terraform::OpenStack::FwPolicyV1

Manages a v1 firewall policy resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
firewall policy.

`Name` - (Optional) A name for the firewall policy. Changing this
updates the `Name` of an existing firewall policy.

`Description` - (Optional) A description for the firewall policy. Changing
this updates the `Description` of an existing firewall policy.

`Rules` - (Optional) An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

`Audited` - (Optional) Audit status of the firewall policy
(must be "true" or "false" if provided - defaults to "false").
This status is set to "false" whenever the firewall policy or any of its
rules are changed. Changing this updates the `Audited` status of an existing
firewall policy.

`Shared` - (Optional) Sharing status of the firewall policy (must be "true"
or "false" if provided). If this is "true" the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
`Shared` status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Audited` - See Properties above.

`Shared` - See Properties above.

## See Also

* [openstack_fw_policy_v1](https://www.terraform.io/docs/providers/openstack/r/fw_policy_v1.html) in the _Terraform Provider Documentation_