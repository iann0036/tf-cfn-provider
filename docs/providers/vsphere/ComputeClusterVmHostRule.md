# Terraform::VSphere::ComputeClusterVmHostRule

The `Terraform::VSphere::ComputeClusterVmHostRule` resource can be used to manage
VM-to-host rules in a cluster, either created by the
[`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`Terraform::VSphere::ComputeCluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource can create both _affinity rules_, where virtual machines run on
specified hosts, or _anti-affinity_ rules, where virtual machines run on hosts
outside of the ones specified in the rule. Virtual machines and hosts are
supplied via groups, which can be managed via the
[`Terraform::VSphere::ComputeClusterVmGroup`][tf-vsphere-cluster-vm-group-resource] and
[`Terraform::VSphere::ComputeClusterHostGroup`][tf-vsphere-cluster-host-group-resource]
resources.

[tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html
[tf-vsphere-cluster-host-group-resource]: /docs/providers/vsphere/r/compute_cluster_host_group.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Properties

`ComputeClusterId` - (Required) The [managed object reference ID][docs-about-morefs] of the cluster to put the group in.  Forces a new resource if changed.

`Name` - (Required) The name of the rule. This must be unique in the cluster.

`VmGroupName` - (Required) The name of the virtual machine group to use with this rule.

`AffinityHostGroupName` - (Optional) When this field is used, the virtual machines defined in [`VmGroupName`](#vm_group_name) will be run on the hosts defined in this host group.

`AntiAffinityHostGroupName` - (Optional) When this field is used, the virtual machines defined in [`VmGroupName`](#vm_group_name) will _not_ be run on the hosts defined in this host group.

`Enabled` - (Optional) Enable this rule in the cluster. Default: `true`.

`Mandatory` - (Optional) When this value is `true`, prevents any virtual machine operations that may violate this rule. Default: `false`.


## See Also

* [vsphere_compute_cluster_vm_host_rule](https://www.terraform.io/docs/providers/vsphere/r/compute_cluster_vm_host_rule.html) in the _Terraform Provider Documentation_