# Terraform::Google::ContainerCluster

Creates a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) The name of the cluster, unique within the project and zone.

`Zone` - (Optional) The zone that the master and the number of nodes specified in `InitialNodeCount` should be created in. Only one of `Zone` and `Region` may be set. If neither zone nor region are set, the provider zone is used.

`AdditionalZones` - (Optional) The list of additional Google Compute Engine locations in which the cluster's nodes should be located. If additional zones are configured, the number of nodes specified in `InitialNodeCount` is created in all specified zones.

`AddonsConfig` - (Optional) The configuration for addons supported by GKE. Structure is documented below.

`ClusterIpv4Cidr` - (Optional) The IP address range of the kubernetes pods in this cluster. Default is an automatically assigned CIDR.

`ClusterAutoscaling` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Configuration for cluster autoscaling (also called autoprovisioning), as described in [the docs](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning). Structure is documented below.

`Description` - (Optional) Description of the cluster.

`EnableBinaryAuthorization` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Enable Binary Authorization for this cluster. If enabled, all container images will be validated by Google Binary Authorization.

`EnableKubernetesAlpha` - (Optional) Whether to enable Kubernetes Alpha features for this cluster. Note that when this option is enabled, the cluster cannot be upgraded and will be automatically deleted after 30 days.

`EnableTpu` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Whether to enable Cloud TPU resources in this cluster. See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).

`EnableLegacyAbac` - (Optional) Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM. Defaults to `false`.

`InitialNodeCount` - (Optional) The number of nodes to create in this cluster (not including the Kubernetes master). Must be set if `NodePool` is not set.

`IpAllocationPolicy` - (Optional) Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported. This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases) Structure is documented below.

`LoggingService` - (Optional) The logging service that the cluster should write logs to. Available options include `logging.googleapis.com`, `logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`.

`MaintenancePolicy` - (Optional) The maintenance policy to use for the cluster. Structure is documented below.

`MasterAuth` - (Optional) The authentication information for accessing the Kubernetes master. Structure is documented below.

`MasterAuthorizedNetworksConfig` - (Optional) The desired configuration options for master authorized networks. Omit the nested `CidrBlocks` attribute to disallow external access (except the cluster node IPs, which GKE automatically whitelists).

`MinMasterVersion` - (Optional) The minimum version of the master. GKE will auto-update the master to new versions, so this does not guarantee the current master version--use the read-only `master_version` field to obtain that. If unset, the cluster's version will be set by GKE to the version of the most recent official release (which is not necessarily the latest version).  Most users will find the `Terraform::Google::ContainerEngineVersions` data source useful - it indicates which versions are available.  If you intend to specify versions manually, [the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version) describe the various acceptable formats for this field.

`MonitoringService` - (Optional) The monitoring service that the cluster should write metrics to. Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API. VM metrics will be collected by Google Compute Engine regardless of this setting Available options include `monitoring.googleapis.com`, `monitoring.googleapis.com/kubernetes` (beta) and `none`. Defaults to `monitoring.googleapis.com`.

`Network` - (Optional) The name or self_link of the Google Compute Engine network to which the cluster is connected. For Shared VPC, set this to the self link of the shared network.

`NetworkPolicy` - (Optional) Configuration options for the [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/) feature. Structure is documented below.

`NodeConfig` -  (Optional) Parameters used in creating the cluster's nodes. Structure is documented below.

`NodePool` - (Optional) List of node pools associated with this cluster. See [google_container_node_pool](container_node_pool.html) for schema. **Warning:** node pools defined inside a cluster can't be changed (or added/removed) after cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability to say "these are the _only_ node pools associated with this cluster", use the [google_container_node_pool](container_node_pool.html) resource instead of this property.

`NodeVersion` - (Optional) The Kubernetes version on the nodes. Must either be unset or set to the same value as `MinMasterVersion` on create. Defaults to the default version set by GKE which is not necessarily the latest version. This only affects nodes in the default node pool. To update nodes in other node pools, use the `version` attribute on the node pool.

