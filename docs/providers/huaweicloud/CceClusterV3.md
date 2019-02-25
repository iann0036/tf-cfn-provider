# Terraform::HuaweiCloud::CceClusterV3

Provides a cluster resource (CCE).

## Properties

`Name` - (Required) Cluster name. Changing this parameter will create a new cluster resource.

`Labels` - (Optional) Cluster tag, key/value pair format. Changing this parameter will create a new cluster resource.

`Annotations` - (Optional) Cluster annotation, key/value pair format. Changing this parameter will create a new cluster resource.

`FlavorId` - (Required) Cluster specifications. Changing this parameter will create a new cluster resource. Possible values:.

### FlavorId Properties

`Cce.s1.small` - small-scale single cluster (up to 50 nodes).
* `Cce.s1.medium` - medium-scale single cluster (up to 200 nodes).
* `Cce.s1.large` - large-scale single cluster (up to 1000 nodes).
* `Cce.s2.small` - small-scale HA cluster (up to 50 nodes).
* `Cce.s2.medium` - medium-scale HA cluster (up to 200 nodes).
* `Cce.s2.large` - large-scale HA cluster (up to 1000 nodes).
* `Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.s1.medium` - medium-scale single cluster (up to 200 nodes).
* `Cce.s1.large` - large-scale single cluster (up to 1000 nodes).
* `Cce.s2.small` - small-scale HA cluster (up to 50 nodes).
* `Cce.s2.medium` - medium-scale HA cluster (up to 200 nodes).
* `Cce.s2.large` - large-scale HA cluster (up to 1000 nodes).
* `Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.s1.large` - large-scale single cluster (up to 1000 nodes).
* `Cce.s2.small` - small-scale HA cluster (up to 50 nodes).
* `Cce.s2.medium` - medium-scale HA cluster (up to 200 nodes).
* `Cce.s2.large` - large-scale HA cluster (up to 1000 nodes).
* `Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.s2.small` - small-scale HA cluster (up to 50 nodes).
* `Cce.s2.medium` - medium-scale HA cluster (up to 200 nodes).
* `Cce.s2.large` - large-scale HA cluster (up to 1000 nodes).
* `Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.s2.medium` - medium-scale HA cluster (up to 200 nodes).
* `Cce.s2.large` - large-scale HA cluster (up to 1000 nodes).
* `Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.s2.large` - large-scale HA cluster (up to 1000 nodes).
* `Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.t1.small` - small-scale single physical machine cluster (up to 10 nodes).
* `Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.t1.medium` - medium-scale single physical machine cluster (up to 100 nodes).
* `Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.t1.large` - large-scale single physical machine cluster (up to 500 nodes).
* `Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.t2.small` - small-scale HA physical machine cluster (up to 10 nodes).
* `Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.t2.medium` - medium-scale HA physical machine cluster (up to 100 nodes).
* `Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`Cce.t2.large` - large-scale HA physical machine cluster (up to 500 nodes).

`ClusterVersion` - (Optional) For the cluster version, possible values are v1.7.3-r10 or v1.9.2-r1.

`ClusterType` - (Required) Cluster Type, possible values are VirtualMachine and BareMetal. Changing this parameter will create a new cluster resource.

`Description` - (Optional) Cluster description.

`BillingMode` - (Optional) Charging mode of the cluster, which is 0 (on demand). Changing this parameter will create a new cluster resource.

`ExtendParam` - (Optional) Extended parameter. Changing this parameter will create a new cluster resource.

`VpcId` - (Required) The ID of the VPC used to create the node. Changing this parameter will create a new cluster resource.

`SubnetId` - (Required) The ID of the subnet used to create the node. Changing this parameter will create a new cluster resource.

`HighwaySubnetId` - (Optional) The ID of the high speed network used to create bare metal nodes. Changing this parameter will create a new cluster resource.

`ContainerNetworkType` - (Required) Container network parameters. Possible values:.

### ContainerNetworkType Properties

`OverlayL2` - An overlay_l2 network built for containers by using Open vSwitch(OVS)
* `UnderlayIpvlan` - An underlay_ipvlan network built for bare metal servers by using ipvlan.
* `Vpc-router` - An vpc-router network built for containers by using ipvlan and custom VPC routes.

`UnderlayIpvlan` - An underlay_ipvlan network built for bare metal servers by using ipvlan.
* `Vpc-router` - An vpc-router network built for containers by using ipvlan and custom VPC routes.

`Vpc-router` - An vpc-router network built for containers by using ipvlan and custom VPC routes.

`ContainerNetworkCidr` - (Optional) Container network segment. Changing this parameter will create a new cluster resource.


## Return Values

### Fn::GetAtt

`Id` -  Id of the cluster resource.

`Status` -  Cluster status information.

## See Also

* [huaweicloud_cce_cluster_v3](https://www.terraform.io/docs/providers/huaweicloud/r/cce_cluster_v3.html) in the _Terraform Provider Documentation_