# Terraform::AWS::DefaultNetworkAcl

Provides a resource to manage the default AWS Network ACL. VPC Only.

Each VPC created in AWS comes with a Default Network ACL that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource.

The `Terraform::AWS::DefaultNetworkAcl` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead attempts to "adopt" it
into management. We can do this because each VPC created has a Default Network
ACL that cannot be destroyed, and is created with a known set of default rules.

When Terraform first adopts the Default Network ACL, it **immediately removes all
rules in the ACL**. It then proceeds to create any rules specified in the
configuration. This step is required so that only the rules specified in the
configuration are created.

This resource treats its inline rules as absolute; only the rules defined
inline are created, and any additions/removals external to this resource will
result in diffs being shown. For these reasons, this resource is incompatible with the
`Terraform::AWS::NetworkAclRule` resource.

For more information about Network ACLs, see the AWS Documentation on
[Network ACLs][aws-network-acls].

## Properties

`DefaultNetworkAclId` - (Required) The Network ACL ID to manage. This
attribute is exported from `Terraform::AWS::Vpc`, or manually found via the AWS Console.

`SubnetIds` - (Optional) A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL.

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

`Id` - The ID of the Default Network ACL.

`VpcId` -  The ID of the associated VPC.

`Ingress` - Set of ingress rules.

`Egress` - Set of egress rules.

`OwnerId` - The ID of the AWS account that owns the Default Network ACL.

## See Also

* [aws_default_network_acl](https://www.terraform.io/docs/providers/aws/r/default_network_acl.html) in the _Terraform Provider Documentation_