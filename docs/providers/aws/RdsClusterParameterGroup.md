# Terraform::AWS::RdsClusterParameterGroup

Provides an RDS DB cluster parameter group resource. Documentation of the available parameters for various Aurora engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)

## Properties

`Name` - (Required) The name of the DB parameter.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Family` - (Required) The family of the DB cluster parameter group.

`Description` - (Optional) The description of the DB cluster parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-cluster-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-parameters.html) after initial creation of the group.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Value` - (Required) The value of the DB parameter.

`ApplyMethod` - (Optional) "immediate" (default), or "pending-reboot". Some engines can't apply some parameters without a reboot, and you will need to specify "pending-reboot" here.


## Return Values

### Fn::GetAtt

`Id` - The db cluster parameter group name.

`Arn` - The ARN of the db cluster parameter group.

## See Also

* [aws_rds_cluster_parameter_group](https://www.terraform.io/docs/providers/aws/r/rds_cluster_parameter_group.html) in the _Terraform Provider Documentation_