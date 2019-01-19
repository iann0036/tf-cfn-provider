# Terraform::Alicloud::DbInstance

Provides an RDS instance resource. A DB instance is an isolated database
environment in the cloud. A DB instance can contain multiple user-created
databases.

## Properties

`Engine` - (Required) Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.

`EngineVersion` - (Required) Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.

`DbInstanceClass` - (Deprecated) It has been deprecated from version 1.5.0 and use 'instance_type' to replace.

`InstanceType` - (Required) DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).

`DbInstanceStorage` - (Deprecated) It has been deprecated from version 1.5.0 and use 'instance_storage' to replace.

`InstanceStorage` - (Required) User-defined DB instance storage space. Value range: - [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition; - [20,1000] for MySQL 5.7 basic single node edition; - [10, 2000] for SQL Server 2008R2; - [20,2000] for SQL Server 2012 basic single node edition Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).

`InstanceName` - (Optional) The name of DB instance. It a string of 2 to 256 characters.

`InstanceChargeType` - (Optional) Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`.

`Period` - (Optional) The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.

`ZoneId` - (Optional) The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone. If it is a multi-zone and `VswitchId` is specified, the vswitch must in the one of them. The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `Terraform::Alicloud::Zones`.

`MultiAz` - (Optional) It has been deprecated from version 1.8.1, and `ZoneId` can support multiple zone.

`DbInstanceNetType` - (Deprecated) It has been deprecated from version 1.5.0. If you want to set public connection, please use new resource `Terraform::Alicloud::DbConnection`. Default to Intranet.

`AllocatePublicConnection` - (Deprecated) It has been deprecated from version 1.5.0. If you want to allocate public connection string, please use new resource `Terraform::Alicloud::DbConnection`.

`InstanceNetworkType` - (Deprecated) It has been deprecated from version 1.5.0. If you want to create instances in VPC network, this parameter must be set.

`VswitchId` - (Optional) The virtual switch ID to launch DB instances in one VPC.

`MasterUserName` - (Deprecated) It has been deprecated from version 1.5.0. New resource `Terraform::Alicloud::DbAccount` field 'name' replaces it.

`MasterUserPassword` - (Deprecated) It has been deprecated from version 1.5.0. New resource `Terraform::Alicloud::DbAccount` field 'password' replaces it.

`PreferredBackupPeriod` - (Deprecated) It has been deprecated from version 1.5.0. New resource `Terraform::Alicloud::DbBackupPolicy` field 'backup_period' replaces it.

`PreferredBackupTime` - (Deprecated) It has been deprecated from version 1.5.0. New resource `Terraform::Alicloud::DbBackupPolicy` field 'backup_time' replaces it.

`BackupRetentionPeriod` - (Deprecated) It has been deprecated from version 1.5.0. New resource `Terraform::Alicloud::DbBackupPolicy` field 'retention_period' replaces it.

`SecurityIps` - (Optional) List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).

`DbMappings` - (Deprecated) It has been deprecated from version 1.5.0. New resource `Terraform::Alicloud::DbDatabase` replaces it.


## Return Values

### Fn::GetAtt

`Id` - The RDS instance ID.

`InstanceChargeType` - The instance charge type.

`Period` - The DB instance using duration.

`Engine` - Database type.

`EngineVersion` - The database engine version.

`DbInstanceClass` - (Deprecated from version 1.5.0).

`InstanceType` - The RDS instance type.

`DbInstanceStorage` - (Deprecated from version 1.5.0).

`InstanceStorage` - The RDS instance storage space.

`InstanceName` - The name of DB instance.

`Port` - RDS database connection port.

`ConnectionString` - RDS database connection string.

`ZoneId` - The zone ID of the RDS instance.

`DbInstanceNetType` - (Deprecated from version 1.5.0).

`InstanceNetworkType` - (Deprecated from version 1.5.0).

`DbMappings` - - (Deprecated from version 1.5.0).

`PreferredBackupPeriod` - (Deprecated from version 1.5.0).

`PreferredBackupTime` - (Deprecated from version 1.5.0).

`BackupRetentionPeriod` - (Deprecated from version 1.5.0).

`SecurityIps` - Security ips of instance whitelist.

`Connections` - (Deprecated from version 1.5.0).

`VswitchId` - If the rds instance created in VPC, then this value is virtual switch ID.

`MasterUserName` - (Deprecated from version 1.5.0).

## See Also

* [alicloud_db_instance](https://www.terraform.io/docs/providers/alicloud/r/db_instance.html) in the _Terraform Provider Documentation_