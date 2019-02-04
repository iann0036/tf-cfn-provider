# Terraform::VSphere::ComputeClusterVmDependencyRule

The `Terraform::VSphere::ComputeClusterVmDependencyRule` resource can be used to manage
VM dependency rules in a cluster, either created by the
[`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

A virtual machine dependency rule applies to vSphere HA, and allows
user-defined startup orders for virtual machines in the case of host failure.
Virtual machines are supplied via groups, which can be managed via the
[`Terraform::VSphere::ComputeClusterVmGroup`][tf-vsphere-cluster-vm-group-resource]
resource.

[tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Properties

`ComputeClusterId` - (Required) The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

`Name` - (Required) The name of the rule. This must be unique in the
cluster.

`DependencyVmGroupName` - (Required) The name of the VM group that this
rule depends on. The VMs defined in the group specified by
[`VmGroupName`](#vm_group_name) will not be started until the VMs in this
group are started.

`VmGroupName` - (Required) The name of the VM group that is the subject of
this rule. The VMs defined in this group will not be started until the VMs in
the group specified by
[`DependencyVmGroupName`](#dependency_vm_group_name) are started.

`Enabled` - (Optional) Enable this rule in the cluster. Default: `true`.

`Mandatory` - (Optional) When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.


## See Also

* [vsphere_compute_cluster_vm_dependency_rule](https://www.terraform.io/docs/providers/vsphere/r/compute_cluster_vm_dependency_rule.html) in the _Terraform Provider Documentation_