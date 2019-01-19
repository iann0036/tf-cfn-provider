# Terraform::TencentCloud::ContainerCluster

Provides a Container Cluster resource.

## Properties

`ClusterName` - (Required) The name of the cluster.

`Cpu` - (Required) The cpu of the node.

`Mem` - (Required) The memory of the node.

`OsName` - (Required) The system os name of the node.

`Bandwidth` - (Required) The network bandwidth of the node.

`BandwidthType` - (Required) The network type of the node.

`SubnetId` - (Required) The subnet id which the node stays in.

`IsVpcGateway` - (Required) Describe whether the node enable the gateway capability.

`StorageSize` - (Required) The size of the data volumn.

`StorageType` - (Optional) The type of the data volumn. see more from CVM.

`RootSize` - (Required) The size of the root volumn.

`RootType` - (Optional) The type of the root volumn. see more from CVM.

`GoodsNum` - (Required) The node number is going to create in the cluster.

`VpcId` - (Required) Specify vpc which the node(s) stay in.

`ClusterCidr` - (Required) The CIDR which the cluster is going to use.

`ClusterDesc` - (Optional) The descirption of the cluster.

`CvmType` - (Optional) The type of node needed by cvm.

`Period` - (Optional) The puchase duration of the node needed by cvm.

`ZoneId` - (Required) The zone which the node stays in.

`InstanceType` - (Optional) The instance type of the node needed by cvm.

`SgId` - (Optional) The safe-group id.

`MountTarget` - (Optional) The path which volumn is going to be mounted.

`DockerGraphPath` - (Optional) The docker graph path is going to mounted.

`InstanceName` - (Optional) The name ot node.

`ClusterVersion` - (Optional) The kubernetes version of the cluster.

`Password` - (Optional) The password of each node.

`KeyId` - (Optional) The key_id of each node(if using key pair to access).

`RequireWanIp` - (Optional) Indicate whether wan ip is needed.

`UserScript` - (Optional) User defined script in a base64-format. The script runs after the kubernetes component is ready on node. see more from CCS api documents.


## Return Values

### Fn::GetAtt

`KubernetesVersion` - The kubernetes version of the cluster.

`NodesNum` - The node number of the cluster.

`NodesStatus` - The node status of the cluster.

`TotalCpu` - The total cpu of the cluster.

`TotalMem` - The total memory of the cluster.

## See Also

* [tencentcloud_container_cluster](https://www.terraform.io/docs/providers/tencentcloud/r/container_cluster.html) in the _Terraform Provider Documentation_