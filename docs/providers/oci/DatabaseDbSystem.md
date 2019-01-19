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

## Properties

`AvailabilityDomain` - (Required) The availability domain where the DB system is located.

`BackupSubnetId` - (Optional) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

`ClusterName` - (Optional) The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

`CompartmentId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment the DB system  belongs in.

`CpuCoreCount` - (Required) (Updatable) The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape: * BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. * BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. * Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. * Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. * Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. * Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. * Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. * Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

`DataStoragePercentage` - (Optional) The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.

`DataStorageSizeInGb` - (Optional) (Updatable) Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.

`DatabaseEdition` - (Required) The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

`DbHome` - (Required) * `Database` - (Required) * `AdminPassword` - (Required) A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \#, or -. * `BackupId` - (Required when source=DB_BACKUP) The backup [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). * `BackupTdePassword` - (Required when source=DB_BACKUP) The password to open the TDE wallet. * `CharacterSet` - (Applicable when source=NONE) The character set for the database.  The default is AL32UTF8. Allowed values are:.

`Database` - (Required) * `AdminPassword` - (Required) A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \#, or -. * `BackupId` - (Required when source=DB_BACKUP) The backup [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). * `BackupTdePassword` - (Required when source=DB_BACKUP) The password to open the TDE wallet. * `CharacterSet` - (Applicable when source=NONE) The character set for the database.  The default is AL32UTF8. Allowed values are:.

`AdminPassword` - (Required) A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \#, or -. * `BackupId` - (Required when source=DB_BACKUP) The backup [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). * `BackupTdePassword` - (Required when source=DB_BACKUP) The password to open the TDE wallet. * `CharacterSet` - (Applicable when source=NONE) The character set for the database.  The default is AL32UTF8. Allowed values are:.

`BackupId` - (Required when source=DB_BACKUP) The backup [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). * `BackupTdePassword` - (Required when source=DB_BACKUP) The password to open the TDE wallet. * `CharacterSet` - (Applicable when source=NONE) The character set for the database.  The default is AL32UTF8. Allowed values are:.

`BackupTdePassword` - (Required when source=DB_BACKUP) The password to open the TDE wallet. * `CharacterSet` - (Applicable when source=NONE) The character set for the database.  The default is AL32UTF8. Allowed values are:.

`CharacterSet` - (Applicable when source=NONE) The character set for the database.  The default is AL32UTF8. Allowed values are:.

### CharacterSet Properties

`DbBackupConfig` - (Applicable when source=NONE) * `AutoBackupEnabled` - (Applicable when source=NONE) If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work. * `DbName` - (Required when source=NONE) The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. * `DbWorkload` - (Applicable when source=NONE) The database workload type. * `DefinedTags` - (Applicable when source=NONE) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}` * `FreeformTags` - (Applicable when source=NONE) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` * `NcharacterSet` - (Applicable when source=NONE) The national character set for the database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8. * `PdbName` - (Applicable when source=NONE) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. * `DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`AutoBackupEnabled` - (Applicable when source=NONE) If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work. * `DbName` - (Required when source=NONE) The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. * `DbWorkload` - (Applicable when source=NONE) The database workload type. * `DefinedTags` - (Applicable when source=NONE) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}` * `FreeformTags` - (Applicable when source=NONE) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` * `NcharacterSet` - (Applicable when source=NONE) The national character set for the database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8. * `PdbName` - (Applicable when source=NONE) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. * `DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`DbName` - (Required when source=NONE) The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. * `DbWorkload` - (Applicable when source=NONE) The database workload type. * `DefinedTags` - (Applicable when source=NONE) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}` * `FreeformTags` - (Applicable when source=NONE) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` * `NcharacterSet` - (Applicable when source=NONE) The national character set for the database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8. * `PdbName` - (Applicable when source=NONE) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. * `DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`DbWorkload` - (Applicable when source=NONE) The database workload type. * `DefinedTags` - (Applicable when source=NONE) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}` * `FreeformTags` - (Applicable when source=NONE) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}` * `NcharacterSet` - (Applicable when source=NONE) The national character set for the database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8. * `PdbName` - (Applicable when source=NONE) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. * `DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`NcharacterSet` - (Applicable when source=NONE) The national character set for the database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8. * `PdbName` - (Applicable when source=NONE) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. * `DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`PdbName` - (Applicable when source=NONE) The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. * `DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`DbVersion` - (Required when source=NONE) A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions](https://docs.cloud.oracle.com/iaas/api/#/en/database/20160918/DbVersion/ListDbVersions) operation. * `DisplayName` - (Optional) The user-provided name of the database home.

`DisplayName` - (Optional) The user-friendly name for the DB system. The name does not have to be unique.

`DiskRedundancy` - (Optional) The type of redundancy configured for the DB system. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.

`Domain` - (Optional) A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.

`Hostname` - (Required) The hostname for the DB system. The hostname must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).

`LicenseModel` - (Optional) The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED. Allowed values are: LICENSE_INCLUDED, BRING_YOUR_OWN_LICENSE.

`NodeCount` - (Optional) The number of nodes to launch for a 2-node RAC virtual machine DB system.

`Shape` - (Required) The shape of the DB system. The shape determines resources allocated to the DB system. * For virtual machine shapes, the number of CPU cores and memory * For bare metal and Exadata shapes, the number of CPU cores, memory, and storage.

`Source` - (Optional) The source of the database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a backup. The default is NONE.

`SparseDiskgroup` - (Optional) If true, Sparse Diskgroup is configured for Exadata dbsystem. If False, Sparse diskgroup is not configured.

`SshPublicKeys` - (Required) (Updatable) The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.

`SubnetId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the DB system is associated with.


## Return Values

### Fn::GetAtt

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