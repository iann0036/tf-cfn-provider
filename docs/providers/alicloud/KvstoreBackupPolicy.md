# Terraform::Alicloud::KvstoreBackupPolicy

Provides a backup policy for ApsaraDB Redis / Memcache instance resource.

## Properties

`InstanceId` - (Required) The id of ApsaraDB for Redis or Memcache intance.

`BackupTime` - (Required) Backup time, in the format of HH:mmZ- HH:mm Z.

`BackupPeriod` - (Required) Backup Cycle. Allowed values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.


## Return Values

### Fn::GetAtt

`Id` - The id of the backup policy.

`InstanceId` - The id of ApsaraDB for Redis or Memcache intance.

`BackupTime` - Backup time, in the format of HH:mmZ- HH:mm Z.

`BackupPeriod` - Backup Cycle. Allowed values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.

## See Also

* [alicloud_kvstore_backup_policy](https://www.terraform.io/docs/providers/alicloud/r/kvstore_backup_policy.html) in the _Terraform Provider Documentation_