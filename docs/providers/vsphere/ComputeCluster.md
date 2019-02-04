# Terraform::VSphere::ComputeCluster

-> **A note on the naming of this resource:** VMware refers to clusters of
hosts in the UI and documentation as _clusters_, _HA clusters_, or _DRS
clusters_. All of these refer to the same kind of resource (with the latter two
referring to specific features of clustering). In Terraform, we use
`Terraform::VSphere::ComputeCluster` to differentiate host clusters from _datastore
clusters_, which are clusters of datastores that can be used to distribute load
and ensure fault tolerance via distribution of virtual machines. Datastore
clusters can also be managed through Terraform, via the
[`Terraform::VSphere::DatastoreCluster` resource][docs-r-vsphere-datastore-cluster].

[docs-r-vsphere-datastore-cluster]: /docs/providers/vsphere/r/datastore_cluster.html

The `Terraform::VSphere::ComputeCluster` resource can be used to create and manage
clusters of hosts allowing for resource control of compute resources, load
balancing through DRS, and high availability through vSphere HA.

For more information on vSphere clusters and DRS, see [this
page][ref-vsphere-drs-clusters]. For more information on vSphere HA, see [this
page][ref-vsphere-ha-clusters].

[ref-vsphere-drs-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-8ACF3502-5314-469F-8CC9-4A9BD5925BC2.html
[ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Properties

`Name` - (Required) The name of the cluster.

`DatacenterId` - (Required) The [managed object ID][docs-about-morefs] of
the datacenter to create the cluster in. Forces a new resource if changed.

`Folder` - (Optional) The relative path to a folder to put this cluster in.
This is a path relative to the datacenter you are deploying the cluster to.
Example: for the `dc1` datacenter, and a provided `Folder` of `foo/bar`,
Terraform will place a cluster named `terraform-compute-cluster-test` in a
host folder located at `/dc1/host/foo/bar`, with the final inventory path
being `/dc1/host/foo/bar/terraform-datastore-cluster-test`.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

`CustomAttributes` - (Optional) A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.


## See Also

* [vsphere_compute_cluster](https://www.terraform.io/docs/providers/vsphere/r/compute_cluster.html) in the _Terraform Provider Documentation_