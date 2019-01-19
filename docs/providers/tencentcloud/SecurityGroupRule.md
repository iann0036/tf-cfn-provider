# Terraform::TencentCloud::SecurityGroupRule

Provides a security group rule resource. Represents a single `ingress` or `egress` group rule, which can be added to external Security Groups.

## Properties

`SecurityGroupId` - (Required, Forces new resource) The security group to apply this rule to.

`Type` - (Required, Forces new resource) The type of rule being created. Valid options are "ingress" (inbound) or "egress" (outbound).

`CidrIp` - (Required, Forces new resource) can be IP, or CIDR block.

`IpProtocol` - (Optional, Forces new resource) Support "UDP"、"TCP"、"ICMP", Not configured means all protocols.

`PortRange` - (Optional, Forces new resource) examples, Single port: "53"、Multiple ports: "80,8080,443"、Continuous port: "80-90", Not configured to represent all ports.

`Policy` - (Required, Forces new resource) Policy of rule, "accept" or "drop".


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group rule.

`Type` - The type of rule, "ingress" or "egress".

`CidrIp` - The source of rule, IP or CIDR block.

`Policy` - The policy of rule, "accept" or "drop".

## See Also

* [tencentcloud_security_group_rule](https://www.terraform.io/docs/providers/tencentcloud/r/security_group_rule.html) in the _Terraform Provider Documentation_