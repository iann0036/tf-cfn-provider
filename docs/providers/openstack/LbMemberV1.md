# Terraform::OpenStack::LbMemberV1

Manages a V1 load balancer member resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create an LB member. If omitted, the `Region` argument of the provider is used. Changing this creates a new LB member.

`PoolId` - (Required)  The ID of the LB pool. Changing this creates a new member.

`Address` - (Required) The IP address of the member. Changing this creates a new member.

`Port` - (Required) An integer representing the port on which the member is hosted. Changing this creates a new member.

`AdminStateUp` - (Optional) The administrative state of the member. Acceptable values are 'true' and 'false'. Changing this value updates the state of the existing member.

`TenantId` - (Optional) The owner of the member. Required if admin wants to create a member for another tenant. Changing this creates a new member.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`PoolId` - See Properties above.

`Address` - See Properties above.

`Port` - See Properties above.

`AdminStateUp` - See Properties above.

`Weight` - The load balancing weight of the member. This is currently unable.

## See Also

* [openstack_lb_member_v1](https://www.terraform.io/docs/providers/openstack/r/lb_member_v1.html) in the _Terraform Provider Documentation_