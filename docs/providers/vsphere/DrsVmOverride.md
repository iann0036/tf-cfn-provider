# Terraform::VSphere::DrsVmOverride

The `vsphere_drs_vm_override` resource can be used to add a DRS override to a
cluster for a specific virtual machine. With this resource, one can enable or
disable DRS and control the automation level for a single virtual machine
without affecting the rest of the cluster.

For more information on vSphere clusters and DRS, see [this
page][ref-vsphere-drs-clusters].

[ref-vsphere-drs-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-8ACF3502-5314-469F-8CC9-4A9BD5925BC2.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [vsphere_drs_vm_override](https://www.terraform.io/docs/providers/vsphere/r/drs_vm_override.html) in the _Terraform Provider Documentation_