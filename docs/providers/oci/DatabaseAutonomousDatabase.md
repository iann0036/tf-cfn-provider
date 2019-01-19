# Terraform::OCI::DatabaseAutonomousDatabase

This resource provides the Autonomous Database resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Database.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`ConnectionStrings` - The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.

`AllConnectionStrings` - All connection strings to use to connect to the Autonomous Database.

`High` - The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.

`Low` - The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.

`Medium` - The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.

`CpuCoreCount` - The number of CPU cores to be made available to the database.

`DataStorageSizeInTbs` - The quantity of data in the database, in terabytes.

`DbName` - The database name.

`DbVersion` - A valid Oracle Database version for Autonomous Database.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - The user-friendly name for the Autonomous Database. The name does not have to be unique.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Database.

`LicenseModel` - The Oracle license model that applies to the Oracle Autonomous Database. The default is BRING_YOUR_OWN_LICENSE.

`LifecycleDetails` - Information about the current lifecycle state.

`ServiceConsoleUrl` - The URL of the Service Console for the Autonomous Database.

`State` - The current state of the database.

`TimeCreated` - The date and time the database was created.

## See Also

* [oci_database_autonomous_database](https://www.terraform.io/docs/providers/oci/r/database_autonomous_database.html) in the _Terraform Provider Documentation_