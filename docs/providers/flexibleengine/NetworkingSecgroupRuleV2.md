# Terraform::FlexibleEngine::NetworkingSecgroupRuleV2

Manages a V2 neutron security group rule resource within FlexibleEngine.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client. A networking client is needed to create a port. If omitted, the `Region` argument of the provider is used. Changing this creates a new security group rule.

`Direction` - (Required) The direction of the rule, valid values are __ingress__ or __egress__. Changing this creates a new security group rule.

`Ethertype` - (Required) The layer 3 protocol type, valid values are __IPv4__ or __IPv6__. Changing this creates a new security group rule.

`Protocol` - (Optional) The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range. * __tcp__ * __udp__ * __icmp__ * __ah__ * __dccp__ * __egp__ * __esp__ * __gre__ * __igmp__ * __ipv6-encap__ * __ipv6-frag__ * __ipv6-icmp__ * __ipv6-nonxt__ * __ipv6-opts__ * __ipv6-route__ * __ospf__ * __pgm__ * __rsvp__ * __sctp__ * __udplite__ * __vrrp__.

`PortRangeMin` - (Optional) The lower part of the allowed port range, valid integer value needs to be between 1 and 65535. Changing this creates a new security group rule.

`PortRangeMax` - (Optional) The higher part of the allowed port range, valid integer value needs to be between 1 and 65535. Changing this creates a new security group rule.

`RemoteIpPrefix` - (Optional) The remote CIDR, the value needs to be a valid CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.

`RemoteGroupId` - (Optional) The remote group id, the value needs to be an FlexibleEngine ID of a security group in the same tenant. Changing this creates a new security group rule.

`SecurityGroupId` - (Required) The security group id the rule should belong to, the value needs to be an FlexibleEngine ID of a security group in the same tenant. Changing this creates a new security group rule.

`TenantId` - (Optional) The owner of the security group. Required if admin wants to create a port for another tenant. Changing this creates a new security group rule.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Direction` - See Properties above.

`Ethertype` - See Properties above.

`Protocol` - See Properties above.

`PortRangeMin` - See Properties above.

`PortRangeMax` - See Properties above.

`RemoteIpPrefix` - See Properties above.

`RemoteGroupId` - See Properties above.

`SecurityGroupId` - See Properties above.

`TenantId` - See Properties above.

## See Also

* [flexibleengine_networking_secgroup_rule_v2](https://www.terraform.io/docs/providers/flexibleengine/r/networking_secgroup_rule_v2.html) in the _Terraform Provider Documentation_