# Terraform::AWS::RdsClusterInstance

Provides an RDS Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a [RDS Cluster][3],
specifically running Amazon Aurora.

Unlike other RDS resources that support replication, with Amazon Aurora you do
not designate a primary and subsequent replicas. Instead, you simply add RDS
Instances and Aurora manages the replication. You can use the [count][5]
meta-parameter to make multiple instances and join them all to the same RDS
Cluster, or you may specify different Cluster Instance resources with various
`InstanceClass` sizes.

For more information on Amazon Aurora, see [Aurora on Amazon RDS][2] in the Amazon RDS User Guide.

~> **NOTE:** Deletion Protection from the RDS service can only be enabled at the cluster level, not for individual cluster instances. You can still add the [`prevent_destroy` lifecycle behavior](https://www.terraform.io/docs/configuration/resources.html#prevent_destroy) to your Terraform resource configuration if you desire protection from accidental deletion.

## Properties

`Identifier` - (Optional, Forces new resource) The indentifier for the RDS instance, if omitted, Terraform will assign a random, unique identifier.

`IdentifierPrefix` - (Optional, Forces new resource) Creates a unique identifier beginning with the specified prefix. Conflicts with `Identifier`.

`ClusterIdentifier` - (Required) The identifier of the [`Terraform::AWS::RdsCluster`](/docs/providers/aws/r/rds_cluster.html) in which to launch this instance.

`Engine` - (Optional) The name of the database engine to be used for the RDS instance. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`.
For information on the difference between the available Aurora MySQL engines
see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
in the Amazon RDS User Guide.

`EngineVersion` - (Optional) The database engine version.

`InstanceClass` - (Required) The instance class to use. For details on CPU
and memory, see [Scaling Aurora DB Instances][4]. Aurora currently
supports the below instance classes. Please see [AWS Documentation][7] for complete details.
- db.t2.small
- db.t2.medium
- db.r3.large
- db.r3.xlarge
- db.r3.2xlarge
- db.r3.4xlarge
- db.r3.8xlarge
- db.r4.large
- db.r4.xlarge
- db.r4.2xlarge
- db.r4.4xlarge
- db.r4.8xlarge
- db.r4.16xlarge.

`PubliclyAccessible` - (Optional) Bool to control if instance is publicly accessible.
Default `false`. See the documentation on [Creating DB Instances][6] for more
details on controlling this property.

`DbSubnetGroupName` - (Required if `publicly_accessible = false`, Optional otherwise) A DB subnet group to associate with this DB instance. **NOTE:** This must match the `DbSubnetGroupName` of the attached [`Terraform::AWS::RdsCluster`](/docs/providers/aws/r/rds_cluster.html).

`DbParameterGroupName` - (Optional) The name of the DB parameter group to associate with this instance.

`ApplyImmediately` - (Optional) Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

`MonitoringRoleArn` - (Optional) The ARN for the IAM role that permits RDS to send
enhanced monitoring metrics to CloudWatch Logs. You can find more information on the [AWS Documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)
what IAM permissions are needed to allow Enhanced Monitoring for RDS Instances.

`MonitoringInterval` - (Optional) The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0. Valid Values: 0, 1, 5, 10, 15, 30, 60.

`PromotionTier` - (Optional) Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

`AvailabilityZone` - (Optional, Computed) The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) about the details.

`PreferredBackupWindow` - (Optional) The daily time range during which automated backups are created if automated backups are enabled.
Eg: "04:00-09:00".

`PreferredMaintenanceWindow` - (Optional) The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

`AutoMinorVersionUpgrade` - (Optional) Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

`PerformanceInsightsEnabled` - (Optional) Specifies whether Performance Insights is enabled or not.

`PerformanceInsightsKmsKeyId` - (Optional) The ARN for the KMS key to encrypt Performance Insights data. When specifying `PerformanceInsightsKmsKeyId`, `PerformanceInsightsEnabled` needs to be set to true.

`Tags` - (Optional) A mapping of tags to assign to the instance.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of cluster instance.

`ClusterIdentifier` - The RDS Cluster Identifier.

`Identifier` - The Instance identifier.

`Id` - The Instance identifier.

`AllocatedStorage` - The amount of allocated storage.

`AvailabilityZone` - The availability zone of the instance.

`Endpoint` - The DNS address for this instance. May not be writable.

`Engine` - The database engine.

`EngineVersion` - The database engine version.

`DatabaseName` - The database name.

`Port` - The database port.

`Status` - The RDS instance status.

`StorageEncrypted` - Specifies whether the DB cluster is encrypted.

`KmsKeyId` - The ARN for the KMS encryption key if one is set to the cluster.

`DbiResourceId` - The region-unique, immutable identifier for the DB instance.

`PerformanceInsightsEnabled` - Specifies whether Performance Insights is enabled or not.

`PerformanceInsightsKmsKeyId` - The ARN for the KMS encryption key used by Performance Insights.

## See Also

* [aws_rds_cluster_instance](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the _Terraform Provider Documentation_