# Terraform::AWS::RedshiftCluster

Provides a Redshift Cluster Resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ClusterIdentifier` - (Required) The Cluster Identifier. Must be a lower case string.

`DatabaseName` - (Optional) The name of the first database to be created when the cluster is created. If you do not provide a name, Amazon Redshift will create a default database called `dev`.

`NodeType` - (Required) The node type to be provisioned for the cluster.

`ClusterType` - (Optional) The cluster type to use. Either `single-node` or `multi-node`.

`MasterPassword` - (Required unless a `SnapshotIdentifier` is provided) Password for the master DB user. Note that this may show up in logs, and it will be stored in the state file. Password must contain at least 8 chars and contain at least one uppercase letter, one lowercase letter, and one number.

`MasterUsername` - (Required unless a `SnapshotIdentifier` is provided) Username for the master DB user.

`ClusterSecurityGroups` - (Optional) A list of security groups to be associated with this cluster.

`VpcSecurityGroupIds` - (Optional) A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

`ClusterSubnetGroupName` - (Optional) The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

`AvailabilityZone` - (Optional) The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

`PreferredMaintenanceWindow` - (Optional) The weekly time range (in UTC) during which automated cluster maintenance can occur. Format: ddd:hh24:mi-ddd:hh24:mi.

`ClusterParameterGroupName` - (Optional) The name of the parameter group to be associated with this cluster.

`AutomatedSnapshotRetentionPeriod` - (Optional) The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with create-cluster-snapshot. Default is 1.

`Port` - (Optional) The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default port is 5439.

`ClusterVersion` - (Optional) The version of the Amazon Redshift engine software that you want to deploy on the cluster. The version selected runs on all the nodes in the cluster.

`AllowVersionUpgrade` - (Optional) If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default is true.

`NumberOfNodes` - (Optional) The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node. Default is 1.

`PubliclyAccessible` - (Optional) If true, the cluster can be accessed from a public network. Default is `true`.

`Encrypted` - (Optional) If true , the data in the cluster is encrypted at rest.

`EnhancedVpcRouting` - (Optional) If true , enhanced VPC routing is enabled.

`KmsKeyId` - (Optional) The ARN for the KMS encryption key. When specifying `KmsKeyId`, `Encrypted` needs to be set to true.

`ElasticIp` - (Optional) The Elastic IP (EIP) address for the cluster.

`SkipFinalSnapshot` - (Optional) Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted. Default is false.

`FinalSnapshotIdentifier` - (Optional) The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, `SkipFinalSnapshot` must be false.

`SnapshotIdentifier` - (Optional) The name of the snapshot from which to create the new cluster.

`SnapshotClusterIdentifier` - (Optional) The name of the cluster the source snapshot was created from.

`OwnerAccount` - (Optional) The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

`IamRoles` - (Optional) A list of IAM Role ARNs to associate with the cluster. A Maximum of 10 can be associated to the cluster at any time.

`Logging` - (Optional) Logging, documented below.

`SnapshotCopy` - (Optional) Configuration of automatic copy of snapshots from one region to another. Documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

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