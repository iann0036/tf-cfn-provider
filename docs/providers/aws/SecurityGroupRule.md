# Terraform::AWS::SecurityGroupRule

Provides a security group rule resource. Represents a single `ingress` or
`egress` group rule, which can be added to external Security Groups.

~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
provides both a standalone Security Group Rule resource (a single `ingress` or
`egress` rule), and a [Security Group resource](security_group.html) with `ingress` and `egress` rules
defined in-line. At this time you cannot use a Security Group with in-line rules
in conjunction with any Security Group Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

~> **NOTE:** Setting `protocol = "all"` or `protocol = -1` with `FromPort` and `ToPort` will result in the EC2 API creating a security group rule with all ports open. This API behavior cannot be controlled by Terraform and may generate warnings in the future.

~> **NOTE:** Referencing Security Groups across VPC peering has certain restrictions. More information is available in the [VPC Peering User Guide](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html).

## Properties

`Type` - (Required) The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).

`CidrBlocks` - (Optional) List of CIDR blocks. Cannot be specified with `SourceSecurityGroupId`.

`Ipv6CidrBlocks` - (Optional) List of IPv6 CIDR blocks.

`PrefixListIds` - (Optional) List of prefix list IDs (for allowing access to VPC endpoints). Only valid with `egress`.

`FromPort` - (Required) The start port (or ICMP type number if protocol is "icmp").

`Protocol` - (Required) The protocol. If not icmp, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

`SecurityGroupId` - (Required) The security group to apply this rule to.

`SourceSecurityGroupId` - (Optional) The security group id to allow access to/from, depending on the `Type`. Cannot be specified with `CidrBlocks`.

`Self` - (Optional) If true, the security group itself will be added as a source to this ingress rule.

`ToPort` - (Required) The end port (or ICMP code if protocol is "icmp").

`Description` - (Optional) Description of the rule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group rule.

`Type` - The type of rule, `ingress` or `egress`.

`FromPort` - The start port (or ICMP type number if protocol is "icmp").

`ToPort` - The end port (or ICMP code if protocol is "icmp").

## See Also

* [aws_security_group_rule](https://www.terraform.io/docs/providers/aws/r/security_group_rule.html) in the _Terraform Provider Documentation_