# Terraform::TelefonicaOpenCloud::MrsClusterV1

Manages resource cluster within TelefonicaOpenCloud MRS.

## Properties

TBC

## Return Values

### Fn::GetAtt

`BillingType` - See Argument Reference above.

`DataCenter` - See Argument Reference above.

`MasterNodeNum` - See Argument Reference above.

`MasterNodeSize` - See Argument Reference above.

`CoreNodeNum` - See Argument Reference above.

`CoreNodeSize` - See Argument Reference above.

`AvailableZoneId` - See Argument Reference above.

`ClusterName` - See Argument Reference above.

`VpcId` - See Argument Reference above.

`SubnetId` - See Argument Reference above.

`ClusterVersion` - See Argument Reference above.

`ClusterType` - See Argument Reference above.

`VolumeType` - See Argument Reference above.

`VolumeSize` - See Argument Reference above.

`NodePublicCertName` - See Argument Reference above.

`SafeMode` - See Argument Reference above.

`ClusterAdminSecret` - See Argument Reference above.

`LogCollection` - See Argument Reference above.

`ComponentList` - See Argument Reference below.

`AddJobs` - See Argument Reference above.

`OrderId` - Order ID for creating clusters.

`ClusterId` - Cluster ID.

`AvailableZoneName` - Name of an availability zone.

`InstanceId` - Instance ID.

`HadoopVersion` - Hadoop version.

`MasterNodeIp` - IP address of a Master node.

`ExternalIp` - Internal IP address.

`PrivateIpFirst` - Primary private IP address.

`ExternalIp` - External IP address.

`SlaveSecurityGroupsId` - Standby security group ID.

`SecurityGroupsId` - Security group ID.

`ExternalAlternateIp` - Backup external IP address.

`MasterNodeSpecId` - Specification ID of a Master node.

`CoreNodeSpecId` - Specification ID of a Core node.

`MasterNodeProductId` - Product ID of a Master node.

`CoreNodeProductId` - Product ID of a Core node.

`Duration` - Cluster subscription duration.

`Vnc` - URI address for remote login of the elastic cloud server.

`Fee` - Cluster creation fee, which is automatically calculated.

`DeploymentId` - Deployment ID of a cluster.

`ClusterState` - Cluster status Valid values include: existing history starting.

`TenantId` - Project ID.

`CreateAt` - Cluster creation time.

`UpdateAt` - Cluster update time.

`ErrorInfo` - Error information.

`ChargingStartTime` - Time when charging starts.

`Remark` - Remarks of a cluster.

`ComponentName` - (Required) Component name Currently, Hadoop, Spark, HBase,.

`ComponentId` - Component ID Component IDs supported by MRS 1.5.0 include:.

`ComponentVersion` - Component version MRS 1.5.0 supports the following component.

`ComponentDesc` - Component description.

## See Also

* [telefonicaopencloud_mrs_cluster_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/mrs_cluster_v1.html) in the _Terraform Provider Documentation_