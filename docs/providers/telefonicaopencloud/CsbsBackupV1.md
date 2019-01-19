# Terraform::TelefonicaOpenCloud::CsbsBackupV1

Provides an TelefonicaOpenCloud Backup of Resources.

## Properties

`BackupName` - (Optional) Name for the backup. The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-). Changing backup_name creates a new backup.

`Description` - (Optional) Backup description. The value consists of 0 to 255 characters and must not contain a greater-than sign (>) or less-than sign (<). Changing description creates a new backup.

`ResourceId` - (Required) ID of the target to which the backup is restored. Changing this creates a new backup.

`ResourceType` - (Optional) Type of the target to which the backup is restored. The default value is **OS::Nova::Server** for an ECS. Changing this creates a new backup.


## Return Values

### Fn::GetAtt

`Status` -  Status of backup Volume.

`BackupRecordId` - Specifies backup record ID.

`SpaceSavingRatio` -  Specifies space saving rate.

`Name` - Name of backup data.

`Bootable` -  Specifies whether the disk is bootable.

`AverageSpeed` -  Specifies the average speed.

`SourceVolumeSize` -  Shows source volume size in GB.

`SourceVolumeId` -  It specifies source volume ID.

`Incremental` -  Shows whether incremental backup is used.

`SnapshotId` -  ID of snapshot.

`SourceVolumeName` -  Specifies source volume name.

`ImageType` - Specifies image type.

`Id` -  Specifies Cinder backup ID.

`Size` -  Specifies accumulated size (MB) of backups.

`Eip` - Specifies elastic IP address of the ECS.

`CloudServiceType` - Specifies ECS type.

`Ram` - Specifies memory size of the ECS, in MB.

`Vcpus` - Specifies CPU cores corresponding to the ECS.

`PrivateIp` - It specifies internal IP address of the ECS.

`Disk` - Shows system disk size corresponding to the ECS specifications.

## See Also

* [telefonicaopencloud_csbs_backup_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/csbs_backup_v1.html) in the _Terraform Provider Documentation_