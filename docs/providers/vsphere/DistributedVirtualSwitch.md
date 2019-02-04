# Terraform::VSphere::DistributedVirtualSwitch

The `Terraform::VSphere::DistributedVirtualSwitch` resource can be used to manage VMware
Distributed Virtual Switches.

An essential component of a distributed, scalable VMware datacenter, the
vSphere Distributed Virtual Switch (DVS) provides centralized management and
monitoring of the networking configuration of all the hosts that are associated
with the switch. In addition to adding port groups (see the
[`Terraform::VSphere::DistributedPortGroup`][distributed-port-group] resource) that can
be used as networks for virtual machines, a DVS can be configured to perform
advanced high availability, traffic shaping, network monitoring, and more.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts]. For more information on vSphere DVS, see [this
page][ref-vsphere-dvs].

[distributed-port-group]: /docs/providers/vsphere/r/distributed_port_group.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
[ref-vsphere-dvs]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-375B45C7-684C-4C51-BA3C-70E48DFABF04.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Properties

`Name` - (Required) The name of the distributed virtual switch.

`DatacenterId` - (Required) The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.

`Folder` - (Optional) The folder to create the DVS in. Forces a new resource
if changed.

`Description` - (Optional) A detailed description for the DVS.

`ContactName` - (Optional) The name of the person who is responsible for the
DVS.

`ContactDetail` - (Optional) The detailed contact information for the person
who is responsible for the DVS.

`Ipv4Address` - (Optional) An IPv4 address to identify the switch. This is
mostly useful when used with the [Netflow arguments](#netflow-arguments) found
below.

`LacpApiVersion` - (Optional) The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.

`LinkDiscoveryOperation` - (Optional) Whether to `advertise` or `listen`
for link discovery traffic.

`LinkDiscoveryProtocol` - (Optional) The discovery protocol type. Valid
types are `cdp` and `lldp`.

`MaxMtu` - (Optional) The maximum transmission unit (MTU) for the virtual
switch.

`MulticastFilteringMode` - (Optional) The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.

`Version` - (Optional) - The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

`CustomAttributes` - (Optional) Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.


## See Also

* [vsphere_distributed_virtual_switch](https://www.terraform.io/docs/providers/vsphere/r/distributed_virtual_switch.html) in the _Terraform Provider Documentation_