`PodSecurityPolicyConfig` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Configuration for the [PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature. Structure is documented below.

`PrivateClusterConfig` - (Optional) A set of options for creating a private cluster. Structure is documented below.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`RemoveDefaultNodePool` - (Optional) If true, deletes the default node pool upon cluster creation.

`ResourceLabels` - (Optional) The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

`Subnetwork` - (Optional) The name or self_link of the Google Compute Engine subnetwork in which the cluster's instances are launched.

### MasterAuth Properties

`Password` - (Optional) The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

`Username` - (Optional) The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. If not present basic auth will be disabled.

`ClientCertificateConfig` - (Optional) Whether client certificate authorization is enabled for this cluster.  For example:.

### IpAllocationPolicy Properties

`ClusterSecondaryRangeName` - (Optional) The name of the secondary range to be used as for the cluster CIDR block. The secondary range will be used for pod IP addresses. This must be an existing secondary range associated with the cluster subnetwork.

`ServicesSecondaryRangeName` - (Optional) The name of the secondary range to be used as for the services CIDR block.  The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork.

`ClusterIpv4CidrBlock` - (Optional) The IP address range for the cluster pod IPs. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.

`ServicesIpv4CidrBlock` - (Optional) The IP address range of the services IPs in this cluster. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.

`CreateSubnetwork` - (Optional) Whether a new subnetwork will be created automatically for the cluster.

`SubnetworkName` - (Optional) A custom subnetwork name to be used if create_subnetwork is true. If this field is empty, then an automatic name will be chosen for the new subnetwork.

### NetworkPolicy Properties

`Enabled` - (Optional) Whether network policy is enabled on the cluster. Defaults to false.

`Provider` - (Optional) The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.

### MaintenancePolicy Properties

`DailyMaintenanceWindow` - (Required) Time window specified for daily maintenance operations. Specify `start_time` in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "HH:MM”, where HH : \[00-23\] and MM : \[00-59\] GMT. For example:.

### NodeConfig Properties

`DiskSizeGb` - (Optional) Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.

`DiskType` - (Optional) Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'.

`GuestAccelerator` - (Optional) List of the type and count of accelerator cards attached to the instance. Structure documented below.

`ImageType` - (Optional) The image type to use for this node. Note that changing the image type will delete and recreate all nodes in the node pool.

`Labels` - (Optional) The Kubernetes labels (key/value pairs) to be applied to each node.

`LocalSsdCount` - (Optional) The amount of local SSD disks that will be attached to each cluster node. Defaults to 0.

`MachineType` - (Optional) The name of a Google Compute Engine machine type. Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified [here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).

`Metadata` - (Optional) The metadata key/value pairs assigned to instances in the cluster.

`MinCpuPlatform` - (Optional) Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as `Intel Haswell`. See the [official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform) for more information.

`OauthScopes` - (Optional) The set of Google API scopes to be made available on all of the node VMs under the "default" service account. These can be either FQDNs, or scope aliases. The following scopes are necessary to ensure the correct functioning of the cluster:.

`Preemptible` - (Optional) A boolean that represents whether or not the underlying node VMs are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm) for more information. Defaults to false.

`ServiceAccount` - (Optional) The service account to be used by the Node VMs. If not specified, the "default" service account is used. In order to use the configured `OauthScopes` for logging and monitoring, the service account being used needs the [roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and [roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.

`Tags` - (Optional) The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls.

`Taint` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) List of [kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) to apply to each node. Structure is documented below.

`WorkloadMetadataConfig` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Metadata configuration to expose to workloads on the node pool. Structure is documented below.

### AddonsConfig Properties

`HorizontalPodAutoscaling` - (Optional) The status of the Horizontal Pod Autoscaling addon, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods. It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service. It is enabled by default; set `disabled = true` to disable.

`HttpLoadBalancing` - (Optional) The status of the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster. It is enabled by default; set `disabled = true` to disable.

`KubernetesDashboard` - (Optional) The status of the Kubernetes Dashboard add-on, which controls whether the Kubernetes Dashboard is enabled for this cluster. It is enabled by default; set `disabled = true` to disable.

`NetworkPolicyConfig` - (Optional) Whether we should enable the network policy addon for the master.  This must be enabled in order to enable network policy for the nodes. It can only be disabled if the nodes already do not have network policies enabled. Set `disabled = true` to disable.

`IstioConfig` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)). Structure is documented below.

`CloudrunConfig` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)). The status of the CloudRun addon. It requires `IstioConfig` enabled. It is disabled by default. Set `disabled = false` to enable. This addon can only be enabled at cluster creation time.

`Disabled` - (Optional) The status of the Istio addon, which makes it easy to set up Istio for services in a cluster. It is disabled by default. Set `disabled = false` to enable.

`Auth` - (Optional) The authentication type between services in Istio. Available options include `AUTH_MUTUAL_TLS`.

`ResourceLimits` - (Optional) A list of limits on the autoprovisioning. See [the docs](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) for an explanation of what options are available.  If enabling autoprovisioning, make sure to set at least `cpu` and `memory`.  Structure is documented below.

`ResourceType` - (Required) See [the docs](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) for a list of permitted types - `cpu`, `memory`, and others.

`Minimum` - (Optional) The minimum value for the resource type specified.

`Maximum` - (Optional) The maximum value for the resource type specified.

### PrivateClusterConfig Properties

`PrivateEndpoint` - The internal IP address of this cluster's master endpoint.

`PublicEndpoint` - The external IP address of this cluster's master endpoint.

### MasterAuthorizedNetworksConfig Properties

`CidrBlocks` - (Optional) Defines up to 20 external networks that can access Kubernetes master through HTTPS.

`CidrBlock` - (Optional) External network that can access Kubernetes master through HTTPS. Must be specified in CIDR notation.

`DisplayName` - (Optional) Field for users to identify CIDR blocks.


## Return Values

### Fn::GetAtt

`Endpoint` - The IP address of this cluster's Kubernetes master.

`InstanceGroupUrls` - List of instance group URLs which have been assigned.

`MaintenancePolicy.0.dailyMaintenanceWindow.0.duration` - Duration of the time window, automatically chosen to be.

`MasterAuth.0.clientCertificate` - Base64 encoded public certificate.

`MasterAuth.0.clientKey` - Base64 encoded private key used by clients.

`MasterAuth.0.clusterCaCertificate` - Base64 encoded public certificate.

`MasterVersion` - The current version of the master in the cluster. This may.

`TpuIpv4CidrBlock` - ([Beta](https://terraform.io/docs/providers/google/provider_versions.html)) The IP address range of the Cloud TPUs in this cluster, in.

## See Also

* [google_container_cluster](https://www.terraform.io/docs/providers/google/r/container_cluster.html) in the _Terraform Provider Documentation_