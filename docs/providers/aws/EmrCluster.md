# Terraform::AWS::EmrCluster

Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the EMR Cluster.

`Name` - The name of the cluster.

`ReleaseLabel` - The release label for the Amazon EMR release.

`MasterInstanceType` - The EC2 instance type of the master node.

`MasterPublicDns` - The public DNS name of the master EC2 instance.

`CoreInstanceType` - The EC2 instance type of the slave nodes.

`LogUri` - The path to the Amazon S3 location where logs for this cluster are stored.

`Applications` - The applications installed on this cluster.

`Ec2Attributes` - Provides information about the EC2 instances in a cluster grouped by category: key name, subnet ID, IAM instance profile, and so on.

`BootstrapAction` - A list of bootstrap actions that will be run before Hadoop is started on the cluster nodes.

`Configurations` - The list of Configurations supplied to the EMR cluster.

`ServiceRole` - The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.

`VisibleToAllUsers` - Indicates whether the job flow is visible to all IAM users of the AWS account associated with the job flow.

`Tags` - The list of tags associated with a cluster.

## See Also

* [aws_emr_cluster](https://www.terraform.io/docs/providers/aws/r/emr_cluster.html) in the _Terraform Provider Documentation_