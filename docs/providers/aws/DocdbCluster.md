# Terraform::AWS::DocdbCluster

Manages a DocDB Cluster.

Changes to a DocDB Cluster can occur when you manually change a
parameter, such as `Port`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`ApplyImmediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `ApplyImmediately` can result in a brief downtime as the server reboots.
~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ApplyImmediately` - (Optional) Specifies whether any cluster modifications
are applied immediately, or during the next maintenance window. Default is
`false`.

`AvailabilityZones` - (Optional) A list of EC2 Availability Zones that
instances in the DB cluster can be created in.

`BackupRetentionPeriod` - (Optional) The days to retain backups for. Default `1`.

`ClusterIdentifierPrefix` - (Optional, Forces new resource) Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

`ClusterIdentifier` - (Optional, Forces new resources) The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

`DbSubnetGroupName` - (Optional) A DB subnet group to associate with this DB instance.* `db_cluster_parameter_group_name` - (Optional) A cluster parameter group to associate with the cluster.

`EnabledCloudwatchLogsExports` - (Optional) List of log types to export to cloudwatch. If omitted, no logs will be exported.
The following log types are supported: `audit`.

`EngineVersion` - (Optional) The database engine version. Updating this argument results in an outage.

`Engine` - (Optional) The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Valid Values: `docdb`.

`FinalSnapshotIdentifier` - (Optional) The name of your final DB snapshot
when this DB cluster is deleted. If omitted, no final snapshot will be
made.

`KmsKeyId` - (Optional) The ARN for the KMS encryption key. When specifying `KmsKeyId`, `StorageEncrypted` needs to be set to true.

`MasterPassword` - (Required unless a `SnapshotIdentifier` is provided) Password for the master DB user. Note that this may
show up in logs, and it will be stored in the state file. Please refer to the DocDB Naming Constraints.

`MasterUsername` - (Required unless a `SnapshotIdentifier` is provided) Username for the master DB user.

`Port` - (Optional) The port on which the DB accepts connections.

`PreferredBackupWindow` - (Optional) The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00.

`PreferredBackupWindow` - (Optional) The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00.

`SkipFinalSnapshot` - (Optional) Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `FinalSnapshotIdentifier`. Default is `false`.

`SnapshotIdentifier` - (Optional) Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.

`StorageEncrypted` - (Optional) Specifies whether the DB cluster is encrypted. The default is `false`.

`Tags` - (Optional) A mapping of tags to assign to the DB cluster.

`VpcSecurityGroupIds` - (Optional) List of VPC security groups to associate
with the Cluster.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of cluster.

`ClusterResourceId` - The DocDB Cluster Resource ID.

`Endpoint` - The DNS address of the DocDB instance.

`HostedZoneId` - The Route53 Hosted Zone ID of the endpoint.

`Id` - The DocDB Cluster Identifier.

`MaintenanceWindow` - The instance maintenance window.

`ReaderEndpoint` - A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas.

`Status` - The DocDB instance status.

## See Also

* [aws_docdb_cluster](https://www.terraform.io/docs/providers/aws/r/docdb_cluster.html) in the _Terraform Provider Documentation_