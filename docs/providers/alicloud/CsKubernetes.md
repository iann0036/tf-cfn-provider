# Terraform::Alicloud::CsKubernetes

This resource will help you to manager a Kubernetes Cluster. The cluster is same as container service created by web console.

-> **NOTE:** Kubernetes cluster only supports VPC network and it can access internet while creating kubernetes cluster.
A Nat Gateway and configuring a SNAT for it can ensure one VPC network access internet. If there is no nat gateway in the
VPC, you can set `new_nat_gateway` to "true" to create one automatically.

-> **NOTE:** If there is no specified `vswitch_ids`, the resource will create a new VPC and VSwitch while creating kubernetes cluster.

-> **NOTE:** Each kubernetes cluster contains 3 master nodes and those number cannot be changed at now.

-> **NOTE:** Creating kubernetes cluster need to install several packages and it will cost about 15 minutes. Please be patient.

-> **NOTE:** From version 1.9.4, the provider supports to download kube config, client certificate, client key and cluster ca certificate
after creating cluster successfully, and you can put them into the specified location, like '~/.kube/config'.

-> **NOTE:** From version 1.16.0, the provider supports Multiple Availability Zones Kubernetes Cluster. To create a cluster of this kind,
you must specify three items in `vswitch_ids`, `master_instance_types` and `worker_instance_types`.

-> **NOTE:** From version 1.20.0, the provider supports disabling internet load balancer for API Server by setting `false` to `slb_internet_enabled`.

-> **NOTE:** If you want to manage Kubernetes, you can use [Kubernetes Provider](https://www.terraform.io/docs/providers/kubernetes/index.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the container cluster.

`Name` - The name of the container cluster.

`AvailabilityZone` - The ID of availability zone.

`KeyName` - The keypair of ssh login cluster node, you have to create it first.

`WorkerNumber` - (Deprecated from version 1.16.0) The ECS instance node number in the current container cluster.

`WorkerNumbers` - The ECS instance node number in the current container cluster.

`VswitchId` - (Deprecated from version 1.16.0) The ID of VSwitch where the current cluster is located.

`VswitchIds` - The ID of VSwitches where the current cluster is located.

`VpcId` - The ID of VPC where the current cluster is located.

`SlbId` - (Deprecated from version 1.9.2).

`SlbInternetEnabled` - Whether internet load balancer for API Server is created.

`SlbInternet` - The ID of public load balancer where the current cluster master node is located.

`SlbIntranet` - The ID of private load balancer where the current cluster master node is located.

`SecurityGroupId` - The ID of security group where the current cluster worker node is located.

`ImageId` - The ID of node image.

`NatGatewayId` - The ID of nat gateway used to launch kubernetes cluster.

`MasterInstanceType` - (Deprecated from version 1.16.0) The instance type of master node.

`MasterInstanceTypes` - The instance type of master node.

`WorkerInstanceType` - (Deprecated from version 1.16.0)The instance type of worker node.

`WorkerInstanceTypes` - The instance type of worker node.

`MasterDiskCategory` - The system disk category of master node.

`MasterDiskSize` - The system disk size of master node.

`WorkerDiskCategory` - The system disk category of worker node.

`WorkerDiskSize` - The system disk size of worker node.

`WorkerDataDiskCategory` - The data disk size of worker node.

`WorkerDataDiskSize` - The data disk category of worker node.

`Nodes` - (Deprecated from version 1.9.4) It has been deprecated from provider version 1.9.4. New field `master_nodes` and `worker_nodes` replace it.

`MasterNodes` - List of cluster master nodes. It contains several attributes to `Block Nodes`.

`WorkerNodes` - List of cluster worker nodes. It contains several attributes to `Block Nodes`.

`Connections` - Map of kubernetes cluster connection information. It contains several attributes to `Block Connections`.

`NodeCidrMask` - The network mask used on pods for each node.

`LogConfig` - A list of one element containing information about the associated log store. It contains the following attributes:.

`Type` - Type of collecting logs.

`Project` - Log Service project name.

## See Also

* [alicloud_cs_kubernetes](https://www.terraform.io/docs/providers/alicloud/r/cs_kubernetes.html) in the _Terraform Provider Documentation_