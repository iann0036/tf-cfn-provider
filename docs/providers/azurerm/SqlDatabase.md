# Terraform::AzureRM::SqlDatabase

Allows you to manage an Azure SQL Database

## Properties

`Name` - (Required) The name of the database.

`ResourceGroupName` - (Required) The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ServerName` - (Required) The name of the SQL Server on which to create the database.

`CreateMode` - (Optional) Specifies the type of database to create. Defaults to `Default`. See below for the accepted values/.

`Import` - (Optional) A Database Import block as documented below. `CreateMode` must be set to `Default`.

`SourceDatabaseId` - (Optional) The URI of the source database if `CreateMode` value is not `Default`.

`RestorePointInTime` - (Optional) The point in time for the restore. Only applies if `CreateMode` is `PointInTimeRestore` e.g. 2013-11-08T22:00:40Z.

`Edition` - (Optional) The edition of the database to be created. Applies only if `CreateMode` is `Default`. Valid values are: `Basic`, `Standard`, `Premium`, or `DataWarehouse`. Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

`Collation` - (Optional) The name of the collation. Applies only if `CreateMode` is `Default`.  Azure default is `SQL_LATIN1_GENERAL_CP1_CI_AS`. Changing this forces a new resource to be created.

`MaxSizeBytes` - (Optional) The maximum size that the database can grow to. Applies only if `CreateMode` is `Default`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

`RequestedServiceObjectiveId` - (Optional) Use `RequestedServiceObjectiveId` or `RequestedServiceObjectiveName` to set the performance level for the database. Valid values are: `S0`, `S1`, `S2`, `S3`, `P1`, `P2`, `P4`, `P6`, `P11` and `ElasticPool`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

`RequestedServiceObjectiveName` - (Optional) Use `RequestedServiceObjectiveName` or `RequestedServiceObjectiveId` to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

`SourceDatabaseDeletionDate` - (Optional) The deletion date time of the source database. Only applies to deleted databases where `CreateMode` is `PointInTimeRestore`.

`ElasticPoolName` - (Optional) The name of the elastic database pool.

`ThreatDetectionPolicy` - (Optional) Threat detection policy configuration. The `ThreatDetectionPolicy` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Import Properties

`StorageUri` - (Required) Specifies the blob URI of the .bacpac file.

`StorageKey` - (Required) Specifies the access key for the storage account.

`StorageKeyType` - (Required) Specifies the type of access key for the storage account. Valid values are `StorageAccessKey` or `SharedAccessKey`.

`AdministratorLogin` - (Required) Specifies the name of the SQL administrator.

`AdministratorLoginPassword` - (Required) Specifies the password of the SQL administrator.

`AuthenticationType` - (Required) Specifies the type of authentication used to access the server. Valid values are `SQL` or `ADPassword`.

`OperationMode` - (Optional) Specifies the type of import operation being performed. The only allowable value is `Import`.

### ThreatDetectionPolicy Properties

`State` - (Required) The State of the Policy. Possible values are `Enabled`, `Disabled` or `New`.

`DisabledAlerts` - (Optional) Specifies a list of alerts which should be disabled. Possible values include `Access_Anomaly`, `Sql_Injection` and `Sql_Injection_Vulnerability`.

`EmailAccountAdmins` - (Optional) Should the account administrators be emailed when this alert is triggered?.

`EmailAddresses` - (Optional) A list of email addresses which alerts should be sent to.

`RetentionDays` - (Optional) Specifies the number of days to keep in the Threat Detection audit logs.

`StorageAccountAccessKey` - (Optional) Specifies the identifier key of the Threat Detection audit storage account. Required if `State` is `Enabled`.

`StorageEndpoint` - (Optional) Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs. Required if `State` is `Enabled`.

`UseServerDefault` - (Optional) Should the default server policy be used? Defaults to `Disabled`.


## Return Values

### Fn::GetAtt

`Id` - The SQL Database ID.

`CreationDate` - The creation date of the SQL Database.

`DefaultSecondaryLocation` - The default secondary location of the SQL Database.

## See Also

* [azurerm_sql_database](https://www.terraform.io/docs/providers/azurerm/r/sql_database.html) in the _Terraform Provider Documentation_