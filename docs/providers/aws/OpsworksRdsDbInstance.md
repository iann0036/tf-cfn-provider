# Terraform::AWS::OpsworksRdsDbInstance

Provides an OpsWorks RDS DB Instance resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The computed id. Please note that this is only used internally to identify the stack <-> instance relation. This value is not used in aws.

## See Also

* [aws_opsworks_rds_db_instance](https://www.terraform.io/docs/providers/aws/r/opsworks_rds_db_instance.html) in the _Terraform Provider Documentation_