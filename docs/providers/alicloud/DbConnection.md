# Terraform::Alicloud::DbConnection

Provides an RDS connection resource to allocate an Internet connection string for RDS instance.

~> **NOTE:** Each RDS instance will allocate a intranet connnection string automatically and its prifix is RDS instance ID.
 To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.

## Properties

`InstanceId` - (Required) The Id of instance that can run database.

`ConnectionPrefix` - (Optional) Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <instance_id> + 'tf'.

`Port` - (Optional) Internet connection port. Valid value: [3001-3999]. Default to 3306.


## Return Values

### Fn::GetAtt

`Id` - The current instance connection resource ID. Composed of instance ID and connection string with format `<instance_id>:<connection_prefix>`.

`ConnectionPrefix` - Prefix of a connection string.

`Port` - Connection instance port.

`ConnectionString` - Connection instance string.

`IpAddress` - The ip address of connection string.

## See Also

* [alicloud_db_connection](https://www.terraform.io/docs/providers/alicloud/r/db_connection.html) in the _Terraform Provider Documentation_