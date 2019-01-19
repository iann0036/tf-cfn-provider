# Terraform::Alicloud::CsManagedKubernetes

This resource will help you to manager a Managed Kubernetes Cluster. The cluster is same as container service created by web console.

-> **NOTE:** Managed Kubernetes cluster only supports single availability zone currently. Arguments `vswitch_ids`, `worker_numbers`, `worker_instance_types` only accept one item.

-> **NOTE:** Managed Kubernetes cluster only supports VPC network and it can access internet while creating kubernetes cluster.
A Nat Gateway and configuring a SNAT for it can ensure one VPC network access internet. If there is no nat gateway in the
VPC, you can set `new_nat_gateway` to "true" to create one automatically.

-> **NOTE:** If there is no specified `vswitch_ids`, the resource will create a new VPC and VSwitch while creating managed kubernetes cluster.

-> **NOTE:** Creating managed kubernetes cluster need to install several packages and it will cost about 10 minutes. Please be patient.

-> **NOTE:** The provider supports to download kube config, client certificate, client key and cluster ca certificate
after creating cluster successfully, and you can put them into the specified location, like '~/.kube/config'.

-> **NOTE:** If you want to manage managed Kubernetes, you can use [Kubernetes Provider](https://www.terraform.io/docs/providers/kubernetes/index.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the container cluster.

`Name` - The name of the container cluster.

`AvailabilityZone` - The ID of availability zone.

`KeyName` - The keypair of ssh login cluster node, you have to create it first.

`WorkerNumbers` - The ECS instance node number in the current container cluster.

`VswitchIds` - The ID of VSwitches where the current cluster is located.

`VpcId` - The ID of VPC where the current cluster is located.

`SecurityGroupId` - The ID of security group where the current cluster worker node is located.

`ImageId` - The ID of node image.

`NatGatewayId` - The ID of nat gateway used to launch kubernetes cluster.

`WorkerInstanceTypes` - The instance type of worker node.

`WorkerDiskSize` - The system disk size of worker node.

`WorkerDiskCategory` - The system disk category of worker node.

`WorkerDataDiskSize` - The data disk category of worker node.

`WorkerDataDiskCategory` - The data disk size of worker node.

`WorkerNodes` - List of cluster worker nodes. It contains several attributes to `Block Nodes`.

## See Also

* [alicloud_cs_managed_kubernetes](https://www.terraform.io/docs/providers/alicloud/r/cs_managed_kubernetes.html) in the _Terraform Provider Documentation_