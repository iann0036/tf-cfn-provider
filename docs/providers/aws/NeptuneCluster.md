# Terraform::AWS::NeptuneCluster

Provides an Neptune Cluster Resource. A Cluster Resource defines attributes that are
applied to the entire cluster of Neptune Cluster Instances.

Changes to a Neptune Cluster can occur when you manually change a
parameter, such as `BackupRetentionPeriod`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`ApplyImmediately` flag to instruct the service to apply the change immediately
(see documentation below).

## Properties

`ApplyImmediately` - (Optional) Specifies whether any cluster modifications are applied immediately, or during the next maintenance window. Default is `false`.

`AvailabilityZones` - (Optional) A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.

`BackupRetentionPeriod` - (Optional) The days to retain backups for. Default `1`.

`ClusterIdentifier` - (Optional, Forces new resources) The cluster identifier. If omitted, Terraform will assign a random, unique identifier.

`ClusterIdentifierPrefix` - (Optional, Forces new resource) Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.

`Engine` - (Optional) The name of the database engine to be used for this Neptune cluster. Defaults to `neptune`.

`EngineVersion` - (Optional) The database engine version.

`FinalSnapshotIdentifier` - (Optional) The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted, no final snapshot will be made.

`IamRoles` - (Optional) A List of ARNs for the IAM roles to associate to the Neptune Cluster.

`IamDatabaseAuthenticationEnabled` - (Optional) Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.

`KmsKeyArn` - (Optional) The ARN for the KMS encryption key. When specifying `KmsKeyArn`, `StorageEncrypted` needs to be set to true.

`NeptuneSubnetGroupName` - (Optional) A Neptune subnet group to associate with this Neptune instance.

`NeptuneClusterParameterGroupName` - (Optional) A cluster parameter group to associate with the cluster.

`PreferredBackupWindow` - (Optional) The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00.

`PreferredMaintenanceWindow` - (Optional) The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30.

`Port` - (Optional) The port on which the Neptune accepts connections. Default is `8182`.

`ReplicationSourceIdentifier` - (Optional) ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be created as a Read Replica.

`SkipFinalSnapshot` - (Optional) Determines whether a final Neptune snapshot is created before the Neptune cluster is deleted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot is created before the Neptune cluster is deleted, using the value from `FinalSnapshotIdentifier`. Default is `false`.

`SnapshotIdentifier` - (Optional) Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot.

`StorageEncrypted` - (Optional) Specifies whether the Neptune cluster is encrypted. The default is `false` if not specified.

`Tags` - (Optional) A mapping of tags to assign to the Neptune cluster.

`VpcSecurityGroupIds` - (Optional) List of VPC security groups to associate with the Cluster.


## Return Values

### Fn::GetAtt

`Arn` - The Neptune Cluster Amazon Resource Name (ARN).

`ClusterResourceId` - The Neptune Cluster Resource ID.

`Endpoint` - The DNS address of the Neptune instance.

`HostedZoneId` - The Route53 Hosted Zone ID of the endpoint.

`Id` - The Neptune Cluster Identifier.

`ReaderEndpoint` - A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas.

`Status` - The Neptune instance status.

## See Also

* [aws_neptune_cluster](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in the _Terraform Provider Documentation_