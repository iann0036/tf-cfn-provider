# Terraform::Google::ContainerCluster

Creates a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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