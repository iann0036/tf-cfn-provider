# Terraform::OpenStack::LbL7policyV2

Manages a Load Balancer L7 Policy resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`Region` argument of the provider is used. Changing this creates a new
L7 Policy.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns
the L7 Policy.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Policy.

`Name` - (Optional) Human-readable name for the L7 Policy. Does not have
to be unique.

`Description` - (Optional) Human-readable description for the L7 Policy.

`Action` - (Required) The L7 Policy action - can either be REDIRECT\_TO\_POOL,
REDIRECT\_TO\_URL or REJECT.

`ListenerId` - (Required) The Listener on which the L7 Policy will be associated with.
Changing this creates a new L7 Policy.

`Position` - (Optional) The position of this policy on the listener. Positions start at 1.

`RedirectPoolId` - (Optional) Requests matching this policy will be redirected to the
pool with this ID. Only valid if action is REDIRECT\_TO\_POOL.

`RedirectUrl` - (Optional) Requests matching this policy will be redirected to this URL.
Only valid if action is REDIRECT\_TO\_URL.

`AdminStateUp` - (Optional) The administrative state of the L7 Policy.
A valid value is true (UP) or false (DOWN).


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the L7 {olicy.

`Region` - See Properties above.

`TenantId` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Action` - See Properties above.

`ListenerId` - See Properties above.

`Position` - See Properties above.

`RedirectPoolId` - See Properties above.

`RedirectUrl` - See Properties above.

`AdminStateUp` - See Properties above.

## See Also

* [openstack_lb_l7policy_v2](https://www.terraform.io/docs/providers/openstack/r/lb_l7policy_v2.html) in the _Terraform Provider Documentation_