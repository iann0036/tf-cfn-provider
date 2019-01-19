# Terraform::AWS::ElasticacheReplicationGroup

Provides an ElastiCache Replication Group resource.
For working with Memcached or single primary Redis instances (Cluster Mode Disabled), see the
[`Terraform::AWS::ElasticacheCluster` resource](/docs/providers/aws/r/elasticache_cluster.html).

~> **Note:** When you change an attribute, such as `EngineVersion`, by
default the ElastiCache API applies it in the next maintenance window. Because
of this, Terraform may report a difference in its planning phase because the
actual modification has not yet taken place. You can use the
`ApplyImmediately` flag to instruct the service to apply the change
immediately. Using `ApplyImmediately` can result in a brief downtime as
servers reboots.

## Properties

`NumberCacheClusters` - (Required for Cluster Mode Disabled) The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.

`NodeType` - (Required) The compute and memory capacity of the nodes in the node group.

`AutomaticFailoverEnabled` - (Optional) Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.

`AutoMinorVersionUpgrade` - (Optional) Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. Defaults to `true`.

`AvailabilityZones` - (Optional) A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.

`Engine` - (Optional) The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`.

`AtRestEncryptionEnabled` - (Optional) Whether to enable encryption at rest.

`TransitEncryptionEnabled` - (Optional) Whether to enable encryption in transit.

`AuthToken` - (Optional) The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.

`EngineVersion` - (Optional) The version number of the cache engine to be used for the cache clusters in this replication group.

`ParameterGroupName` - (Optional) The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.

`SubnetGroupName` - (Optional) The name of the cache subnet group to be used for the replication group.

`SecurityGroupNames` - (Optional) A list of cache security group names to associate with this replication group.

`SecurityGroupIds` - (Optional) One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud.

`SnapshotName` - (Optional) The name of a snapshot from which to restore data into the new node group. Changing the `SnapshotName` forces a new resource.

`SnapshotWindow` - (Optional, Redis only) The daily time range (in UTC) during which ElastiCache will begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`.

`SnapshotRetentionLimit` - (Optional, Redis only) The number of days for which ElastiCache will retain automatic cache cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off. Please note that setting a `SnapshotRetentionLimit` is not supported on cache.t1.micro or cache.t2.* cache nodes.

`ApplyImmediately` - (Optional) Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`ClusterMode` - (Optional) Create a native redis cluster. `AutomaticFailoverEnabled` must be set to true. Cluster Mode documented below. Only 1 `ClusterMode` block is allowed.

### ClusterMode Properties

`ReplicasPerNodeGroup` - (Required) Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.

`NumNodeGroups` - (Required) Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.


## Return Values

### Fn::GetAtt

`Id` - The ID of the ElastiCache Replication Group.

`ConfigurationEndpointAddress` - The address of the replication group configuration endpoint when cluster mode is enabled.

`PrimaryEndpointAddress` - (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.

`MemberClusters` - The identifiers of all the nodes that are part of this replication group.

## See Also

* [aws_elasticache_replication_group](https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html) in the _Terraform Provider Documentation_