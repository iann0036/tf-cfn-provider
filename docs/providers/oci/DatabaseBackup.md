# Terraform::OCI::DatabaseBackup

This resource provides the Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailabilityDomain` - The name of the availability domain where the database backup is stored.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`DatabaseEdition` - The Oracle Database edition of the DB system from which the database backup was taken.

`DatabaseId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.

`DatabaseSizeInGbs` - The size of the database in gigabytes at the time the backup was taken.

`DisplayName` - The user-friendly name for the backup. The name does not have to be unique.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup.

`LifecycleDetails` - Additional information about the current lifecycleState.

`State` - The current state of the backup.

`TimeEnded` - The date and time the backup was completed.

`TimeStarted` - The date and time the backup started.

`Type` - The type of backup.

## See Also

* [oci_database_backup](https://www.terraform.io/docs/providers/oci/r/database_backup.html) in the _Terraform Provider Documentation_