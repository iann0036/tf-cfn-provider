# Terraform::OCI::ContainerengineCluster

This resource provides the Cluster resource in Oracle Cloud Infrastructure Container Engine service.

Create a new cluster.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailableKubernetesUpgrades` - Available Kubernetes versions to which the clusters masters may be upgraded.

`CompartmentId` - The OCID of the compartment in which the cluster exists.

`Endpoints` - Endpoints served up by the cluster masters.

`Kubernetes` - The Kubernetes API server endpoint.

`Id` - The OCID of the cluster.

`KubernetesVersion` - The version of Kubernetes running on the cluster masters.

`LifecycleDetails` - Details about the state of the cluster masters.

`Metadata` - Metadata about the cluster.

`CreatedByUserId` - The user who created the cluster.

`CreatedByWorkRequestId` - The OCID of the work request which created the cluster.

`DeletedByUserId` - The user who deleted the cluster.

`DeletedByWorkRequestId` - The OCID of the work request which deleted the cluster.

`TimeCreated` - The time the cluster was created.

`TimeDeleted` - The time the cluster was deleted.

`TimeUpdated` - The time the cluster was updated.

`UpdatedByUserId` - The user who updated the cluster.

`UpdatedByWorkRequestId` - The OCID of the work request which updated the cluster.

`Name` - The name of the cluster.

`Options` - Optional attributes for the cluster.

`AddOns` - Configurable cluster add-ons.

`IsKubernetesDashboardEnabled` - Whether or not to enable the Kubernetes Dashboard add-on.

`IsTillerEnabled` - Whether or not to enable the Tiller add-on.

`KubernetesNetworkConfig` - Network configuration for Kubernetes.

`PodsCidr` - The CIDR block for Kubernetes pods.

`ServicesCidr` - The CIDR block for Kubernetes services.

`ServiceLbSubnetIds` - The OCIDs of the subnets used for Kubernetes services load balancers.

`State` - The state of the cluster masters.

`VcnId` - The OCID of the virtual cloud network (VCN) in which the cluster exists.

## See Also

* [oci_containerengine_cluster](https://www.terraform.io/docs/providers/oci/r/containerengine_cluster.html) in the _Terraform Provider Documentation_