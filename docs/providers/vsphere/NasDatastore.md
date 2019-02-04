# Terraform::VSphere::NasDatastore

The `Terraform::VSphere::NasDatastore` resource can be used to create and manage NAS
datastores on an ESXi host or a set of hosts. The resource supports mounting
NFS v3 and v4.1 shares to be used as datastores.

~> **NOTE:** Unlike [`Terraform::VSphere::VmfsDatastore`][resource-vmfs-datastore], a NAS
datastore is only mounted on the hosts you choose to mount it on. To mount on
multiple hosts, you must specify each host that you want to add in the
`HostSystemIds` argument.

[resource-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html

## Properties

`Name` - (Required) The name of the datastore. Forces a new resource if
changed.

`HostSystemIds` - (Required) The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.

`Type` - (Optional) The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.

`RemoteHosts` - (Required) The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.

`RemotePath` - (Required) The remote path of the mount point. Forces a new
resource if changed.

`AccessMode` - (Optional) Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.

`SecurityType` - (Optional) The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.

`Folder` - (Optional) The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `Folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`DatastoreClusterId`.

`DatastoreClusterId` - (Optional) The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `Folder`.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

`CustomAttributes` - (Optional) Map of custom attribute ids to attribute
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.


## See Also

* [vsphere_nas_datastore](https://www.terraform.io/docs/providers/vsphere/r/nas_datastore.html) in the _Terraform Provider Documentation_