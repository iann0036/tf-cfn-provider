# Terraform::TencentCloud::ContainerClusterInstance

Provides a Container Cluster Instance resource.

## Properties

`ClusterId` - (Required) The id of the cluster.

`Cpu` - (Required) The cpu of the node.

`Mem` - (Required) The memory of the node.

`Bandwidth` - (Required) The network bandwidth of the node.

`BandwidthType` - (Required) The network type of the node.

`RequireWanIp` - (Optional) Indicate whether wan ip is needed.

`SubnetId` - (Required) The subnet id which the node stays in.

`IsVpcGateway` - (Required) Describe whether the node enable the gateway capability.

`StorageSize` - (Required) The size of the data volumn.

`StorageType` - (Optional) The type of the data volumn. see more from CVM.

`RootSize` - (Required) The size of the root volumn.

`RootType` - (Optional) The type of the root volumn. see more from CVM.

`VpcId` - (Required) Specify vpc which the node(s) stay in.

`CvmType` - (Optional) The type of node needed by cvm.

`Period` - (Optional) The puchase duration of the node needed by cvm.

`ZoneId` - (Required) The zone which the node stays in.

`InstanceType` - (Optional) The instance type of the node needed by cvm.

`SgId` - (Optional) The safe-group id.

`MountTarget` - (Optional) The path which volumn is going to be mounted.

`DockerGraphPath` - (Optional) The docker graph path is going to mounted.

`Password` - (Optional) The password of each node.

`KeyId` - (Optional) The key_id of each node(if using key pair to access).

`Unschedulable` - (Optional) Determine whether the node will be schedulable. 0 is the default meaning node will be schedulable. 1 for unschedulable.

`UserScript` - (Optional) User defined script in a base64-format. The script runs after the kubernetes component is ready on node. see more from CCS api documents.


## Return Values

### Fn::GetAtt

`AbnormalReason` - Describe the reason when node is in abnormal state(if it was).

`InstanceId` - An id identify the node, provided by cvm.

`IsNormal` - Describe whether the node is normal.

`WanIp` - Describe the wan ip of the node.

`LanIp` - Descirbe the lan ip of the node.

## See Also

* [tencentcloud_container_cluster_instance](https://www.terraform.io/docs/providers/tencentcloud/r/container_cluster_instance.html) in the _Terraform Provider Documentation_