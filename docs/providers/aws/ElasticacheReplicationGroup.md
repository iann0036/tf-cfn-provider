# Terraform::AWS::ElasticacheReplicationGroup

Provides an ElastiCache Replication Group resource.
For working with Memcached or single primary Redis instances (Cluster Mode Disabled), see the
[`aws_elasticache_cluster` resource](/docs/providers/aws/r/elasticache_cluster.html).

~> **Note:** When you change an attribute, such as `engine_version`, by
default the ElastiCache API applies it in the next maintenance window. Because
of this, Terraform may report a difference in its planning phase because the
actual modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change
immediately. Using `apply_immediately` can result in a brief downtime as
servers reboots.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the ElastiCache Replication Group.

`ConfigurationEndpointAddress` - The address of the replication group configuration endpoint when cluster mode is enabled.

`PrimaryEndpointAddress` - (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.

`MemberClusters` - The identifiers of all the nodes that are part of this replication group.

## See Also

* [aws_elasticache_replication_group](https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html) in the _Terraform Provider Documentation_