# Terraform::AWS::DbOptionGroup

Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:
* [MariaDB Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html)
* [Microsoft SQL Server Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
* [MySQL Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)
* [Oracle Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)

## Properties

`Name` - (Optional, Forces new resource) The name of the option group. If omitted, Terraform will assign a random, unique name. Must be lowercase, to match as it is stored in AWS.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`. Must be lowercase, to match as it is stored in AWS.

`OptionGroupDescription` - (Optional) The description of the option group. Defaults to "Managed by Terraform".

`EngineName` - (Required) Specifies the name of the engine that this option group should be associated with.

`MajorEngineVersion` - (Required) Specifies the major version of the engine that this option group should be associated with.

`Option` - (Optional) A list of Options to apply.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`OptionName` - (Required) The Name of the Option (e.g. MEMCACHED).

`OptionSettings` - (Optional) A list of option settings to apply.

`Port` - (Optional) The Port number when connecting to the Option (e.g. 11211).

`Version` - (Optional) The version of the option (e.g. 13.1.0.0).

`DbSecurityGroupMemberships` - (Optional) A list of DB Security Groups for which the option is enabled.

`VpcSecurityGroupMemberships` - (Optional) A list of VPC Security Groups for which the option is enabled.

`Name` - (Optional) The Name of the setting.

`Value` - (Optional) The Value of the setting.


## Return Values

### Fn::GetAtt

`Id` - The db option group name.

`Arn` - The ARN of the db option group.

## See Also

* [aws_db_option_group](https://www.terraform.io/docs/providers/aws/r/db_option_group.html) in the _Terraform Provider Documentation_