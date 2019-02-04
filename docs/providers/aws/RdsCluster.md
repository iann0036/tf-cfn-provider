# Terraform::AWS::RdsCluster

Manages a [RDS Aurora Cluster][2]. To manage cluster instances that inherit configuration from the cluster (when not running the cluster in `serverless` engine mode), see the [`Terraform::AWS::RdsClusterInstance` resource](/docs/providers/aws/r/rdsClusterInstance.html). To manage non-Aurora databases (e.g. MySQL, PostgreSQL, SQL Server, etc.), see the [`awsDbInstance` resource](/docs/providers/aws/r/db_instance.html).

For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

Changes to a RDS Cluster can occur when you manually change a
parameter, such as `Port`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`ApplyImmediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `ApplyImmediately` can result in a
brief downtime as the server reboots. See the AWS Docs on [RDS Maintenance][4]
for more information.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ClusterIdentifier` - (Optional, Forces new resources) The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

`ClusterIdentifierPrefix` - (Optional, Forces new resource) Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

`DatabaseName` - (Optional) Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5].

`DeletionProtection` - (Optional) If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.

`MasterPassword` - (Required unless a `SnapshotIdentifier` is provided) Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5].

`MasterUsername` - (Required unless a `SnapshotIdentifier` is provided) Username for the master DB user. Please refer to the [RDS Naming Constraints][5].

`FinalSnapshotIdentifier` - (Optional) The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

`SkipFinalSnapshot` - (Optional) Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `FinalSnapshotIdentifier`. Default is `false`.

`AvailabilityZones` - (Optional) A list of EC2 Availability Zones that
instances in the DB cluster can be created in.

`BacktrackWindow` - (Optional) The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours).

`BackupRetentionPeriod` - (Optional) The days to retain backups for. Default `1`.

`PreferredBackupWindow` - (Optional) The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00.

`PreferredMaintenanceWindow` - (Optional) The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30.

`Port` - (Optional) The port on which the DB accepts connections.

`VpcSecurityGroupIds` - (Optional) List of VPC security groups to associate
with the Cluster.

`SnapshotIdentifier` - (Optional) Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

`StorageEncrypted` - (Optional) Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `EngineMode` and `true` for `serverless` `EngineMode`.

`ReplicationSourceIdentifier` - (Optional) ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.

`ApplyImmediately` - (Optional) Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html).

`DbSubnetGroupName` - (Optional) A DB subnet group to associate with this DB instance. **NOTE:** This must match the `DbSubnetGroupName` specified on every [`Terraform::AWS::RdsClusterInstance`](/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.

`DbClusterParameterGroupName` - (Optional) A cluster parameter group to associate with the cluster.

`KmsKeyId` - (Optional) The ARN for the KMS encryption key. When specifying `KmsKeyId`, `StorageEncrypted` needs to be set to true.

`IamRoles` - (Optional) A List of ARNs for the IAM roles to associate to the RDS Cluster.

`IamDatabaseAuthenticationEnabled` - (Optional) Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation][6] for availability and limitations.

`Engine` - (Optional) The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.

`EngineMode` - (Optional) The database engine mode. Valid values: `global`, `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.

`EngineVersion` - (Optional) The database engine version. Updating this argument results in an outage.

`SourceRegion` - (Optional) The source region for an encrypted replica DB cluster.

`EnabledCloudwatchLogsExports` - (Optional) List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`, `error`, `general`, `slowquery`.

`ScalingConfiguration` - (Optional) Nested attribute with scaling properties. Only valid when `EngineMode` is set to `serverless`. More details below.

`Tags` - (Optional) A mapping of tags to assign to the DB cluster.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of cluster.

`Id` - The RDS Cluster Identifier.

`ClusterIdentifier` - The RDS Cluster Identifier.

`ClusterResourceId` - The RDS Cluster Resource ID.

`AllocatedStorage` - The amount of allocated storage.

`AvailabilityZones` - The availability zone of the instance.

`BackupRetentionPeriod` - The backup retention period.

`PreferredBackupWindow` - The daily time range during which the backups happen.

`PreferredMaintenanceWindow` - The maintenance window.

`Endpoint` - The DNS address of the RDS instance.

`ReaderEndpoint` - A read-only endpoint for the Aurora cluster, automatically.

`Engine` - The database engine.

`EngineVersion` - The database engine version.

`MaintenanceWindow` - The instance maintenance window.

`DatabaseName` - The database name.

`Port` - The database port.

`Status` - The RDS instance status.

`MasterUsername` - The master username for the database.

`StorageEncrypted` - Specifies whether the DB cluster is encrypted.

`ReplicationSourceIdentifier` - ARN of the source DB cluster or DB instance if this DB cluster is created as a Read Replica.

`HostedZoneId` - The Route53 Hosted Zone ID of the endpoint.

## See Also

* [aws_rds_cluster](https://www.terraform.io/docs/providers/aws/r/rds_cluster.html) in the _Terraform Provider Documentation_