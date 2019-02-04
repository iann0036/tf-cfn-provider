# Terraform::Alicloud::DbAccount

Provides an RDS account resource and used to manage databases. A RDS instance supports multiple database account.

## Properties

`InstanceId` - (Required) The Id of instance in which account belongs.

`Name` - (Required) Operation account requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter and have no more than 16 characters.

`Password` - (Required) Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.

`Description` - (Optional) Database description. It cannot begin with https://. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.

`Type` - Privilege type of account.
- Normal: Common privilege.
- Super: High privilege.


## Return Values

### Fn::GetAtt

`Id` - The current account resource ID. Composed of instance ID and account name with format `<instance_id>:<name>`.

`InstanceId` - The Id of DB instance.

`Name` - The name of DB account.

`Description` - The account description.

`Type` - Privilege type of account.

## See Also

* [alicloud_db_account](https://www.terraform.io/docs/providers/alicloud/r/db_account.html) in the _Terraform Provider Documentation_