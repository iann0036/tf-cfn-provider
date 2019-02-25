# Terraform::OCI::DatabaseAutonomousDatabaseBackup

This resource provides the Autonomous Database Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Database backup for the specified database based on the provided request parameters.

## Properties

`AutonomousDatabaseId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.

`DisplayName` - (Required) The user-friendly name for the backup. The name does not have to be unique.


## Return Values

### Fn::GetAtt

`TimeEnded` - The date and time the backup completed.

`DisplayName` - The user-friendly name for the backup. The name does not have to be unique.

`TimeStarted` - The date and time the backup started.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`AutonomousDatabaseId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database.

`IsAutomatic` - Indicates whether the backup is user-initiated or automatic.

`State` - The current state of the backup.

`LifecycleDetails` - Additional information about the current lifecycle state.

`Type` - The type of backup.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.

## See Also

* [oci_database_autonomous_database_backup](https://www.terraform.io/docs/providers/oci/r/database_autonomous_database_backup.html) in the _Terraform Provider Documentation_