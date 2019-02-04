# Terraform::Alicloud::DbDatabase

Provides an RDS database resource. A DB database deployed in a DB instance. A DB instance can own multiple databases.

-> **NOTE:** This resource does not support creating 'PostgreSQL' database and
you can use [Postgresql Provider](https://www.terraform.io/docs/providers/postgresql/index.html) to do it.

-> **NOTE:** This resource does not support creating 'PPAS' database. You have to login RDS instance to create manually.

## Properties

`InstanceId` - (Required) The Id of instance that can run database.

`Name` - (Required) Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter
and have no more than 64 characters.

`CharacterSet` - (Required) Character set. The value range is limited to the following:
- MySQL: [ utf8, gbk, latin1, utf8mb4 ] \(`Utf8mb4` only supports versions 5.5 and 5.6\).
- SQLServer: [ Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ].

`Description` - (Optional) Database description. It cannot begin with https://. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.


## Return Values

### Fn::GetAtt

`Id` - The current database resource ID. Composed of instance ID and database name with format `<instance_id>:<name>`.

`InstanceId` - The Id of DB instance.

`Name` - The name of DB database.

`CharacterSet` - Character set that database used.

`Description` - The database description.

## See Also

* [alicloud_db_database](https://www.terraform.io/docs/providers/alicloud/r/db_database.html) in the _Terraform Provider Documentation_