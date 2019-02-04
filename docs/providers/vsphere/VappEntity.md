# Terraform::VSphere::VappEntity

The `Terraform::VSphere::VappEntity` resource can be used to describe the behavior of an
entity (virtual machine or sub-vApp container) in a vApp container.

For more information on vSphere vApps, see [this
page][ref-vsphere-vapp].

[ref-vsphere-vapp]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-2A95EBB8-1779-40FA-B4FB-4D0845750879.html

## Properties

`TargetId` - (Required) [Managed object ID|docs-about-morefs] of the entity
to power on or power off. This can be a virtual machine or a vApp.

`ContainerId` - (Required) [Managed object ID|docs-about-morefs] of the vApp
container the entity is a member of.

`StartOrder` - (Optional) Order to start and stop target in vApp. Default: 1.

`StartAction` - (Optional) How to start the entity. Valid settings are none
or powerOn. If set to none, then the entity does not participate in auto-start.
Default: powerOn.

`StartDelay` - (Optional) Delay in seconds before continuing with the next
entity in the order of entities to be started. Default: 120.

`StopAction` - (Optional) Defines the stop action for the entity. Can be set
to none, powerOff, guestShutdown, or suspend. If set to none, then the entity
does not participate in auto-stop. Default: powerOff.

`StopDelay` - (Optional) Delay in seconds before continuing with the next
entity in the order sequence. This is only used if the stopAction is
guestShutdown. Default: 120.

`WaitForGuest` - (Optional) Determines if the VM should be marked as being
started when VMware Tools are ready instead of waiting for `StartDelay`. This
property has no effect for vApps. Default: false.


## See Also

* [vsphere_vapp_entity](https://www.terraform.io/docs/providers/vsphere/r/vapp_entity.html) in the _Terraform Provider Documentation_