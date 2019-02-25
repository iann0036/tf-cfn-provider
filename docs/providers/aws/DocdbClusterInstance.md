# Terraform::AWS::DocdbClusterInstance

Provides an DocDB Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a [DocDB Cluster][1].

You do not designate a primary and subsequent replicas. Instead, you simply add DocDB
Instances and DocDB manages the replication. You can use the [count][3]
meta-parameter to make multiple instances and join them all to the same DocDB
Cluster, or you may specify different Cluster Instance resources with various
`InstanceClass` sizes.

## Properties

`ApplyImmediately` - (Optional) Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

`AutoMinorVersionUpgrade` - (Optional) Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

`AvailabilityZone` - (Optional, Computed) The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonDocDB/latest/APIReference/API_CreateDBInstance.html) about the details.

`ClusterIdentifier` - (Required) The identifier of the [`Terraform::AWS::DocdbCluster`](/docs/providers/aws/r/docdb_cluster.html) in which to launch this instance.

`Engine` - (Optional) The name of the database engine to be used for the DocDB instance. Defaults to `docdb`. Valid Values: `docdb`.

`Identifier` - (Optional, Forces new resource) The indentifier for the DocDB instance, if omitted, Terraform will assign a random, unique identifier.

`IdentifierPrefix` - (Optional, Forces new resource) Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

`InstanceClass` - (Required) The instance class to use. For details on CPU and memory, see [Scaling for DocDB Instances][2]. DocDB currently
supports the below instance classes. Please see [AWS Documentation][4] for complete details.
- db.r4.large
- db.r4.xlarge
- db.r4.2xlarge
- db.r4.4xlarge
- db.r4.8xlarge
- db.r4.16xlarge.

`PreferredMaintenanceWindow` - (Optional) The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

`PromotionTier` - (Optional) Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

`Tags` - (Optional) A mapping of tags to assign to the instance.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of cluster instance.

`DbSubnetGroupName` - The DB subnet group to associate with this DB instance.

`DbiResourceId` - The region-unique, immutable identifier for the DB instance.

`Endpoint` - The DNS address for this instance. May not be writable.

`EngineVersion` - The database engine version.

`KmsKeyId` - The ARN for the KMS encryption key if one is set to the cluster.

`Port` - The database port.

`PreferredBackupWindow` - The daily time range during which automated backups are created if automated backups are enabled.

`Status` - The DocDB instance status.

`StorageEncrypted` - Specifies whether the DB cluster is encrypted.

## See Also

* [aws_docdb_cluster_instance](https://www.terraform.io/docs/providers/aws/r/docdb_cluster_instance.html) in the _Terraform Provider Documentation_