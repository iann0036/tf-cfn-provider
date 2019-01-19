# Terraform::Alicloud::DbConnection

Provides an RDS connection resource to allocate an Internet connection string for RDS instance.

~> **NOTE:** Each RDS instance will allocate a intranet connnection string automatically and its prifix is RDS instance ID.
 To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The current instance connection resource ID. Composed of instance ID and connection string with format `<instance_id>:<connection_prefix>`.

`ConnectionPrefix` - Prefix of a connection string.

`Port` - Connection instance port.

`ConnectionString` - Connection instance string.

`IpAddress` - The ip address of connection string.

## See Also

* [alicloud_db_connection](https://www.terraform.io/docs/providers/alicloud/r/db_connection.html) in the _Terraform Provider Documentation_