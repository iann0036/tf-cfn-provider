# Terraform::Alicloud::SecurityGroupRule

Provides a security group rule resource.
Represents a single `ingress` or `egress` group rule, which can be added to external Security Groups.

~> **NOTE:**  `NicType` should set to `intranet` when security group type is `vpc` or specifying the `SourceSecurityGroupId`. In this situation it does not distinguish between intranet and internet, the rule is effective on them both.

## Properties

`Type` - (Required) The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).

`IpProtocol` - (Required) The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.

`PortRange` - (Required) The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid. For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.

`SecurityGroupId` - (Required) The security group to apply this rule to.

`NicType` - (Optional, Forces new resource) Network type, can be either `internet` or `intranet`, the default value is `internet`.

`Policy` - (Optional, Forces new resource) Authorization policy, can be either `accept` or `drop`, the default value is `accept`.

`Priority` - (Optional, Forces new resource) Authorization policy priority, with parameter values: `1-100`, default value: 1.

`CidrIp` - (Optional, Forces new resource) The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.

`SourceSecurityGroupId` - (Optional, Forces new resource) The target security group ID within the same region. If this field is specified, the `NicType` can only select `intranet`.

`SourceGroupOwnerAccount` - (Optional, Forces new resource) The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `CidrIp` has already been set.


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group rule.

`Type` - The type of rule, `ingress` or `egress`.

`Name` - The name of the security group.

`PortRange` - The range of port numbers.

`IpProtocol` - The protocol of the security group rule.

## See Also

* [alicloud_security_group_rule](https://www.terraform.io/docs/providers/alicloud/r/security_group_rule.html) in the _Terraform Provider Documentation_