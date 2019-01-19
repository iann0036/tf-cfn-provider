# Terraform::VSphere::ComputeClusterVmAffinityRule

The `Terraform::VSphere::ComputeClusterVmAffinityRule` resource can be used to manage
VM affinity rules in a cluster, either created by the
[`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This rule can be used to tell a set to virtual machines to run together on a
single host within a cluster. When configured, DRS will make a best effort to
ensure that the virtual machines run on the same host, or prevent any operation
that would keep that from happening, depending on the value of the
[`Mandatory`](#mandatory) flag.

-> Keep in mind that this rule can only be used to tell VMs to run together on
a _non-specific_ host - it can't be used to pin VMs to a host. For that, see
the
[`Terraform::VSphere::ComputeClusterVmHostRule`][tf-vsphere-cluster-vm-host-rule-resource]
resource.

[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Properties

`ComputeClusterId` - (Required) The [managed object reference ID][docs-about-morefs] of the cluster to put the group in.  Forces a new resource if changed.

`Name` - (Required) The name of the rule. This must be unique in the cluster.

`VirtualMachineIds` - (Required) The UUIDs of the virtual machines to run on the same host together.

`Enabled` - (Optional) Enable this rule in the cluster. Default: `true`.

`Mandatory` - (Optional) When this value is `true`, prevents any virtual machine operations that may violate this rule. Default: `false`.


## See Also

* [vsphere_compute_cluster_vm_affinity_rule](https://www.terraform.io/docs/providers/vsphere/r/compute_cluster_vm_affinity_rule.html) in the _Terraform Provider Documentation_