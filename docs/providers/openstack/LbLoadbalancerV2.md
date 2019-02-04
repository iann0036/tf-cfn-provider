# Terraform::OpenStack::LbLoadbalancerV2

Manages a V2 loadbalancer resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
LB member.

`VipSubnetId` - (Required) The network on which to allocate the
Loadbalancer's address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.

`Name` - (Optional) Human-readable name for the Loadbalancer. Does not have
to be unique.

`Description` - (Optional) Human-readable description for the Loadbalancer.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.

`VipAddress` - (Optional) The ip address of the load balancer.
Changing this creates a new loadbalancer.

`AdminStateUp` - (Optional) The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).

`Flavor` - (Optional) The UUID of a flavor. Changing this creates a new
loadbalancer.

`LoadbalancerProvider` - (Optional) The name of the provider. Changing this
creates a new loadbalancer.

`SecurityGroupIds` - (Optional) A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`VipSubnetId` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`TenantId` - See Properties above.

`VipAddress` - See Properties above.

`AdminStateUp` - See Properties above.

`Flavor` - See Properties above.

`LoadbalancerProvider` - See Properties above.

`SecurityGroupIds` - See Properties above.

`VipPortId` - The Port ID of the Load Balancer IP.

## See Also

* [openstack_lb_loadbalancer_v2](https://www.terraform.io/docs/providers/openstack/r/lb_loadbalancer_v2.html) in the _Terraform Provider Documentation_