# Terraform::AWS::NetworkAcl

Provides an network ACL resource. You might set up network ACLs with rules similar
to your security groups in order to add an additional layer of security to your VPC.

~> **NOTE on Network ACLs and Network ACL Rules:** Terraform currently
provides both a standalone [Network ACL Rule](network_acl_rule.html) resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Properties

`VpcId` - (Required) The ID of the associated VPC.

`SubnetIds` - (Optional) A list of Subnet IDs to apply the ACL to.

`SubnetId` - (Optional, Deprecated) The ID of the associated Subnet. This
attribute is deprecated, please use the `SubnetIds` attribute instead.

`Ingress` - (Optional) Specifies an ingress rule. Parameters defined below.

`Egress` - (Optional) Specifies an egress rule. Parameters defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Egress Properties

`FromPort` - (Required) The from port to match.

`ToPort` - (Required) The to port to match.

`RuleNo` - (Required) The rule number. Used for ordering.

`Action` - (Required) The action to take.

`Protocol` - (Required) The protocol to match. If using the -1 'all'
protocol, you must specify a from and to port of 0.

`CidrBlock` - (Optional) The CIDR block to match. This must be a
valid network mask.

`Ipv6CidrBlock` - (Optional) The IPv6 CIDR block.

`IcmpType` - (Optional) The ICMP type to be used. Default 0.

`IcmpCode` - (Optional) The ICMP type code to be used. Default 0.


## Return Values

### Fn::GetAtt

`Id` - The ID of the network ACL.

`OwnerId` - The ID of the AWS account that owns the network ACL.

## See Also

* [aws_network_acl](https://www.terraform.io/docs/providers/aws/r/network_acl.html) in the _Terraform Provider Documentation_