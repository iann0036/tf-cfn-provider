# Terraform::OraclePaaS::DatabaseServiceInstance

The `Terraform::OraclePaaS::DatabaseServiceInstance` resource creates and manages a an Oracle Database Cloud Service instance on the Oracle Cloud Platform.

## Properties

`Name` - (Required) The name of the Service Instance.

`Edition` - (Required) Database edition for the service instance. Possible values are `SE`, `EE`, `EE_HP`, or `EE_EP`.

`Level` - (Required) Service level for the service instance. Possible values are `BASIC` or `PAAS`.

`Shape` - (Required) Desired compute shape. Possible values are `oc3`, `oc4`, `oc5`, `oc6`, `oc1m`, `oc2m`, `oc3m`, or `oc4m`.

`SubscriptionType` - (Required) Billing unit. Possible values are `HOURLY` or `MONTHLY`.

`Version` - (Required) Oracle Database software version; one of: `12.2.0.1`, `12.1.0.2`, or `11.2.0.4`.

`VmPublicKey` - (Required) Public key for the secure shell (SSH). This key will be used for authentication when connecting to the Database Cloud Service instance using an SSH client.

`DatabaseConfiguration` - (Required) Specifies the details on how to configure the database. Database configuration is documented below.

`DefaultAccessRules` - (Optional) Specifies the details on which default access rules are enable or disabled. Default Access Rules are configured below.

`DesiredState` - (Optional) Specifies the desired state of the service instance. Allowed values are `start`, `stop`, and `restart`.

`InstantiateFromBackup` - (Optional) Specify if the service instance's database should, after the instance is created, be replaced by a database stored in an existing cloud backup that was created using Oracle Database Backup Cloud Service. Instantiate from Backup is documented below.

`IpNetwork` - (Optional) This attribute is only applicable to accounts where regions are supported. The three-part name of an IP network to which the service instance is added. For example: /Compute-identity_domain/user/object.

`IpReservations` - (Optional) Groups one or more IP reservations in use on this service instance. This attribute is only applicable to accounts where regions are supported.

`Backups` - (Optional) Provides Cloud Storage information for how to implement service instance backups. Backups is documented below.

`BringYourOwnLicense` - (Optional) Specify if you want to use an existing perpetual license to Oracle Database to establish the right to use Oracle Database on the new instance. Default value is `false`.

`Description` - (Optional) A description of the Service Instance.

`HighPerformanceStorage` - (Optional) Specifies whether the service instance will be provisioned with high performance storage. Default value is `false`.

`HybridDisasteryRecovery` - (Optional) Provides information about an Oracle Hybrid Disaster Recovery configuration. Hybrid Disaster Recovery is documented below.

`NotificationEmail` - (Optional)  The email address to send notifications around successful or unsuccessful completions of the instance-creation operation.

`Region` - (Optional) Specifies the location where the service instance is provisioned (only for accounts where regions are supported).

`Standby` - (Optional) Specifies the configuration details of the standby database. This is only applicable in Oracle Cloud Infrastructure Regions. `FailoverDatabase` and `DisasterRecovery` inside the `DatabaseConfiguration` block must be set to `true`. Standby is documented below.

`Subnet` - (Optional) Name of the subnet within the region where the Oracle Database Cloud Service instance is to be provisioned.

`AdminPassword` - (Required) Password for Oracle Database administrator users sys and system. The password must meet the following requirements: Starts with a letter. Is between 8 and 30 characters long. Contains letters, at least one number, and optionally, any number of these special characters: dollar sign `$`, pound sign `#`, and underscore `_`.

`UsableStorage` - (Required) Storage size for data (in GB). Minimum value is `15`. Maximum value depends on the backup destination: if `BOTH` is specified, the maximum value is `1200`; if `OSS` or `NONE` is specified, the maximum value is `2048`.

`AvailabilityDomain` - (Optional) Name of the availability domain within the region where the Oracle Database Cloud Service instance is to be provisioned.

`BackupDestination` - (Optional) Backup Destination. Possible values are `BOTH`, `OSS`, `NONE`.This defaults to `NONE`.

`BackupStorageVolumeSize` - (Optional) The size (in GB) for the backup storage volume.

`CharacterSet` - (Optional) Character Set for the Database Cloud Service Instance. Default value is `AL32UTF8`. Supported values are:.

### CharacterSet Properties

`DataStorageVolumeSize` - (Optional) The size (in GB) for the data storage volume.

`DisasterRecovery` - (Optional) Specify if an Oracle Data Guard configuration is created using the Disaster Recovery option or the High Availability option. Default value is `false`.

`FailoverDatabase` - (Optional) Specify if an Oracle Data Guard configuration comprising a primary database and a standby database is created. Default value is `false`.

`GoldenGate` - (Optional) Specify if the database should be configured for use as the replication database of an Oracle GoldenGate Cloud Service instance. You cannot set `goldenGate` to `true` if either `IsRac` or `failoverDatabase` is set to `true`. Default value is `false`.

`IsRac` - (Optional) Specify if a cluster database using Oracle Real Application Clusters should be configured. Default value is `false`.

