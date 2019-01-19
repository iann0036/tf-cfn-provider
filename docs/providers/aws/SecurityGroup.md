# Terraform::AWS::SecurityGroup

Provides a security group resource.

~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
provides both a standalone [Security Group Rule resource](security_group_rule.html) (a single `ingress` or
`egress` rule), and a Security Group resource with `ingress` and `egress` rules
defined in-line. At this time you cannot use a Security Group with in-line rules
in conjunction with any Security Group Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

~> **NOTE:** Referencing Security Groups across VPC peering has certain restrictions. More information is available in the [VPC Peering User Guide](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html).

## Properties

TBC

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