# Terraform::OCI::DatabaseAutonomousDataWarehouseBackup

This resource provides the Autonomous Data Warehouse Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Data Warehouse backup for the specified database based on the provided request parameters.

## Properties

`AutonomousDataWarehouseId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse backup.

`DisplayName` - (Required) The user-friendly name for the backup. The name does not have to be unique.


## Return Values

### Fn::GetAtt

`AutonomousDataWarehouseId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`DisplayName` - The user-friendly name for the backup. The name does not have to be unique.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse backup.

`IsAutomatic` - Indicates whether the backup is user-initiated or automatic.

`LifecycleDetails` - Additional information about the current lifecycle state.

`State` - The current state of the backup.

`TimeEnded` - The date and time the backup completed.

`TimeStarted` - The date and time the backup started.

`Type` - The type of backup.

## See Also

* [oci_database_autonomous_data_warehouse_backup](https://www.terraform.io/docs/providers/oci/r/database_autonomous_data_warehouse_backup.html) in the _Terraform Provider Documentation_