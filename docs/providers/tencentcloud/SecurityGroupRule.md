# Terraform::TencentCloud::SecurityGroupRule

Provides a security group rule resource. Represents a single `ingress` or `egress` group rule, which can be added to external Security Groups.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the security group rule.

`Type` - The type of rule, "ingress" or "egress".

`CidrIp` - The source of rule, IP or CIDR block.

`Policy` - The policy of rule, "accept" or "drop".

## See Also

* [tencentcloud_security_group_rule](https://www.terraform.io/docs/providers/tencentcloud/r/security_group_rule.html) in the _Terraform Provider Documentation_