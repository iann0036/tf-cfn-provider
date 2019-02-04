# Terraform::VSphere::ComputeClusterHostGroup

The `Terraform::VSphere::ComputeClusterHostGroup` resource can be used to manage groups
of hosts in a cluster, either created by the
[`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource mainly serves as an input to the
[`Terraform::VSphere::ComputeClusterVmHostRule`][tf-vsphere-cluster-vm-host-rule-resource]
resource - see the documentation for that resource for further details on how
to use host groups.

[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Properties

`Name` - (Required) The name of the host group. This must be unique in the
cluster. Forces a new resource if changed.

`ComputeClusterId` - (Required) The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

`HostSystemIds` - (Optional) The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.


## See Also

* [vsphere_compute_cluster_host_group](https://www.terraform.io/docs/providers/vsphere/r/compute_cluster_host_group.html) in the _Terraform Provider Documentation_