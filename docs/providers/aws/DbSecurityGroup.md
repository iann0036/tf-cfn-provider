# Terraform::AWS::DbSecurityGroup

Provides an RDS security group resource. This is only for DB instances in the
EC2-Classic Platform. For instances inside a VPC, use the
[`Terraform::AWS::DbInstance.vpcSecurityGroupIds`](/docs/providers/aws/r/db_instance.html#vpc_security_group_ids)
attribute instead.

## Properties

`Name` - (Required) The name of the DB security group.

`Description` - (Optional) The description of the DB security group. Defaults to "Managed by Terraform".

`Ingress` - (Required) A list of ingress rules.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Cidr` - The CIDR block to accept.

`SecurityGroupName` - The name of the security group to authorize.

`SecurityGroupId` - The ID of the security group to authorize.

`SecurityGroupOwnerId` - The owner Id of the security group provided by `SecurityGroupName`.


## Return Values

### Fn::GetAtt

`Id` - The db security group ID.

`Arn` - The arn of the DB security group.

## See Also

* [aws_db_security_group](https://www.terraform.io/docs/providers/aws/r/db_security_group.html) in the _Terraform Provider Documentation_