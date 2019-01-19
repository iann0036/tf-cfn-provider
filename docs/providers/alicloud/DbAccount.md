# Terraform::Alicloud::DbAccount

Provides an RDS account resource and used to manage databases. A RDS instance supports multiple database account.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The current account resource ID. Composed of instance ID and account name with format `<instance_id>:<name>`.

`InstanceId` - The Id of DB instance.

`Name` - The name of DB account.

`Description` - The account description.

`Type` - Privilege type of account.

## See Also

* [alicloud_db_account](https://www.terraform.io/docs/providers/alicloud/r/db_account.html) in the _Terraform Provider Documentation_