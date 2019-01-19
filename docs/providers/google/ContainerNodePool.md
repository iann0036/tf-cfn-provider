# Terraform::Google::ContainerNodePool

Manages a Node Pool resource within GKE. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/node-pools)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools).

## Properties

`Zone` - (Optional) The zone in which the cluster resides.

`Region` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) The region in which the cluster resides (for regional clusters).

`Cluster` - (Required) The cluster to create the node pool for.  Cluster must be present in `Zone` provided for zonal clusters.

`Autoscaling` - (Optional) Configuration required by cluster autoscaler to adjust the size of the node pool to the current cluster usage. Structure is documented below.

`InitialNodeCount` - (Optional) The initial node count for the pool. Changing this will force recreation of the resource.

`Management` - (Optional) Node management configuration, wherein auto-repair and auto-upgrade is configured. Structure is documented below.

`MaxPodsPerNode` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) The maximum number of pods per node in this node pool. Note that this does not work on node pools which are "route-based" - that is, node pools belonging to clusters that do not have IP Aliasing enabled.

`Name` - (Optional) The name of the node pool. If left blank, Terraform will auto-generate a unique name.

`NodeConfig` - (Optional) The node configuration of the pool. See [google_container_cluster](container_cluster.html) for schema.

`NodeCount` - (Optional) The number of nodes per instance group. This field can be used to update the number of nodes per instance group but should not be used alongside `Autoscaling`.

`Project` - (Optional) The ID of the project in which to create the node pool. If blank, the provider-configured project will be used.

`Version` - (Optional) The Kubernetes version for the nodes in this pool. Note that if this field and `AutoUpgrade` are both specified, they will fight each other for what the node version should be, so setting both is highly discouraged.

### Autoscaling Properties

`MinNodeCount` - (Required) Minimum number of nodes in the NodePool. Must be >=1 and <= `MaxNodeCount`.

`MaxNodeCount` - (Required) Maximum number of nodes in the NodePool. Must be >= min_node_count.

### Management Properties

`AutoRepair` - (Optional) Whether the nodes will be automatically repaired.

`AutoUpgrade` - (Optional) Whether the nodes will be automatically upgraded.


## See Also

* [google_container_node_pool](https://www.terraform.io/docs/providers/google/r/container_node_pool.html) in the _Terraform Provider Documentation_