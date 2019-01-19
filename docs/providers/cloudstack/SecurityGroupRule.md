# Terraform::CloudStack::SecurityGroupRule

Authorizes and revokes both ingress and egress rulea for a given security group.

## Properties

`SecurityGroupId` - (Required) The security group ID for which to create the rules. Changing this forces a new resource to be created.

`Rule` - (Required) Can be specified multiple times. Each rule block supports fields documented below.

`Project` - (Optional) The name or ID of the project in which the security group is created. Changing this forces a new resource to be created.

### Rule Properties

`CidrList` - (Optional) A CIDR list to allow access to the given ports.

`Protocol` - (Required) The name of the protocol to allow. Valid options are: `tcp`, `udp`, `icmp`, `all` or a valid protocol number.

`IcmpType` - (Optional) The ICMP type to allow, or `-1` to allow `any`. This can only be specified if the protocol is ICMP. (defaults 0).

`IcmpCode` - (Optional) The ICMP code to allow, or `-1` to allow `any`. This can only be specified if the protocol is ICMP. (defaults 0).

`Ports` - (Optional) List of ports and/or port ranges to allow. This can only be specified if the protocol is TCP, UDP, ALL or a valid protocol number.

`TrafficType` - (Optional) The traffic type for the rule. Valid options are: `ingress` or `egress`. (defaults ingress).

`UserSecurityGroupList` - (Optional) A list of security groups to apply the rules to.


## Return Values

### Fn::GetAtt

`Id` - The security group ID for which the rules are created.

## See Also

* [cloudstack_security_group_rule](https://www.terraform.io/docs/providers/cloudstack/r/security_group_rule.html) in the _Terraform Provider Documentation_