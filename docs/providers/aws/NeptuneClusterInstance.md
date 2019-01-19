# Terraform::AWS::NeptuneClusterInstance

A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.

You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various `InstanceClass` sizes.

## Properties

`ApplyImmediately` - (Optional) Specifies whether any instance modifications are applied immediately, or during the next maintenance window. Default is`false`.

`AutoMinorVersionUpgrade` - (Optional) Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.

`AvailabilityZone` - (Optional) The EC2 Availability Zone that the neptune instance is created in.

`ClusterIdentifier` - (Required) The identifier of the [`Terraform::AWS::NeptuneCluster`](/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.

`Engine` - (Optional) The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.

`EngineVersion` - (Optional) The neptune engine version.

`Identifier` - (Optional, Forces new resource) The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.

`IdentifierPrefix` - (Optional, Forces new resource) Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

`InstanceClass` - (Required) The instance class to use.

`NeptuneSubnetGroupName` - (Required if `publicly_accessible = false`, Optional otherwise) A subnet group to associate with this neptune instance. **NOTE:** This must match the `NeptuneSubnetGroupName` of the attached [`Terraform::AWS::NeptuneCluster`](/docs/providers/aws/r/neptune_cluster.html).

`NeptuneParameterGroupName` - (Optional) The name of the neptune parameter group to associate with this instance.

`Port` - (Optional) The port on which the DB accepts connections. Defaults to `8182`.

`PreferredBackupWindow` - (Optional) The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00".

`PreferredMaintenanceWindow` - (Optional) The window to perform maintenance in. Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

`PromotionTier` - (Optional) Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

`PubliclyAccessible` - (Optional) Bool to control if instance is publicly accessible. Default is `false`.

`Tags` - (Optional) A mapping of tags to assign to the instance.


## Return Values

### Fn::GetAtt

`Address` - The hostname of the instance. See also `endpoint` and `Port`.

`Arn` - Amazon Resource Name (ARN) of neptune instance.

`DbiResourceId` - The region-unique, immutable identifier for the neptune instance.

`Endpoint` - The connection endpoint in `address:port` format.

`Id` - The Instance identifier.

`KmsKeyArn` - The ARN for the KMS encryption key if one is set to the neptune cluster.

`StorageEncrypted` - Specifies whether the neptune cluster is encrypted.

## See Also

* [aws_neptune_cluster_instance](https://www.terraform.io/docs/providers/aws/r/neptune_cluster_instance.html) in the _Terraform Provider Documentation_