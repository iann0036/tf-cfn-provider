# Terraform::VSphere::HaVmOverride

The `vsphere_ha_vm_override` resource can be used to add an override for
vSphere HA settings on a cluster for a specific virtual machine. With this
resource, one can control specific HA settings so that they are different than
the cluster default, accommodating the needs of that specific virtual machine,
while not affecting the rest of the cluster.

For more information on vSphere HA, see [this page][ref-vsphere-ha-clusters].

[ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [vsphere_ha_vm_override](https://www.terraform.io/docs/providers/vsphere/r/ha_vm_override.html) in the _Terraform Provider Documentation_