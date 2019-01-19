# Terraform::AWS::ElasticacheCluster

Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
For working with Redis (Cluster Mode Enabled) replication groups, see the
[`aws_elasticache_replication_group` resource](/docs/providers/aws/r/elasticache_replication_group.html).

~> **Note:** When you change an attribute, such as `node_type`, by default
it is applied in the next maintenance window. Because of this, Terraform may report
a difference in its planning phase because the actual modification has not yet taken
place. You can use the `apply_immediately` flag to instruct the service to apply the
change immediately. Using `apply_immediately` can result in a brief downtime as the server reboots.
See the AWS Docs on [Modifying an ElastiCache Cache Cluster][2] for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CacheNodes` - List of node objects including `id`, `address`, `port` and `availability_zone`.

`ConfigurationEndpoint` - (Memcached only) The configuration endpoint to allow host discovery.

`ClusterAddress` - (Memcached only) The DNS name of the cache cluster without the port appended.

## See Also

* [aws_elasticache_cluster](https://www.terraform.io/docs/providers/aws/r/elasticache_cluster.html) in the _Terraform Provider Documentation_