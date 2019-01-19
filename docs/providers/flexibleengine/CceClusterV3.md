# Terraform::FlexibleEngine::CceClusterV3

Provides a cluster resource (CCE).

## Properties

`Name` - (Required) Cluster name. Changing this parameter will create a new cluster resource.

`Labels` - (Optional) Cluster tag, key/value pair format. Changing this parameter will create a new cluster resource.

`Annotations` - (Optional) Cluster annotation, key/value pair format. Changing this parameter will create a new cluster resource.

`FlavorId` - (Required) Cluster specifications. Changing this parameter will create a new cluster resource.

`ClusterVersion` - (Optional) For the cluster version, possible value is v1.9.7-r1.

`ClusterType` - (Required) Cluster Type, Changing this parameter will create a new cluster resource.

`Description` - (Optional) Cluster description.

`BillingMode` - (Optional) Charging mode of the cluster, which is 0 (on demand). Changing this parameter will create a new cluster resource.

`ExtendParam` - (Optional) Extended parameter. Changing this parameter will create a new cluster resource.

`VpcId` - (Required) The ID of the VPC used to create the node. Changing this parameter will create a new cluster resource.

`SubnetId` - (Required) The ID of the subnet used to create the node. Changing this parameter will create a new cluster resource.

`HighwaySubnetId` - (Optional) The ID of the high speed network used to create bare metal nodes. Changing this parameter will create a new cluster resource.

`ContainerNetworkCidr` - (Optional) Container network segment. Changing this parameter will create a new cluster resource.


## Return Values

### Fn::GetAtt

`Id` -  Id of the cluster resource.

`Status` -  Cluster status information.

`Internal` - The internal network address.

`External` - The external network address.

`ExternalOtc` - The endpoint of the cluster to be accessed through API Gateway.

## See Also

* [flexibleengine_cce_cluster_v3](https://www.terraform.io/docs/providers/flexibleengine/r/cce_cluster_v3.html) in the _Terraform Provider Documentation_