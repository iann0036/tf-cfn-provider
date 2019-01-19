# Terraform::Alicloud::DbBackupPolicy

Provides an RDS instance backup policy resource and used to configure instance backup policy.

~> **NOTE:** Each DB instance has a backup policy and it will be set default values when destroying the resource.

## Properties

`InstanceId` - (Required) The Id of instance that can run database.

`BackupPeriod` - (Optional) DB Instance backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Tuesday", "Thursday", "Saturday"].

`BackupTime` - (Optional) DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.

`RetentionPeriod` - (Optional) Instance backup retention days. Valid values: [7-730]. Default to 7.

`LogBackup` - (Optional) Whether to backup instance log. Default to true.

`LogRetentionPeriod` - (Optional) Instance log backup retention days. Valid values: [7-730]. Default to 7. It can be larger than 'retention_period'.


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