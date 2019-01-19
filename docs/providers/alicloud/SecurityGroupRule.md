# Terraform::Alicloud::SecurityGroupRule

Provides a security group rule resource.
Represents a single `ingress` or `egress` group rule, which can be added to external Security Groups.

~> **NOTE:**  `nic_type` should set to `intranet` when security group type is `vpc` or specifying the `source_security_group_id`. In this situation it does not distinguish between intranet and internet, the rule is effective on them both.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the security group rule.

`Type` - The type of rule, `ingress` or `egress`.

`Name` - The name of the security group.

`PortRange` - The range of port numbers.

`IpProtocol` - The protocol of the security group rule.

## See Also

* [alicloud_security_group_rule](https://www.terraform.io/docs/providers/alicloud/r/security_group_rule.html) in the _Terraform Provider Documentation_