# Terraform::OpenStack::LbMemberV2

Manages a V2 member resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`Region` argument of the provider is used. Changing this creates a new
member.

`PoolId` - (Required) The id of the pool that this member will be
assigned to.

`SubnetId` - (Optional) The subnet in which to access the member.

`Name` - (Optional) Human-readable name for the member.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.

`Address` - (Required) The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.

`ProtocolPort` - (Required) The port on which to listen for client traffic.
Changing this creates a new member.

`Weight` - (Optional)  A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.

`AdminStateUp` - (Optional) The administrative state of the member.
A valid value is true (UP) or false (DOWN).


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the member.

`Name` - See Properties above.

`Weight` - See Properties above.

`AdminStateUp` - See Properties above.

`TenantId` - See Properties above.

`SubnetId` - See Properties above.

`PoolId` - See Properties above.

`Address` - See Properties above.

`ProtocolPort` - See Properties above.

## See Also

* [openstack_lb_member_v2](https://www.terraform.io/docs/providers/openstack/r/lb_member_v2.html) in the _Terraform Provider Documentation_