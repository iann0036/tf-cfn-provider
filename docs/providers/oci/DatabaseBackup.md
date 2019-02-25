# Terraform::OCI::DatabaseBackup

This resource provides the Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.

## Properties

`DatabaseId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.

`DisplayName` - (Required) The user-friendly name for the backup. The name does not have to be unique.


## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The name of the availability domain where the database backup is stored.

`DisplayName` - The user-friendly name for the backup. The name does not have to be unique.

`TimeStarted` - The date and time the backup started.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`DatabaseEdition` - The Oracle Database edition of the DB system from which the database backup was taken.

`State` - The current state of the backup.

`TimeEnded` - The date and time the backup was completed.

`DatabaseId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.

`LifecycleDetails` - Additional information about the current lifecycleState.

`DatabaseSizeInGbs` - The size of the database in gigabytes at the time the backup was taken.

`Type` - The type of backup.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup.

## See Also

* [oci_database_backup](https://www.terraform.io/docs/providers/oci/r/database_backup.html) in the _Terraform Provider Documentation_