# Terraform::HuaweiCloud::FwPolicyV2

Manages a v2 firewall policy resource within HuaweiCloud.

## Properties

`Region` - (Optional) The region in which to obtain the v2 networking client.
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

`TenantId` - (Optional) The owner of the firewall policy. Required if admin wants
to create a firewall policy for another tenant. Changing this creates a new
firewall policy.

`ValueSpecs` - (Optional) Map of additional options.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Audited` - See Properties above.

`Shared` - See Properties above.

`TenantId` - See Properties above.

## See Also

* [huaweicloud_fw_policy_v2](https://www.terraform.io/docs/providers/huaweicloud/r/fw_policy_v2.html) in the _Terraform Provider Documentation_