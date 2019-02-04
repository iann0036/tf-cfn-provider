# Terraform::VSphere::DpmHostOverride

The `Terraform::VSphere::DpmHostOverride` resource can be used to add a DPM override to a
cluster for a particular host. This allows you to control the power management
settings for individual hosts in the cluster while leaving any unspecified ones
at the default power management settings.

For more information on DPM within vSphere clusters, see [this
page][ref-vsphere-cluster-dpm].

[ref-vsphere-cluster-dpm]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-5E5E349A-4644-4C9C-B434-1C0243EBDC80.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Properties

`ComputeClusterId` - (Required) The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

`HostSystemIds` - (Optional) The [managed object ID][docs-about-morefs] of
the host to create the override for.

`DpmEnabled` - (Optional) Enable DPM support for this host. Default:
`false`.

`DpmAutomationLevel` - (Optional) The automation level for host power
operations on this host. Can be one of `manual` or `automated`. Default:
`manual`.


## See Also

* [vsphere_dpm_host_override](https://www.terraform.io/docs/providers/vsphere/r/dpm_host_override.html) in the _Terraform Provider Documentation_