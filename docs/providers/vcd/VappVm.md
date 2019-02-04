# Terraform::VCD::VappVm

Provides a vCloud Director VM resource. This can be used to create,
modify, and delete VMs within a vApp.

~> **Note:** To make sure resources are created in the right order and both plan apply and destroy succeeds, use the `depends_on` clause (see example below)

## Properties

`VappName` - (Required) The vApp this VM should belong to.

`Name` - (Required) A unique name for the vApp.

`CatalogName` - (Required) The catalog name in which to find the given vApp Template.

`TemplateName` - (Required) The name of the vApp Template to use.

`Memory` - (Optional) The amount of RAM (in MB) to allocate to the vApp.

`Cpus` - (Optional) The number of virtual CPUs to allocate to the vApp.

`NetworkName` - (Optional) Name of the network this VM should connect to.

`Ip` - (Optional) The IP to assign to this vApp. Must be an IP address or
one of dhcp, allocated or none. If given the address must be within the
`static_ip_pool` set for the network. If left blank, and the network has
`dhcp_pool` set with at least one available IP then this will be set with
DHCP.

`PowerOn` - (Optional) A boolean value stating if this vApp should be powered on. Default is `true`.

`AcceptAllEulas` - (Optional; *v2.0+*) Automatically accept EULA if OVA has it. Default is `true`.

`Org` - (Optional; *v2.0+*) The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

`Vdc` - (Optional; *v2.0+*) The name of VDC to use, optional if defined at provider level.


## See Also

* [vcd_vapp_vm](https://www.terraform.io/docs/providers/vcd/r/vapp_vm.html) in the _Terraform Provider Documentation_