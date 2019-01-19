# Terraform::AWS::NetworkAcl

Provides an network ACL resource. You might set up network ACLs with rules similar
to your security groups in order to add an additional layer of security to your VPC.

~> **NOTE on Network ACLs and Network ACL Rules:** Terraform currently
provides both a standalone [Network ACL Rule](network_acl_rule.html) resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the network ACL.

`OwnerId` - The ID of the AWS account that owns the network ACL.

## See Also

* [aws_network_acl](https://www.terraform.io/docs/providers/aws/r/network_acl.html) in the _Terraform Provider Documentation_