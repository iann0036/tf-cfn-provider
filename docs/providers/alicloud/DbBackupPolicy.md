# Terraform::Alicloud::DbBackupPolicy

Provides an RDS instance backup policy resource and used to configure instance backup policy.

~> **NOTE:** Each DB instance has a backup policy and it will be set default values when destroying the resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The current backup policy resource ID. It is same as 'instance_id'.

`InstanceId` - The Id of DB instance.

`BackupPeriod` - DB Instance backup period.

`BackupTime` - DB instance backup time.

`RetentionPeriod` - Instance backup retention days.

`LogBackup` - Whether to backup instance log.

`LogRetentionPeriod` - Instance log backup retention days.

## See Also

* [alicloud_db_backup_policy](https://www.terraform.io/docs/providers/alicloud/r/db_backup_policy.html) in the _Terraform Provider Documentation_