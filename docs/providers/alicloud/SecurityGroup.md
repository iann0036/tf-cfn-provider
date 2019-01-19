# Terraform::Alicloud::SecurityGroup

Provides a security group resource.

~> **NOTE:** `Terraform::Alicloud::SecurityGroup` is used to build and manage a security group, and `alicloudSecurityGroupRule` can define ingress or egress rules for it.

~> **NOTE:** From version 1.7.2, `Terraform::Alicloud::SecurityGroup` has supported to segregate different ECS instance in which the same security group.

## Properties

`Name` - (Optional) The name of the security group. Defaults to null.

`Description` - (Optional, Forces new resource) The security group description. Defaults to null.

`VpcId` - (Optional, Forces new resource) The VPC ID.

`InnerAccess` - (Optional) Whether to allow both machines to access each other on all ports in the same security group.

`Tags` - (Optional) A mapping of tags to assign to the resource.


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