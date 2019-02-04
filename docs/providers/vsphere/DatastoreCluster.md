# Terraform::VSphere::DatastoreCluster

The `Terraform::VSphere::DatastoreCluster` resource can be used to create and manage
datastore clusters. This can be used to create groups of datastores with a
shared management interface, allowing for resource control and load balancing
through Storage DRS.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.

## Properties

`Name` - (Required) The name of the datastore cluster.

`DatacenterId` - (Required) The [managed object ID][docs-about-morefs] of
the datacenter to create the datastore cluster in. Forces a new resource if
changed.

`Folder` - (Optional) The relative path to a folder to put this datastore
cluster in.  This is a path relative to the datacenter you are deploying the
datastore to.  Example: for the `dc1` datacenter, and a provided `Folder` of
`foo/bar`, Terraform will place a datastore cluster named
`terraform-datastore-cluster-test` in a datastore folder located at
`/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-datastore-cluster-test`.

`SdrsEnabled` - (Optional) Enable Storage DRS for this datastore cluster.
Default: `false`.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

`CustomAttributes` - (Optional) A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.


## See Also

* [vsphere_datastore_cluster](https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster.html) in the _Terraform Provider Documentation_