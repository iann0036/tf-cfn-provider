# Terraform::AWS::SecurityGroup

Provides a security group resource.

~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
provides both a standalone [Security Group Rule resource](security_group_rule.html) (a single `Ingress` or
`Egress` rule), and a Security Group resource with `Ingress` and `Egress` rules
defined in-line. At this time you cannot use a Security Group with in-line rules
in conjunction with any Security Group Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

~> **NOTE:** Referencing Security Groups across VPC peering has certain restrictions. More information is available in the [VPC Peering User Guide](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html).

## Properties

`Name` - (Optional, Forces new resource) The name of the security group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Description` - (Optional, Forces new resource) The security group description. Defaults to "Managed by Terraform". Cannot be "". __NOTE__: This field maps to the AWS `GroupDescription` attribute, for which there is no Update API. If you'd like to classify your security groups in a way that can be updated, use `Tags`.

`Ingress` - (Optional) Can be specified multiple times for each ingress rule. Each ingress block supports fields documented below.

`Egress` - (Optional, VPC only) Can be specified multiple times for each egress rule. Each egress block supports fields documented below.

`RevokeRulesOnDelete` - (Optional) Instruct Terraform to revoke all of the Security Groups attached ingress and egress rules before deleting the rule itself. This is normally not needed, however certain AWS services such as Elastic Map Reduce may automatically add required rules to security groups used with the service, and those rules may contain a cyclic dependency that prevent the security groups from being destroyed without removing the dependency first. Default `false`.

`VpcId` - (Optional, Forces new resource) The VPC ID.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Ingress Properties

`CidrBlocks` - (Optional) List of CIDR blocks.

`Ipv6CidrBlocks` - (Optional) List of IPv6 CIDR blocks.

`PrefixListIds` - (Optional) List of prefix list IDs.

`FromPort` - (Required) The start port (or ICMP type number if protocol is "icmp").

`Protocol` - (Required) The protocol. If you select a protocol of "-1" (semantically equivalent to `"all"`, which is not a valid value here), you must specify a "from_port" and "to_port" equal to 0. If not icmp, tcp, udp, or "-1" use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

`SecurityGroups` - (Optional) List of security group Group Names if using EC2-Classic, or Group IDs if using a VPC.

`Self` - (Optional) If true, the security group itself will be added as a source to this ingress rule.

`ToPort` - (Required) The end range port (or ICMP code if protocol is "icmp").

`Description` - (Optional) Description of this ingress rule.

### Egress Properties

`CidrBlocks` - (Optional) List of CIDR blocks.

`Ipv6CidrBlocks` - (Optional) List of IPv6 CIDR blocks.

`PrefixListIds` - (Optional) List of prefix list IDs (for allowing access to VPC endpoints).

`FromPort` - (Required) The start port (or ICMP type number if protocol is "icmp").

`Protocol` - (Required) The protocol. If you select a protocol of "-1" (semantically equivalent to `"all"`, which is not a valid value here), you must specify a "from_port" and "to_port" equal to 0. If not icmp, tcp, udp, or "-1" use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

`SecurityGroups` - (Optional) List of security group Group Names if using EC2-Classic, or Group IDs if using a VPC.

`Self` - (Optional) If true, the security group itself will be added as a source to this egress rule.

`ToPort` - (Required) The end range port (or ICMP code if protocol is "icmp").

`Description` - (Optional) Description of this egress rule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group.

`Arn` - The ARN of the security group.

`VpcId` - The VPC ID.

`OwnerId` - The owner ID.

`Name` - The name of the security group.

`Description` - The description of the security group.

`Ingress` - The ingress rules. See above for more.

`Egress` - The egress rules. See above for more.

## See Also

* [aws_security_group](https://www.terraform.io/docs/providers/aws/r/security_group.html) in the _Terraform Provider Documentation_