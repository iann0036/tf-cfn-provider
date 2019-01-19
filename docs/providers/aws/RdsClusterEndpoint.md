# Terraform::AWS::RdsClusterEndpoint

Manages a RDS Aurora Cluster Endpoint.
You can refer to the [User Guide][1].

## Properties

`ClusterIdentifier` - (Required, Forces new resources) The cluster identifier.

`ClusterEndpointIdentifier` - (Required, Forces new resources) The identifier to use for the new endpoint. This parameter is stored as a lowercase string.

`CustomEndpointType` - (Required) The type of the endpoint. One of: READER , ANY .

`StaticMembers` - (Optional) List of DB instance identifiers that are part of the custom endpoint group. Conflicts with `ExcludedMembers`.

`ExcludedMembers` - (Optional) List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty. Conflicts with `StaticMembers`.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of cluster.

`Id` - The RDS Cluster Endpoint Identifier.

`Endpoint` - A custom endpoint for the Aurora cluster.

## See Also

* [aws_rds_cluster_endpoint](https://www.terraform.io/docs/providers/aws/r/rds_cluster_endpoint.html) in the _Terraform Provider Documentation_