# Terraform::AWS::NetworkAclRule

Creates an entry (a rule) in a network ACL with the specified rule number.

~> **NOTE on Network ACLs and Network ACL Rules:** Terraform currently
provides both a standalone Network ACL Rule resource and a [Network ACL](network_acl.html) resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Properties

`NetworkAclId` - (Required) The ID of the network ACL.

`RuleNumber` - (Required) The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.

`Egress` - (Optional, bool) Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.

`Protocol` - (Required) The protocol. A value of -1 means all protocols.

`RuleAction` - (Required) Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`.

`CidrBlock` - (Optional) The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

`Ipv6CidrBlock` - (Optional) The IPv6 CIDR block to allow or deny.

`FromPort` - (Optional) The from port to match.

`ToPort` - (Optional) The to port to match.

`IcmpType` - (Optional) ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1.

`IcmpCode` - (Optional) ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1.


## Return Values

### Fn::GetAtt

`Id` - The ID of the network ACL Rule.

## See Also

* [aws_network_acl_rule](https://www.terraform.io/docs/providers/aws/r/network_acl_rule.html) in the _Terraform Provider Documentation_