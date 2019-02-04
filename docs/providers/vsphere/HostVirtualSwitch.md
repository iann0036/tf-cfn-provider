# Terraform::VSphere::HostVirtualSwitch

The `Terraform::VSphere::HostVirtualSwitch` resource can be used to manage vSphere
standard switches on an ESXi host. These switches can be used as a backing for
standard port groups, which can be managed by the
[`Terraform::VSphere::HostPortGroup`][host-port-group] resource.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts].

[host-port-group]: /docs/providers/vsphere/r/host_port_group.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html

## Properties

`Name` - (Required) The name of the virtual switch. Forces a new resource if
changed.

`HostSystemId` - (Required) The [managed object ID][docs-about-morefs] of
the host to set the virtual switch up on. Forces a new resource if changed.

`Mtu` - (Optional) The maximum transmission unit (MTU) for the virtual
switch. Default: `1500`.

`NumberOfPorts` - (Optional) The number of ports to create with this
virtual switch. Default: `128`.


## See Also

* [vsphere_host_virtual_switch](https://www.terraform.io/docs/providers/vsphere/r/host_virtual_switch.html) in the _Terraform Provider Documentation_