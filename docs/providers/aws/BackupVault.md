# Terraform::AWS::BackupVault

Provides an AWS Backup vault resource.

## Properties

`Name` - (Required) Name of the backup vault to create.

`Tags` - (Optional) Metadata that you can assign to help organize the resources that you create.

`KmsKeyArn` - (Optional) The server-side encryption key that is used to protect your backups.


## Return Values

### Fn::GetAtt

`Id` - The name of the vault.

`Arn` - The ARN of the vault.

`RecoveryPoints` - The number of recovery points that are stored in a backup vault.

## See Also

* [aws_backup_vault](https://www.terraform.io/docs/providers/aws/r/backup_vault.html) in the _Terraform Provider Documentation_