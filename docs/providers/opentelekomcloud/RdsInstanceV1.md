# Terraform::OpenTelekomCloud::RdsInstanceV1

Manages rds instance resource within OpenTelekomCloud

## Properties

`Name` - (Required) Specifies the DB instance name. The DB instance name of the same type is unique in the same tenant. The changes of the instance name will be suppressed in HA scenario.

`Datastore` - (Required) Specifies database information. The structure is described below.

`Flavorref` - (Required) Specifies the specification ID (flavors.id in the response message in Obtaining All DB Instance Specifications). If you want to enable ha for the rds instance, a flavor with ha speccode is required.

`Volume` - (Required) Specifies the volume information. The structure is described below.

`Region` - (Required) Specifies the region ID.

`Availabilityzone` - (Required) Specifies the ID of the AZ.

`Vpc` - (Required) Specifies the VPC ID. For details about how to obtain this parameter value, see section "Virtual Private Cloud" in the Virtual Private Cloud API Reference.

`Nics` - (Required) Specifies the nics information. For details about how to obtain this parameter value, see section "Subnet" in the Virtual Private Cloud API Reference. The structure is described below.

`Securitygroup` - (Required) Specifies the security group which the RDS DB instance belongs to. The structure is described below.

`Dbport` - (Optional) Specifies the database port number.

`Backupstrategy` - (Optional) Specifies the advanced backup policy. The structure is described below.

`Dbrtpd` - (Required) Specifies the password for user root of the database.

`Ha` - (Optional) Specifies the parameters configured on HA and is used when creating HA DB instances. The structure is described below. NOTICE: RDS for Microsoft SQL Server does not support creating HA DB instances and this parameter is not involved.

### Datastore Properties

`Version` - (Required) Specifies the DB instance version.

### Volume Properties

`Type` - (Required) Specifies the volume type. Valid value: It must be COMMON (SATA) or ULTRAHIGH (SSD) and is case-sensitive.

`Size` - (Required) Specifies the volume size. Its value must be a multiple of 10 and the value range is 100 GB to 2000 GB.

### Ha Properties

`Enable` - (Optional) Specifies the configured parameters on the HA. Valid value: The value is true or false. The value true indicates creating HA DB instances. The value false indicates creating a single DB instance.

`Replicationmode` - (Optional) Specifies the replication mode for the standby DB instance. The value cannot be empty. For MySQL, the value is async or semisync. For PostgreSQL, the value is async or sync.

### Nics Properties

`SubnetId` - (Required) Specifies the subnet ID obtained from the VPC.

`Id` - (Required) Specifies the ID obtained from the securitygroup.

`Starttime` - (Optional) Indicates the backup start time that has been set. The backup task will be triggered within one hour after the backup start time. Valid value: The value cannot be empty. It must use the hh:mm:ss format and must be valid. The current time is the UTC time.

`Keepdays` - (Optional) Specifies the number of days to retain the generated backup files. Its value range is 0 to 35. If this parameter is not specified or set to 0, the automated backup policy is disabled.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Flavorref` - See Properties above.

`Volume` - See Properties above.

`Availabilityzone` - See Properties above.

`Vpc` - See Properties above.

`Nics` - See Properties above.

`Securitygroup` - See Properties above.

`Dbport` - See Properties above.

`Backupstrategy` - See Properties above.

`Dbrtpd` - See Properties above.

`Ha` - See Properties above.

`Status` - Indicates the DB instance status.

`Hostname` - Indicates the instance connection address. It is a blank string.

`Type` - Indicates the DB instance type, which can be master or readreplica.

`Created` - Indicates the creation time in the following format: yyyy-mm-dd Thh:mm:ssZ.

`Updated` - Indicates the update time in the following format: yyyy-mm-dd Thh:mm:ssZ.

`Volume.size` - See Properties above.

## See Also

* [opentelekomcloud_rds_instance_v1](https://www.terraform.io/docs/providers/opentelekomcloud/r/rds_instance_v1.html) in the _Terraform Provider Documentation_