# Terraform::Alicloud::CsManagedKubernetes

This resource will help you to manager a Managed Kubernetes Cluster. The cluster is same as container service created by web console.

-> **NOTE:** Managed Kubernetes cluster only supports single availability zone currently. Arguments `VswitchIds`, `WorkerNumbers`, `WorkerInstanceTypes` only accept one item.

-> **NOTE:** Managed Kubernetes cluster only supports VPC network and it can access internet while creating kubernetes cluster.
A Nat Gateway and configuring a SNAT for it can ensure one VPC network access internet. If there is no nat gateway in the
VPC, you can set `NewNatGateway` to "true" to create one automatically.

-> **NOTE:** If there is no specified `VswitchIds`, the resource will create a new VPC and VSwitch while creating managed kubernetes cluster.

-> **NOTE:** Creating managed kubernetes cluster need to install several packages and it will cost about 10 minutes. Please be patient.

-> **NOTE:** The provider supports to download kube config, client certificate, client key and cluster ca certificate
after creating cluster successfully, and you can put them into the specified location, like '~/.kube/config'.

-> **NOTE:** If you want to manage managed Kubernetes, you can use [Kubernetes Provider](https://www.terraform.io/docs/providers/kubernetes/index.html).

## Properties

`Name` - The kubernetes cluster's name. It is the only in one Alicloud account.

`NamePrefix` - The kubernetes cluster name's prefix. It is conflict with `Name`. If it is specified, terraform will using it to build the only cluster name. Default to "Terraform-Creation".

`AvailabilityZone` - (Force new resource) The Zone where new kubernetes cluster will be located. If it is not be specified, the value will be vswitch's zone.

`VswitchIds` - (Force new resource) The vswitch where new kubernetes cluster will be located. Specify one vswitch's id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which `AvailabilityZone` specified.

`NewNatGateway` - (Force new resource) Whether to create a new nat gateway while creating kubernetes cluster. Default to true.

`Password` - (Required, Force new resource) The password of ssh login cluster node. You have to specify one of `Password` and `KeyName` fields.

`KeyName` - (Required, Force new resource) The keypair of ssh login cluster node, you have to create it first.

`PodCidr` - (Required, Force new resource) The CIDR block for the pod network. It will be allocated automatically when `VswitchIds` is not specified. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation. Maximum number of hosts allowed in the cluster: 256. Refer to [Plan Kubernetes CIDR blocks under VPC](https://www.alibabacloud.com/help/doc-detail/64530.htm).

`ServiceCidr` - (Required, Force new resource) The CIDR block for the service network.  It will be allocated automatically when `vswitch_id` is not specified. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.

`InstallCloudMonitor` - (Force new resource) Whether to install cloud monitor for the kubernetes' node.

`WorkerDiskSize` - (Force new resource) The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.

`WorkerDiskCategory` - (Force new resource) The system disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.

`WorkerDataDiskSize` - (Force new resource) The data disk size of worker node. Its valid value range [20~32768] in GB. When `WorkerDataDiskCategory` is presented, it defaults to 40.

`WorkerDataDiskCategory` - (Force new resource) The data disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`, if not set, data disk will not be created.

`WorkerNumbers` - The worker node number of the kubernetes cluster. Default to [3]. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.

`WorkerInstanceTypes` - (Required, Force new resource) The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.

`WorkerInstanceChargeType` - (Optional, Force new resource) Worker payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.

`WorkerPeriodUnit` - (Optional) Worker payment period unit. `Month` or `Week`, defaults to `Month`.

`WorkerPeriod` - (Optional) Worker payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.

`WorkerAutoRenew` - (Optional) Enable worker payment auto-renew, defaults to false.

`WorkerAutoRenewPeriod` - (Optional) Worker payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.

`ClusterNetworkType` - (Optional, Force new resource) The network that cluster uses, use `flannel` or `terway`.

`KubeConfig` - (Optional) The path of kube config, like `~/.kube/config`.

`ClientCert` - (Optional) The path of client certificate, like `~/.kube/client-cert.pem`.

`ClientKey` - (Optional) The path of client key, like `~/.kube/client-key.pem`.

`ClusterCaCert` - (Optional) The path of cluster ca certificate, like `~/.kube/cluster-ca-cert.pem`.


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