# Terraform::AWS::DbOptionGroup

Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:
* [MariaDB Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html)
* [Microsoft SQL Server Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
* [MySQL Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)
* [Oracle Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The db option group name.

`Arn` - The ARN of the db option group.

## See Also

* [aws_db_option_group](https://www.terraform.io/docs/providers/aws/r/db_option_group.html) in the _Terraform Provider Documentation_