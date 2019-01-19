# Terraform::AWS::DefaultSecurityGroup

Provides a resource to manage the default AWS Security Group.

For EC2 Classic accounts, each region comes with a Default Security Group.
Additionally, each VPC created in AWS comes with a Default Security Group that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource.

The `Terraform::AWS::DefaultSecurityGroup` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management. We can do this because these default security groups cannot be
destroyed, and are created with a known set of default ingress/egress rules.

When Terraform first adopts the Default Security Group, it **immediately removes all
ingress and egress rules in the Security Group**. It then proceeds to create any rules specified in the
configuration. This step is required so that only the rules specified in the
configuration are created.

This resource treats its inline rules as absolute; only the rules defined
inline are created, and any additions/removals external to this resource will
result in diff shown. For these reasons, this resource is incompatible with the
`Terraform::AWS::SecurityGroupRule` resource.

For more information about Default Security Groups, see the AWS Documentation on
[Default Security Groups][aws-default-security-groups].

## Properties

`Ingress` - (Optional) Can be specified multiple times for each ingress rule. Each ingress block supports fields documented below.

`Egress` - (Optional, VPC only) Can be specified multiple times for each egress rule. Each egress block supports fields documented below.

`VpcId` - (Optional, Forces new resource) The VPC ID. **Note that changing the `VpcId` will _not_ restore any default security group rules that were modified, added, or removed.** It will be left in its current state.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the security group.

`VpcId` - The VPC ID.

`OwnerId` - The owner ID.

`Name` - The name of the security group.

`Description` - The description of the security group.

`Ingress` - The ingress rules. See above for more.

`Egress` - The egress rules. See above for more.

## See Also

* [aws_default_security_group](https://www.terraform.io/docs/providers/aws/r/default_security_group.html) in the _Terraform Provider Documentation_