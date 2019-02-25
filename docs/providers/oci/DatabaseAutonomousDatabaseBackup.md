# Terraform::OCI::DatabaseAutonomousDatabaseBackup

This resource provides the Autonomous Database Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Database backup for the specified database based on the provided request parameters.

## Properties

`AutonomousDatabaseId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.

`DisplayName` - (Required) The user-friendly name for the backup. The name does not have to be unique.


## Return Values

### Fn::GetAtt

`AutonomousDatabaseId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`DisplayName` - The user-friendly name for the backup. The name does not have to be unique.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.

`IsAutomatic` - Indicates whether the backup is user-initiated or automatic.

`LifecycleDetails` - Additional information about the current lifecycle state.

`State` - The current state of the backup.

`TimeEnded` - The date and time the backup completed.

`TimeStarted` - The date and time the backup started.

`Type` - The type of backup.

## See Also

* [oci_database_autonomous_database_backup](https://www.terraform.io/docs/providers/oci/r/database_autonomous_database_backup.html) in the _Terraform Provider Documentation_