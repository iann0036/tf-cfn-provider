# Terraform::AWS::DbSecurityGroup

Provides an RDS security group resource. This is only for DB instances in the
EC2-Classic Platform. For instances inside a VPC, use the
[`aws_db_instance.vpc_security_group_ids`](/docs/providers/aws/r/db_instance.html#vpc_security_group_ids)
attribute instead.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The db security group ID.

`Arn` - The arn of the DB security group.

## See Also

* [aws_db_security_group](https://www.terraform.io/docs/providers/aws/r/db_security_group.html) in the _Terraform Provider Documentation_