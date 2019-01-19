# Terraform::VSphere::StorageDrsVmOverride

The `Terraform::VSphere::StorageDrsVmOverride` resource can be used to add a Storage DRS
override to a datastore cluster for a specific virtual machine. With this
resource, one can enable or disable Storage DRS, and control the automation
level and disk affinity for a single virtual machine without affecting the rest
of the datastore cluster.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

## Properties

`DatastoreClusterId` - (Required) The [managed object reference ID][docs-about-morefs] of the datastore cluster to put the override in. Forces a new resource if changed.

`VirtualMachineId` - (Required) The UUID of the virtual machine to create the override for.  Forces a new resource if changed.

`SdrsEnabled` - (Optional) Overrides the default Storage DRS setting for this virtual machine. When not specified, the datastore cluster setting is used.

`SdrsAutomationLevel` - (Optional) Overrides any Storage DRS automation levels for this virtual machine. Can be one of `automated` or `manual`. When not specified, the datastore cluster's settings are used according to the [specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].

`SdrsIntraVmAffinity` - (Optional) Overrides the intra-VM affinity setting for this virtual machine. When `true`, all disks for this virtual machine will be kept on the same datastore. When `false`, Storage DRS may locate individual disks on different datastores if it helps satisfy cluster requirements. When not specified, the datastore cluster's settings are used.


## See Also

* [vsphere_storage_drs_vm_override](https://www.terraform.io/docs/providers/vsphere/r/storage_drs_vm_override.html) in the _Terraform Provider Documentation_