# Terraform::Alicloud::DbReadWriteSplittingConnection

Provides an RDS read write splitting connection resource to allocate an Intranet connection string for RDS instance.

## Properties

`InstanceId` - (Required, ForceNew) The Id of instance that can run database.

`DistributionType` - (Required) Read weight distribution mode. Values are as follows: `Standard` indicates automatic weight distribution based on types, `Custom` indicates custom weight distribution.

`ConnectionPrefix` - (Optional, ForceNew) Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <instance_id> + 'rw'.

`Port` - (Optional) Intranet connection port. Valid value: [3001-3999]. Default to 3306.

`MaxDelayTime` - (Optional) Delay threshold, in seconds. The value range is 0 to 7200. Default to 30. Read requests are not routed to the read-only instances with a delay greater than the threshold.

`Weight` - (Optional) Read weight distribution. Read weights increase at a step of 100 up to 10,000. Enter weights in the following format: {"Instanceid":"Weight","Instanceid":"Weight"}. This parameter must be set when distribution_type is set to Custom.


## Return Values

### Fn::GetAtt

`Id` - The Id of DB instance.

`ConnectionString` - Connection instance string.

## See Also

* [alicloud_db_read_write_splitting_connection](https://www.terraform.io/docs/providers/alicloud/r/db_read_write_splitting_connection.html) in the _Terraform Provider Documentation_