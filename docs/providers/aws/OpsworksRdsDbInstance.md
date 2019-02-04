# Terraform::AWS::OpsworksRdsDbInstance

Provides an OpsWorks RDS DB Instance resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`StackId` - (Required) The stack to register a db instance for. Changing this will force a new resource.

`RdsDbInstanceArn` - (Required) The db instance to register for this stack. Changing this will force a new resource.

`DbUser` - (Required) A db username.

`DbPassword` - (Required) A db password.


## Return Values

### Fn::GetAtt

`Id` - The computed id. Please note that this is only used internally to identify the stack <-> instance relation. This value is not used in aws.

## See Also

* [aws_opsworks_rds_db_instance](https://www.terraform.io/docs/providers/aws/r/opsworks_rds_db_instance.html) in the _Terraform Provider Documentation_