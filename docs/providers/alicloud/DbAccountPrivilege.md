# Terraform::Alicloud::DbAccountPrivilege

Provides an RDS account privilege resource and used to grant several database some access privilege. A database can be granted by multiple account.

## Properties

`InstanceId` - (Required) The Id of instance in which account belongs.

`AccountName` - (Required) A specified account name.

`Privilege` - The privilege of one account access database. Valid values: ["ReadOnly", "ReadWrite"]. Default to "ReadOnly".

`DbNames` - (Optional) List of specified database name.


## Return Values

### Fn::GetAtt

`Id` - The current account resource ID. Composed of instance ID, account name and privilege with format `<instance_id>:<name>:<privilege>`.

`InstanceId` - The Id of DB instance.

`AccountName` - The name of DB account.

`Privilege` - The specified account privilege.

`DbNames` - List of granted privilege database names.

## See Also

* [alicloud_db_account_privilege](https://www.terraform.io/docs/providers/alicloud/r/db_account_privilege.html) in the _Terraform Provider Documentation_