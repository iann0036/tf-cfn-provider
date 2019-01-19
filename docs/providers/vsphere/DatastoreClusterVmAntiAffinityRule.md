# Terraform::VSphere::DatastoreClusterVmAntiAffinityRule

The `vsphere_datastore_cluster_vm_anti_affinity_rule` resource can be used to
manage VM anti-affinity rules in a datastore cluster, either created by the
[`vsphere_datastore_cluster`][tf-vsphere-datastore-cluster-resource] resource or looked up
by the [`vsphere_datastore_cluster`][tf-vsphere-datastore-cluster-data-source] data source.

[tf-vsphere-datastore-cluster-resource]: /docs/providers/vsphere/r/datastore_cluster.html
[tf-vsphere-datastore-cluster-data-source]: /docs/providers/vsphere/d/datastore_cluster.html

This rule can be used to tell a set to virtual machines to run on different
datastores within a cluster, useful for preventing single points of failure in
application cluster scenarios. When configured, Storage DRS will make a best effort to
ensure that the virtual machines run on different datastores, or prevent any
operation that would keep that from happening, depending on the value of the
[`mandatory`](#mandatory) flag.

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [vsphere_datastore_cluster_vm_anti_affinity_rule](https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster_vm_anti_affinity_rule.html) in the _Terraform Provider Documentation_