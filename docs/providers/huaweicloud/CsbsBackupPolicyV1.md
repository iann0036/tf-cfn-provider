# Terraform::HuaweiCloud::CsbsBackupPolicyV1

Provides an HuaweiCloud Backup Policy of Resources.

## Properties

`Name` - (Required) Specifies the name of backup policy. The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).

`Description` - (Optional) Backup policy description. The value consists of 0 to 255 characters and must not contain a greater-than sign (>) or less-than sign (<).

`ProviderId` - (Required) Specifies backup provider ID. Default value is **fc4d5750-22e7-4798-8a46-f48f62c4c1da**.

`Common` - (Optional) General backup policy parameters, which are blank by default.

### ScheduledOperation Properties

`Name` - (Optional) Specifies Scheduling period name.The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).

`Description` - (Optional) Specifies Scheduling period description.The value consists of 0 to 255 characters and must not contain a greater-than sign (>) or less-than sign (<).

`Enabled` - (Optional) Specifies whether the scheduling period is enabled. Default value is **true**.

`MaxBackups` - (Optional) Specifies maximum number of backups that can be automatically created for a backup object.

`RetentionDurationDays` - (Optional) Specifies duration of retaining a backup, in days.

`Permanent` - (Optional) Specifies whether backups are permanently retained.

`TriggerPattern` - (Required) Specifies Scheduling policy of the scheduler.

`OperationType` - (Required) Specifies Operation type, which can be backup.

### Resource Properties

`Id` - (Required) Specifies the ID of the object to be backed up.

`Type` - (Required) Entity object type of the backup object. If the type is VMs, the value is **OS::Nova::Server**.

`Name` - (Required) Specifies backup object name.


## Return Values

### Fn::GetAtt

`Status` - Status of Backup Policy.

`Id` -  Specifies Scheduling period ID.

`TriggerId` -  Specifies Scheduler ID.

`TriggerName` -  Specifies Scheduler name.

`TriggerType` -  Specifies Scheduler type.

## See Also

* [huaweicloud_csbs_backup_policy_v1](https://www.terraform.io/docs/providers/huaweicloud/r/csbs_backup_policy_v1.html) in the _Terraform Provider Documentation_