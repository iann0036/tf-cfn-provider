# Terraform::AWS::NeptuneCluster

Provides an Neptune Cluster Resource. A Cluster Resource defines attributes that are
applied to the entire cluster of Neptune Cluster Instances.

Changes to a Neptune Cluster can occur when you manually change a
parameter, such as `backup_retention_period`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - The Neptune Cluster Amazon Resource Name (ARN).

`ClusterResourceId` - The Neptune Cluster Resource ID.

`Endpoint` - The DNS address of the Neptune instance.

`HostedZoneId` - The Route53 Hosted Zone ID of the endpoint.

`Id` - The Neptune Cluster Identifier.

`ReaderEndpoint` - A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas.

`Status` - The Neptune instance status.

## See Also

* [aws_neptune_cluster](https://www.terraform.io/docs/providers/aws/r/neptune_cluster.html) in the _Terraform Provider Documentation_