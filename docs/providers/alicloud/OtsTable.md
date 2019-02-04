# Terraform::Alicloud::OtsTable

Provides an OTS table resource.

~> **NOTE:** From Provider version 1.10.0, the provider field 'ots_instance_name' has been deprecated and
you should use resource alicloud_ots_table's new field 'instance_name' and 'table_name' to re-import this resource.

## Properties

`InstanceName` - (Required, ForceNew) The name of the OTS instance in which table will located.

`TableName` - (Required, ForceNew) The table name of the OTS instance. If changed, a new table would be created.

`PrimaryKey` - (Required, Type: List) The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `PrimaryKey` should not be less than one and not be more than four.

`Name` - (Required) Name for primary key.

`Type` - (Required, Type: list) Type for primary key. Only `Integer`, `String` or `Binary` is allowed.

`TimeToLive` - (Required) The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.

`MaxVersion` - (Required) The maximum number of versions stored in this table. The valid value is 1-2147483647.


## Return Values

### Fn::GetAtt

`Id` - The resource ID. The value is `<instance_name>:<table_name>`.

`InstanceName` - The OTS instance name.

`TableName` - The table name of the OTS which could not be changed.

`PrimaryKey` - The property of `TableMeta` which indicates the structure information of a table.

`TimeToLive` - The retention time of data stored in this table.

`MaxVersion` - The maximum number of versions stored in this table.

## See Also

* [alicloud_ots_table](https://www.terraform.io/docs/providers/alicloud/r/ots_table.html) in the _Terraform Provider Documentation_