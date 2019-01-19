# Terraform::AWS::RedshiftCluster

Provides a Redshift Cluster Resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Redshift Cluster ID.

`ClusterIdentifier` - The Cluster Identifier.

`ClusterType` - The cluster type.

`NodeType` - The type of nodes in the cluster.

`DatabaseName` - The name of the default database in the Cluster.

`AvailabilityZone` - The availability zone of the Cluster.

`AutomatedSnapshotRetentionPeriod` - The backup retention period.

`PreferredMaintenanceWindow` - The backup window.

`Endpoint` - The connection endpoint.

`Encrypted` - Whether the data in the cluster is encrypted.

`ClusterSecurityGroups` - The security groups associated with the cluster.

`VpcSecurityGroupIds` - The VPC security group Ids associated with the cluster.

`DnsName` - The DNS name of the cluster.

`Port` - The Port the cluster responds on.

`ClusterVersion` - The version of Redshift engine software.

`ClusterParameterGroupName` - The name of the parameter group to be associated with this cluster.

`ClusterSubnetGroupName` - The name of a cluster subnet group to be associated with this cluster.

`ClusterPublicKey` - The public key for the cluster.

`ClusterRevisionNumber` - The specific revision number of the database in the cluster.

## See Also

* [aws_redshift_cluster](https://www.terraform.io/docs/providers/aws/r/redshift_cluster.html) in the _Terraform Provider Documentation_