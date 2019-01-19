# Terraform::AWS::EmrCluster

Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
for more information.

## Properties

`Name` - (Required) The name of the job flow.

`ReleaseLabel` - (Required) The release label for the Amazon EMR release.

`MasterInstanceType` - (Optional) The EC2 instance type of the master node. Exactly one of `MasterInstanceType` and `InstanceGroup` must be specified.

`ScaleDownBehavior` - (Optional) The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.

`AdditionalInfo` - (Optional) A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.

`ServiceRole` - (Required) IAM role that will be assumed by the Amazon EMR service to access AWS resources.

`SecurityConfiguration` - (Optional) The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `ReleaseLabel` 4.8.0 or greater.

`CoreInstanceType` - (Optional) The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set.

`CoreInstanceCount` - (Optional) Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`CoreInstanceCount`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`.

`InstanceGroup` - (Optional) A list of `InstanceGroup` objects for each instance group in the cluster. Exactly one of `MasterInstanceType` and `InstanceGroup` must be specified. If `InstanceGroup` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below.

`LogUri` - (Optional) S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created.

`Applications` - (Optional) A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive.

`TerminationProtection` - (Optional) Switch on/off termination protection (default is off).

`KeepJobFlowAliveWhenNoSteps` - (Optional) Switch on/off run cluster with no steps or when all steps are complete (default is on).

`Ec2Attributes` - (Optional) Attributes for the EC2 instances running the job flow. Defined below.

`KerberosAttributes` - (Optional) Kerberos configuration for the cluster. Defined below.

`EbsRootVolumeSize` - (Optional) Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

`CustomAmiId` - (Optional) A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.

`BootstrapAction` - (Optional) List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.

`Configurations` - (Optional) List of configurations supplied for the EMR cluster you are creating.

`ConfigurationsJson` - (Optional) A JSON string for supplying list of configurations for the EMR cluster.

`VisibleToAllUsers` - (Optional) Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`.

`AutoscalingRole` - (Optional) An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

`Step` - (Optional) List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.

`Tags` - (Optional) list of tags to apply to the EMR Cluster.


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