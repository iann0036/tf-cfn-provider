# Terraform::OpenStack::LbPoolV1

Manages a V1 load balancer pool resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create an LB pool. If omitted, the `Region` argument of the provider is used. Changing this creates a new LB pool.

`Name` - (Required) The name of the pool. Changing this updates the name of the existing pool.

`Protocol` - (Required)  The protocol used by the pool members, you can use either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

`SubnetId` - (Required) The network on which the members of the pool will be located. Only members that are on this network can be added to the pool. Changing this creates a new pool.

`LbMethod` - (Required) The algorithm used to distribute load between the members of the pool. The current specification supports 'ROUND_ROBIN' and 'LEAST_CONNECTIONS' as valid values for this attribute.

`LbProvider` - (Optional) The backend load balancing provider. For example: `haproxy`, `F5`, etc.

`TenantId` - (Optional) The owner of the pool. Required if admin wants to create a pool member for another tenant. Changing this creates a new pool.

`MonitorIds` - (Optional) A list of IDs of monitors to associate with the pool.

`Member` - (Optional) An existing node to add to the pool. Changing this updates the members of the pool. The member object structure is documented below. Please note that the `Member` block is deprecated in favor of the `Terraform::OpenStack::LbMemberV1` resource.

### Member Properties

`Address` - (Required) The IP address of the member. Changing this creates a new member.

`Port` - (Required) An integer representing the port on which the member is hosted. Changing this creates a new member.

`AdminStateUp` - (Required) The administrative state of the member. Acceptable values are 'true' and 'false'. Changing this value updates the state of the existing member.

`TenantId` - (Optional) The owner of the member. Required if admin wants to create a pool member for another tenant. Changing this creates a new member.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Protocol` - See Properties above.

`SubnetId` - See Properties above.

`LbMethod` - See Properties above.

`LbProvider` - See Properties above.

`TenantId` - See Properties above.

`MonitorId` - See Properties above.

`Member` - See Properties above.

## See Also

* [openstack_lb_pool_v1](https://www.terraform.io/docs/providers/openstack/r/lb_pool_v1.html) in the _Terraform Provider Documentation_