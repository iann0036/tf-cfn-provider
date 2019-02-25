# Terraform::Alicloud::DbReadonlyInstance

Provides an RDS readonly instance resource.

## Properties

`EngineVersion` - (Required, ForceNew) Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.

`MasterDbInstanceId` - (Required, ForceNew) ID of the master instance.

`InstanceType` - (Required) DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).

`InstanceStorage` - (Required) User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).

`InstanceName` - (Optional) The name of DB instance. It a string of 2 to 256 characters.

`Parameters` - (Optional) Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm).

`ZoneId` - (Optional, ForceNew) The Zone to launch the DB instance.

`VswitchId` - (Optional, ForceNew) The virtual switch ID to launch DB instances in one VPC.


## Return Values

### Fn::GetAtt

`Id` - The RDS instance ID.

`Engine` - Database type.

`Port` - RDS database connection port.

`ConnectionString` - RDS database connection string.

## See Also

* [alicloud_db_readonly_instance](https://www.terraform.io/docs/providers/alicloud/r/db_readonly_instance.html) in the _Terraform Provider Documentation_