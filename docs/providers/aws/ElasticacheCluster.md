# Terraform::AWS::ElasticacheCluster

Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
For working with Redis (Cluster Mode Enabled) replication groups, see the
[`Terraform::AWS::ElasticacheReplicationGroup` resource](/docs/providers/aws/r/elasticache_replication_group.html).

~> **Note:** When you change an attribute, such as `NodeType`, by default
it is applied in the next maintenance window. Because of this, Terraform may report
a difference in its planning phase because the actual modification has not yet taken
place. You can use the `ApplyImmediately` flag to instruct the service to apply the
change immediately. Using `ApplyImmediately` can result in a brief downtime as the server reboots.
See the AWS Docs on [Modifying an ElastiCache Cache Cluster][2] for more information.

## Properties

`ReplicationGroupId` - (Optional) The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.

`ApplyImmediately` - (Optional) Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0).

`SnapshotName` - (Optional) The name of a snapshot from which to restore data into the new node group.  Changing the `SnapshotName` forces a new resource.

`SnapshotWindow` - (Optional, Redis only) The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00.

`SnapshotRetentionLimit` - (Optional, Redis only) The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `SnapshotRetentionLimit` is not supported on cache.t1.micro or cache.t2.* cache nodes.

`AzMode` - (Optional, Memcached only) Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `NumCacheNodes` must be greater than `1`.

`AvailabilityZone` - (Optional) The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `PreferredAvailabilityZones` instead. Default: System chosen Availability Zone.

`AvailabilityZones` - (*DEPRECATED*, Optional, Memcached only) Use `PreferredAvailabilityZones` instead unless you want to create cache nodes in single-az, then use `AvailabilityZone`. Set of Availability Zones in which the cache nodes will be created.

`PreferredAvailabilityZones` - (Optional, Memcached only) A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `NumCacheNodes`. If you want all the nodes in the same Availability Zone, use `AvailabilityZone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`CacheNodes` - List of node objects including `id`, `address`, `Port` and `AvailabilityZone`.

`ConfigurationEndpoint` - (Memcached only) The configuration endpoint to allow host discovery.

`ClusterAddress` - (Memcached only) The DNS name of the cache cluster without the port appended.

## See Also

* [aws_elasticache_cluster](https://www.terraform.io/docs/providers/aws/r/elasticache_cluster.html) in the _Terraform Provider Documentation_