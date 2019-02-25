# Terraform::OCI::ContainerengineCluster

This resource provides the Cluster resource in Oracle Cloud Infrastructure Container Engine service.

Create a new cluster.

## Properties

`CompartmentId` - (Required) The OCID of the compartment in which to create the cluster.

`KubernetesVersion` - (Required) (Updatable) The version of Kubernetes to install into the cluster masters.

`Name` - (Required) (Updatable) The name of the cluster. Avoid entering confidential information.

`Options` - (Optional) Optional attributes for the cluster.
* `AddOns` - (Optional) Configurable cluster add-ons
* `IsKubernetesDashboardEnabled` - (Optional) Whether or not to enable the Kubernetes Dashboard add-on.
* `IsTillerEnabled` - (Optional) Whether or not to enable the Tiller add-on.
* `KubernetesNetworkConfig` - (Optional) Network configuration for Kubernetes.
* `PodsCidr` - (Optional) The CIDR block for Kubernetes pods.
* `ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`AddOns` - (Optional) Configurable cluster add-ons
* `IsKubernetesDashboardEnabled` - (Optional) Whether or not to enable the Kubernetes Dashboard add-on.
* `IsTillerEnabled` - (Optional) Whether or not to enable the Tiller add-on.
* `KubernetesNetworkConfig` - (Optional) Network configuration for Kubernetes.
* `PodsCidr` - (Optional) The CIDR block for Kubernetes pods.
* `ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`IsKubernetesDashboardEnabled` - (Optional) Whether or not to enable the Kubernetes Dashboard add-on.
* `IsTillerEnabled` - (Optional) Whether or not to enable the Tiller add-on.
* `KubernetesNetworkConfig` - (Optional) Network configuration for Kubernetes.
* `PodsCidr` - (Optional) The CIDR block for Kubernetes pods.
* `ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`IsTillerEnabled` - (Optional) Whether or not to enable the Tiller add-on.
* `KubernetesNetworkConfig` - (Optional) Network configuration for Kubernetes.
* `PodsCidr` - (Optional) The CIDR block for Kubernetes pods.
* `ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`KubernetesNetworkConfig` - (Optional) Network configuration for Kubernetes.
* `PodsCidr` - (Optional) The CIDR block for Kubernetes pods.
* `ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`PodsCidr` - (Optional) The CIDR block for Kubernetes pods.
* `ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`ServicesCidr` - (Optional) The CIDR block for Kubernetes services.
* `ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`ServiceLbSubnetIds` - (Optional) The OCIDs of the subnets used for Kubernetes services load balancers.

`VcnId` - (Required) The OCID of the virtual cloud network (VCN) in which to create the cluster.


## Return Values

### Fn::GetAtt

`UpdatedByUserId` - The user who updated the cluster.

`TimeCreated` - The time the cluster was created.

`ServiceLbSubnetIds` - The OCIDs of the subnets used for Kubernetes services load balancers.

`TimeDeleted` - The time the cluster was deleted.

`ServicesCidr` - The CIDR block for Kubernetes services.

`Id` - The OCID of the cluster.

`CreatedByUserId` - The user who created the cluster.

`IsTillerEnabled` - Whether or not to enable the Tiller add-on.

`CompartmentId` - The OCID of the compartment in which the cluster exists.

`State` - The state of the cluster masters.

`UpdatedByWorkRequestId` - The OCID of the work request which updated the cluster.

`Metadata` - Metadata about the cluster.

`DeletedByWorkRequestId` - The OCID of the work request which deleted the cluster.

`PodsCidr` - The CIDR block for Kubernetes pods.

`Kubernetes` - The Kubernetes API server endpoint.

`DeletedByUserId` - The user who deleted the cluster.

`IsKubernetesDashboardEnabled` - Whether or not to enable the Kubernetes Dashboard add-on.

`CreatedByWorkRequestId` - The OCID of the work request which created the cluster.

`AddOns` - Configurable cluster add-ons.

`KubernetesNetworkConfig` - Network configuration for Kubernetes.

`AvailableKubernetesUpgrades` - Available Kubernetes versions to which the clusters masters may be upgraded.

`TimeUpdated` - The time the cluster was updated.

`Name` - The name of the cluster.

`VcnId` - The OCID of the virtual cloud network (VCN) in which the cluster exists.

`KubernetesVersion` - The version of Kubernetes running on the cluster masters.

`LifecycleDetails` - Details about the state of the cluster masters.

`Endpoints` - Endpoints served up by the cluster masters.

`Options` - Optional attributes for the cluster.

## See Also

* [oci_containerengine_cluster](https://www.terraform.io/docs/providers/oci/r/containerengine_cluster.html) in the _Terraform Provider Documentation_