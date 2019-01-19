# Terraform::VSphere::HostPortGroup

The `Terraform::VSphere::HostPortGroup` resource can be used to manage vSphere standard
port groups on an ESXi host. These port groups are connected to standard
virtual switches, which can be managed by the
[`Terraform::VSphere::HostVirtualSwitch`][host-virtual-switch] resource.

For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].

[host-virtual-switch]: /docs/providers/vsphere/r/host_virtual_switch.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html

## Properties

`Name` - (Required) The name of the port group.  Forces a new resource if changed.

`HostSystemId` - (Required) The [managed object ID][docs-about-morefs] of the host to set the port group up on. Forces a new resource if changed.

`VirtualSwitchName` - (Required) The name of the virtual switch to bind this port group to. Forces a new resource if changed.

`VlanId` - (Optional) The VLAN ID/trunk mode for this port group.  An ID of `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an ID of `4095` enables trunk mode, allowing the guest to manage its own tagging. Default: `0`.


## See Also

* [vsphere_host_port_group](https://www.terraform.io/docs/providers/vsphere/r/host_port_group.html) in the _Terraform Provider Documentation_