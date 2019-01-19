# Terraform::Alicloud::CsKubernetes

This resource will help you to manager a Kubernetes Cluster. The cluster is same as container service created by web console.

-> **NOTE:** Kubernetes cluster only supports VPC network and it can access internet while creating kubernetes cluster.
A Nat Gateway and configuring a SNAT for it can ensure one VPC network access internet. If there is no nat gateway in the
VPC, you can set `NewNatGateway` to "true" to create one automatically.

-> **NOTE:** If there is no specified `VswitchIds`, the resource will create a new VPC and VSwitch while creating kubernetes cluster.

-> **NOTE:** Each kubernetes cluster contains 3 master nodes and those number cannot be changed at now.

-> **NOTE:** Creating kubernetes cluster need to install several packages and it will cost about 15 minutes. Please be patient.

-> **NOTE:** From version 1.9.4, the provider supports to download kube config, client certificate, client key and cluster ca certificate
after creating cluster successfully, and you can put them into the specified location, like '~/.kube/config'.

-> **NOTE:** From version 1.16.0, the provider supports Multiple Availability Zones Kubernetes Cluster. To create a cluster of this kind,
you must specify three items in `VswitchIds`, `MasterInstanceTypes` and `WorkerInstanceTypes`.

-> **NOTE:** From version 1.20.0, the provider supports disabling internet load balancer for API Server by setting `false` to `SlbInternetEnabled`.

-> **NOTE:** If you want to manage Kubernetes, you can use [Kubernetes Provider](https://www.terraform.io/docs/providers/kubernetes/index.html).

## Properties

`Name` - The kubernetes cluster's name. It is the only in one Alicloud account.

`NamePrefix` - The kubernetes cluster name's prefix. It is conflict with `Name`. If it is specified, terraform will using it to build the only cluster name. Default to "Terraform-Creation".

`AvailabilityZone` - (Force new resource) The Zone where new kubernetes cluster will be located. If it is not be specified, the value will be vswitch's zone.

`VswitchId` - (Deprecated from version 1.16.0)(Force new resource) The vswitch where new kubernetes cluster will be located. If it is not specified, a new VPC and VSwicth will be built. It must be in the zone which `AvailabilityZone` specified.

`VswitchIds` - (Force new resource) The vswitch where new kubernetes cluster will be located. For SingleAZ Cluster, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which `AvailabilityZone` specified. For MultiAZ Cluster, you must create three vswitches firstly, specify them here.

`NewNatGateway` - (Force new resource) Whether to create a new nat gateway while creating kubernetes cluster. Default to true.

`MasterInstanceType` - (Deprecated from version 1.16.0)(Required, Force new resource) The instance type of master node.

`MasterInstanceTypes` - (Required, Force new resource) The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.

`WorkerInstanceType` - (Deprecated from version 1.16.0)(Required, Force new resource) The instance type of worker node.

`WorkerInstanceTypes` - (Required, Force new resource) The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.

`WorkerNumber` - The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.

`Password` - (Required, Force new resource) The password of ssh login cluster node. You have to specify one of `Password` and `KeyName` fields.

`KeyName` - (Required, Force new resource) The keypair of ssh login cluster node, you have to create it first.

`ClusterNetworkType` - (Required, Force new resource) The network that cluster uses, use `flannel` or `terway`.

`PodCidr` - (Required, Force new resource) The CIDR block for the pod network. It will be allocated automatically when `VswitchIds` is not specified. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation. Maximum number of hosts allowed in the cluster: 256. Refer to [Plan Kubernetes CIDR blocks under VPC](https://www.alibabacloud.com/help/doc-detail/64530.htm).

`ServiceCidr` - (Required, Force new resource) The CIDR block for the service network.  It will be allocated automatically when `VswitchId` is not specified. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.

`MasterInstanceChargeType` - (Optional, Force new resource) Master payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.

`MasterPeriodUnit` - (Optional) Master payment period unit. `Month` or `Week`, defaults to `Month`.

`MasterPeriod` - (Optional) Master payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.

`MasterAutoRenew` - (Optional) Enable master payment auto-renew, defaults to false.

`MasterAutoRenewPeriod` - (Optional) Master payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.

`WorkerInstanceChargeType` - (Optional, Force new resource) Worker payment type. `PrePaid` or `PostPaid`, defaults to `PostPaid`.

`WorkerPeriodUnit` - (Optional) Worker payment period unit. `Month` or `Week`, defaults to `Month`.

`WorkerPeriod` - (Optional) Worker payment period. When period unit is `Month`, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”, “4”}.

`WorkerAutoRenew` - (Optional) Enable worker payment auto-renew, defaults to false.

`WorkerAutoRenewPeriod` - (Optional) Worker payment auto-renew period. When period unit is `Month`, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is `Week`, it can be one of {“1”, “2”, “3”}.

`NodeCidrMask` - (Optional, Force new resource) The network mask used on pods for each node, ranging from `24` to `28`. Larger this number is, less pods can be allocated on each node. Default value is `24`, means you can allocate 256 pods on each node.

`LogConfig` - (Optional, Force new resource) A list of one element containing information about the associated log store. It contains the following attributes: * `Type` - Type of collecting logs, only `SLS` are supported currently. * `Project` - Log Service project name, cluster logs will output to this project.

`Type` - Type of collecting logs, only `SLS` are supported currently. * `Project` - Log Service project name, cluster logs will output to this project.

`Project` - Log Service project name, cluster logs will output to this project.

`EnableSsh` - (Force new resource) Whether to allow to SSH login kubernetes. Default to false.

`SlbInternetEnabled` - (Force new resource) Whether to create internet load balancer for API Server. Default to true.

`MasterDiskCategory` - (Force new resource) The system disk category of master node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.

`MasterDiskSize` - (Force new resource) The system disk size of master node. Its valid value range [20~32768] in GB. Default to 20.

`WorkerDiskCategory` - (Force new resource) The system disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`. Default to `cloud_efficiency`.

`WorkerDiskSize` - (Force new resource) The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 20.

`WorkerDataDiskSize` - (Force new resource) The data disk size of worker node. Its valid value range [20~32768] in GB. When `WorkerDataDiskCategory` is presented, it defaults to 40.

`WorkerDataDiskCategory` - (Force new resource) The data disk category of worker node. Its valid value are `cloud_ssd` and `cloud_efficiency`, if not set, data disk will not be created.

`InstallCloudMonitor` - (Force new resource) Whether to install cloud monitor for the kubernetes' node.

`IsOutdated` - (Optional) Whether to use outdated instance type. Default to false.

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