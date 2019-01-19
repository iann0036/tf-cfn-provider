# Terraform::AWS::RdsClusterInstance

Provides an RDS Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a [RDS Cluster][3],
specifically running Amazon Aurora.

Unlike other RDS resources that support replication, with Amazon Aurora you do
not designate a primary and subsequent replicas. Instead, you simply add RDS
Instances and Aurora manages the replication. You can use the [count][5]
meta-parameter to make multiple instances and join them all to the same RDS
Cluster, or you may specify different Cluster Instance resources with various
`instance_class` sizes.

For more information on Amazon Aurora, see [Aurora on Amazon RDS][2] in the Amazon RDS User Guide.

~> **NOTE:** Deletion Protection from the RDS service can only be enabled at the cluster level, not for individual cluster instances. You can still add the [`prevent_destroy` lifecycle behavior](https://www.terraform.io/docs/configuration/resources.html#prevent_destroy) to your Terraform resource configuration if you desire protection from accidental deletion.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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