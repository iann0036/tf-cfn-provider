# Terraform::Alicloud::SecurityGroup

Provides a security group resource.

~> **NOTE:** `alicloud_security_group` is used to build and manage a security group, and `alicloud_security_group_rule` can define ingress or egress rules for it.

~> **NOTE:** From version 1.7.2, `alicloud_security_group` has supported to segregate different ECS instance in which the same security group.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the security group.

`VpcId` - The VPC ID.

`Name` - The name of the security group.

`Description` - The description of the security group.

`InnerAccess` - Whether to allow inner network access.

`Tags` - The instance tags, use jsonencode(item) to display the value.

## See Also

* [alicloud_security_group](https://www.terraform.io/docs/providers/alicloud/r/security_group.html) in the _Terraform Provider Documentation_