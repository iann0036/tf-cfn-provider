# Terraform::FlexibleEngine::CsbsBackupPolicyV1

Provides an FlexibleEngine Backup Policy of Resources.

## Properties

`Name` - (Required) Specifies backup object name.

`Description` - (Optional) Specifies Scheduling period description.The value consists of 0 to 255 characters and must not contain a greater-than sign (>) or less-than sign (<).

`ProviderId` - (Required) Specifies backup provider ID. Default value is **fc4d5750-22e7-4798-8a46-f48f62c4c1da**.

`Common` - (Optional) General backup policy parameters, which are blank by default.

`Enabled` - (Optional) Specifies whether the scheduling period is enabled. Default value is **true**.

`MaxBackups` - (Optional) Specifies maximum number of backups that can be automatically created for a backup object.

`RetentionDurationDays` - (Optional) Specifies duration of retaining a backup, in days.

`Permanent` - (Optional) Specifies whether backups are permanently retained.

`TriggerPattern` - (Required) Specifies Scheduling policy of the scheduler.

`OperationType` - (Required) Specifies Operation type, which can be backup.

`Id` - (Required) Specifies the ID of the object to be backed up.

`Type` - (Required) Entity object type of the backup object. If the type is VMs, the value is **OS::Nova::Server**.


## Return Values

### Fn::GetAtt

`Status` - Status of Backup Policy.

`Id` -  Specifies Scheduling period ID.

`TriggerId` -  Specifies Scheduler ID.

`TriggerName` -  Specifies Scheduler name.

`TriggerType` -  Specifies Scheduler type.

## See Also

* [flexibleengine_csbs_backup_policy_v1](https://www.terraform.io/docs/providers/flexibleengine/r/csbs_backup_policy_v1.html) in the _Terraform Provider Documentation_