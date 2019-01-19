# Terraform::OCI::DatabaseDbSystem

This resource provides the Db System resource in Oracle Cloud Infrastructure Database service.

Launches a new DB system in the specified compartment and availability domain. The Oracle
Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default
options. For more information,
see [Default Options for the Initial Database](https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/launchingDB.htm#DefaultOptionsfortheInitialDatabase).

The DB System will include a command line interface (CLI) that you can use to create additional databases and
manage existing databases. For more information, see the
[Oracle Database CLI Reference](https://docs.cloud.oracle.com/iaas/Content/Database/References/dbacli.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailabilityDomain` - The name of the availability domain that the DB system is located in.

`BackupSubnetId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

`ClusterName` - The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

`CpuCoreCount` - The number of CPU cores enabled on the DB system.

`DataStoragePercentage` - The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40 and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.

`DataStorageSizeInGb` - The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.

`DatabaseEdition` - The Oracle Database edition that applies to all the databases on the DB system.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DiskRedundancy` - The type of redundancy configured for the DB system. NORMAL is 2-way redundancy. HIGH is 3-way redundancy.

`DisplayName` - The user-friendly name for the DB system. The name does not have to be unique.

`Domain` - The domain name for the DB system.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Hostname` - The hostname for the DB system.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DB system.

`LastPatchHistoryEntryId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the last patch history. This value is updated as soon as a patch operation starts.

`LicenseModel` - The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

`LifecycleDetails` - Additional information about the current lifecycleState.

`ListenerPort` - The port number configured for the listener on the DB system.

`NodeCount` - The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.

`RecoStorageSizeInGb` - The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.

`ScanDnsRecordId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DNS record for the SCAN IP addresses that are associated with the DB system.

`ScanIpIds` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Single Client Access Name (SCAN) IP addresses associated with the DB system. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster.

`Shape` - The shape of the DB system. The shape determines resources to allocate to the DB system.

`SparseDiskgroup` - True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.

`SshPublicKeys` - The public key portion of one or more key pairs used for SSH access to the DB system.

`State` - The current state of the DB system.

`SubnetId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the DB system is associated with.

`TimeCreated` - The date and time the DB system was created.

`Version` - The Oracle Database version of the DB system.

`VipIds` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the virtual IP (VIP) addresses associated with the DB system. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

## See Also

* [oci_database_db_system](https://www.terraform.io/docs/providers/oci/r/database_db_system.html) in the _Terraform Provider Documentation_