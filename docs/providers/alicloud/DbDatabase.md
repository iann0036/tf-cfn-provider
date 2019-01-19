# Terraform::Alicloud::DbDatabase

Provides an RDS database resource. A DB database deployed in a DB instance. A DB instance can own multiple databases.

-> **NOTE:** This resource does not support creating 'PostgreSQL' database and
you can use [Postgresql Provider](https://www.terraform.io/docs/providers/postgresql/index.html) to do it.

-> **NOTE:** This resource does not support creating 'PPAS' database. You have to login RDS instance to create manually.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The current database resource ID. Composed of instance ID and database name with format `<instance_id>:<name>`.

`InstanceId` - The Id of DB instance.

`Name` - The name of DB database.

`CharacterSet` - Character set that database used.

`Description` - The database description.

## See Also

* [alicloud_db_database](https://www.terraform.io/docs/providers/alicloud/r/db_database.html) in the _Terraform Provider Documentation_