`NationalCharacterSet` - (Optional) National Character Set for the Database Cloud Service instance. Valid values are `AL16UTF16` and `UTF8`.

`PdbName` - (Optional) This attribute is valid when Database Cloud Service instance is configured with version 12c. Pluggable Database Name for the Database Cloud Service instance. Default value is `pdb1`.

`Sid` - (Optional) Database Name for the Database Cloud Service instance. Default value is `ORCL`.

`SourceServiceName` - (Optional) Indicates that the service instance should be created as a "snapshot clone" of another service instance. Provide the name of the existing service instance whose snapshot is to be used.

`SnapshotName` - (Optional) The name of the snapshot of the service instance specified by sourceServiceName that is to be used to create a "snapshot clone". This parameter is valid only if source_service_name is specified.

`Timezone` - (Optional) Time Zone for the Database Cloud Service instance. Default value is `UTC`.

`Type` - (Optional) Component type to which the set of parameters applies. Defaults to `db`.

`DbDemo` - (Optional) Indicates whether to include the Demos PDB.

`EnableSsh` - (Optional) Indicates whether to enable the ssh access rule.

`EnableHttp` - (Optional) Indicates whether to enable the http access rule. This is only configurable with a single instance.

`EnableHttps` - (Optional) Indiciates whether to enable the http with ssl access rule. This is only configurable with a single instance.

`EnableDbConsole` - (Optional) Indicates whether to enable the db console access rule. This is only configurable with a single instance.

`EnableDbExpress` - (Optional) Indicates whether to enable the db express access rule. This is only configurable with a single instance.

`EnableDbListener` - (Optional) Indicates whether to enable the db listener access rule. This is only configurable with a single instance.

`EnableEmConsole` - (Optional) Indicates whether to enable the em console access rule. This is only configurable with a RAC instance.

`EnableRacDbListener` - (Optional) Indicates whether to enable the rac db listene access rule. This is only configurable with a RAC instance.

`EnableScanListener` - (Optional) Indicates whether to enable the scan listener access rule. This is only configurable with a RAC instance.

`EnableRacOns` - (Optional) Indicates whether to enable the rac ons access rule. This is only configurable with a RAC instance.

`AvailabilityDomain` - (Required) Name of the availability domain within the region where the standby database of the Oracle Database Cloud Service instance is to be provisioned.

`Subnet` - (Required) Name of the subnet within the region where the standby database of the Oracle Database Cloud Service instance is to be provisioned.

`CloudStorageContainer` - (Required) Name of the Oracle Storage Cloud Service container where the existing cloud backup is stored.

`CloudStorageUsername` - (Required) Username of the Oracle Cloud user.

`CloudStoragePassword` - (Required) Password of the Oracle Cloud user specified in `ibkup_cloud_storage_user`.

`DatabaseId` - (Required) Database id of the database from which the existing cloud backup was created.

`DecryptionKey` - (Optional) Password used to create the existing, password-encrypted cloud backup. This password is used to decrypt the backup. Specify either `ibkup_decryption_key` or `ibkup_wallet_file_content` for decrypting the backup.

`OnPremise` - (Optional) Specify if the existing cloud backup being used to replace the database is from an on-premises database or another Database Cloud Service instance. The default value is false.

`ServiceId` - (Optional) Oracle Database Cloud Service instance name from which the database of new Oracle Database Cloud Service instance should be created. This value is required if `OnPremise` is set to true.

`WalletFileContent` - (Optional) String containing the xsd:base64Binary representation of the cloud backup's wallet file. This wallet is used to decrypt the backup. Specify either `ibkup_decryption_key` or `ibkup_wallet_file_content` for decrypting the backup.

`CloudStorageContainer` - (Required) Name of the Oracle Storage Cloud Service container used to provide storage for your service instance backups. Use the following format to specify the container name: `<storageservicename>-<storageidentitydomain>/<containername>`.

`CloudStorageUsername` - (Required) Username for the Oracle Storage Cloud Service administrator.

`CloudStoragePassword` - (Required) Password for the Oracle Storage Cloud Service administrator.

`CreateIfMissing` - (Optional) Specify if the given cloud_storage_container is to be created if it does not already exist. Default value is `false`.

`CloudStorageContainer` - (Required) Name of the Oracle Storage Cloud Service container where the backup from on-premise instance is stored. Use the following format to specify the container name: `<storageservicename>-<storageidentitydomain>/<containername>`.

`CloudStorageUsername` - (Required) Username for the Oracle Storage Cloud Service administrator.

`CloudStoragePassword` - (Required) Password for the Oracle Storage Cloud Service administrator.

`ComputeSiteName` - The Oracle Cloud location housing the service instance.

`DbaasMonitorUrl` - The URL to use to connect to Oracle DBaaS Monitor on the service instance.

`EmUrl` - The URL to use to connect to Enterprise Manager on the service instance.

`GlassfishUrl` - The URL to use to connect to the Oracle GlassFish Server Administration Console on the service instance.

`IdentityDomain` - The identity domain housing the service instance.

`Status` - The status of the service instance.

`Uri` - The Uniform Resource Identifier for the Service Instance.


## See Also

* [oraclepaas_database_service_instance](https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance.html) in the _Terraform Provider Documentation_