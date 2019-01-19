# Terraform::Alicloud::OtsTable

Provides an OTS table resource.

~> **NOTE:** From Provider version 1.10.0, the provider field 'ots_instance_name' has been deprecated and
you should use resource alicloud_ots_table's new field 'instance_name' and 'table_name' to re-import this resource.

## Properties

TBC

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