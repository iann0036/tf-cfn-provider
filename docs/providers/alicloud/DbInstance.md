# Terraform::Alicloud::DbInstance

Provides an RDS instance resource. A DB instance is an isolated database
environment in the cloud. A DB instance can contain multiple user-created
databases.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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