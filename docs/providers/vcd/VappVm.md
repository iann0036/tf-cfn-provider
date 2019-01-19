# Terraform::VCD::VappVm

Provides a vCloud Director VM resource. This can be used to create,
modify, and delete VMs within a vApp.

~> **Note:** There is known bug with this implementation, that to use the vcd_vapp_vm resource, you must set the paralellism parameter to 1. [We are working on this.](https://github.com/terraform-providers/terraform-provider-vcd/issues/27)

## Properties

`VappName` - (Required) The vApp this VM should belong to.

`Name` - (Required) A unique name for the vApp.

`CatalogName` - (Required) The catalog name in which to find the given vApp Template.

`TemplateName` - (Required) The name of the vApp Template to use.

`Memory` - (Optional) The amount of RAM (in MB) to allocate to the vApp.

`Cpus` - (Optional) The number of virtual CPUs to allocate to the vApp.

`Ip` - (Optional) The IP to assign to this vApp. Must be an IP address or one of dhcp, allocated or none. If given the address must be within the `static_ip_pool` set for the network. If left blank, and the network has `dhcp_pool` set with at least one available IP then this will be set with DHCP.

`PowerOn` - (Optional) A boolean value stating if this vApp should be powered on. Default to `true`.


## See Also

* [vcd_vapp_vm](https://www.terraform.io/docs/providers/vcd/r/vapp_vm.html) in the _Terraform Provider Documentation_