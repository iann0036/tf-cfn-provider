# Terraform::OraclePaaS::MysqlServiceInstance

The `Terraform::OraclePaaS::MysqlServiceInstance` resource creates and manages an Oracle MySQL Cloud Service instance on the Oracle Cloud Platform.

## Properties

`Name` - (Required). The name of MySQL Cloud Service instance.

`Description` - (Optional). A description of the MySQL Instance.

`SshPublicKey` - (Required). The public key for the secure shell (SSH). This key wil be used for authentication when the user logs on to the instance over SSH.

`BackupDestination` - (Required) The destination where the database backups will be stored.

`Shape` - (Required) The desired compute shape.  A shape defines the number of Oracle Compute Units (OCPUs) and amount of memory (RAM). See [About Shapes](http://www.oracle.com/pls/topic/lookup?ctx=cloud&id=OCSUG210) in _Using Oracle Compute Cloud Service_ for more information about shapes.

`MeteringFrequency` - (Optional). The billing frequency of the service instance. Allowed values are `MONTHLY` and `HOURLY`.

`Region` - (Optional). Specifies the region where the instance will be provisioned.

`AvailabilityDomain` - (Optional) Name of the availability domain within the region where the Oracle Database Cloud Service instance is to be provisioned. This is applicable only if you wish to provision to an OCI instance.

`NotificationEmail` - (Optional) The email address to send notifications around successful or unsuccessful completions of the instance-creation operation.

`IpNetwork` - (Optional) This attribute is only applicable to accounts where regions are supported. The three-part name of an IP network to which the service instance is added. For example: /Compute-identity_domain/user/object.

`VmUser` - (Optional) The user name of account to be created in the VM.

`Backups` - (Optional) Provides Cloud Storage information for how to implement service instance backups. Backups is documented below.

`MysqlConfiguration` - (Required) Specified the detail of how to configure the MySQL database. mysql_configuration is documented below.

### Backups Properties

`CloudStorageContainer` - (Required). Name of the Oracle Storage Cloud container used for store the backups.

`CloudStorageUsername` - (Required) Username for the Oracle Storage Cloud administrator.

`CloudStoragePassword` - (Required) Password for the Oracle Storage Cloud administrator.

`CreateIfMissing` - (Optional) Specifies whether to create the container if it does not exist. Default value is `false`.

### EnterpriseMonitorConfiguration Properties

`EmAgentUsername` - (Optional). Name for the Enterprise Monitor agent user.

`EmAgentPassword` - (Optional). Password for MySQL Enterprise Monitor agent.

`EmUsername` - (Optional) Name for the Enterprise Monitor Manager user.

`EmPassword` - (Optional) Password for MySQL Enterprise Monitor manager.

`EmPort` - (Optional) The port number for the MySQL Enterprise Monitor instance. The default is 18443.

### MysqlConfiguration Properties

`DbName` - (Optional). The name of the database instance. Default value is `mydatabase`.

`DbStorage` - (Optional). The storage volume sice for MySQL data. The value must be between 25 to 1024. Defaults to 25 (GB).

`MysqlCharset` - (Optional) MySQL server character set. See [Supported Character Sets and Collation](http://dev.mysql.com/doc/en/charset-charsets.html). Default value is `utf8mb4`.

`MysqlPort` - (Optional) The port number for the MySQL Server. The value must be between 3200-3399. Default value is `3306`.

`MysqlUsername` - (Optional) The Administration user for connecting to the service via th MySQL protocol. Default value is `root`.

`MysqlPassword` - (Optional) The password for the MySQL Administration user.

`SourceServiceName` - (Optional) When present, indicates that the service instance should be created as a "snapshot clone" of another service instance. Provide the name of the existing service instance whose snapshot is to be used. `DbName`, `MysqlCharset`, `MysqlCollation`, `enterpriseMonitor`, and associated MySQL server component parameters do not apply when cloning a service from a snapshot. For those parameters, the clone operation uses the values defined in the snapshot of the source service instance.

`SnapshotName` - (Optional) The name of the snapshot of the service instance specified by `SourceServiceName` that is to be used to create a "snapshot clone". This parameter is valid only if `SourceServiceName` is specified.

`EnterpriseMonitorConfiguration` - (Optional) Provides the Enterprise Monitor configuration for the MySQL Instance. If this is omitted, there will be no EM created for the MySQL Instance. `EnterpriseMonitorConfiguration` is documented below.


## See Also

* [oraclepaas_mysql_service_instance](https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance.html) in the _Terraform Provider Documentation_