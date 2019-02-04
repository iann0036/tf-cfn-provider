# Terraform::AWS::DbParameterGroup

Provides an RDS DB parameter group resource .Documentation of the available parameters for various RDS engines can be found at:
* [Aurora MySQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Reference.html)
* [Aurora PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html)
* [MariaDB Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Parameters.html)
* [Oracle Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Oracle.html#USER_ModifyInstance.Oracle.sqlnet)
* [PostgreSQL Parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.Parameters)

## Properties

`Name` - (Optional, Forces new resource) The name of the DB parameter group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Family` - (Required) The family of the DB parameter group.

`Description` - (Optional) The description of the DB parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of DB parameters to apply. Note that parameters may differ from a family to an other. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the group.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Name` - (Required) The name of the DB parameter.

`Value` - (Required) The value of the DB parameter.

`ApplyMethod` - (Optional) "immediate" (default), or "pending-reboot". Some
engines can't apply some parameters without a reboot, and you will need to
specify "pending-reboot" here.


## Return Values

### Fn::GetAtt

`Id` - The db parameter group name.

`Arn` - The ARN of the db parameter group.

## See Also

* [aws_db_parameter_group](https://www.terraform.io/docs/providers/aws/r/db_parameter_group.html) in the _Terraform Provider Documentation_