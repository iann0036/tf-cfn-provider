# Terraform::AWS::RdsClusterParameterGroup

Provides an RDS DB cluster parameter group resource. Documentation of the available parameters for various Aurora engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The db cluster parameter group name.

`Arn` - The ARN of the db cluster parameter group.

## See Also

* [aws_rds_cluster_parameter_group](https://www.terraform.io/docs/providers/aws/r/rds_cluster_parameter_group.html) in the _Terraform Provider Documentation_