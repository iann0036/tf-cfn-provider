# Terraform::OCI::DatabaseAutonomousDataWarehouseBackup

This resource provides the Autonomous Data Warehouse Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Data Warehouse backup for the specified database based on the provided request parameters.

## Properties

`AutonomousDataWarehouseId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse backup.

`DisplayName` - (Required) The user-friendly name for the backup. The name does not have to be unique.


## Return Values

### Fn::GetAtt

`TimeEnded` - The date and time the backup completed.

`DisplayName` - The user-friendly name for the backup. The name does not have to be unique.

`TimeStarted` - The date and time the backup started.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`AutonomousDataWarehouseId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse.

`IsAutomatic` - Indicates whether the backup is user-initiated or automatic.

`State` - The current state of the backup.

`LifecycleDetails` - Additional information about the current lifecycle state.

`Type` - The type of backup.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse backup.

## See Also

* [oci_database_autonomous_data_warehouse_backup](https://www.terraform.io/docs/providers/oci/r/database_autonomous_data_warehouse_backup.html) in the _Terraform Provider Documentation_