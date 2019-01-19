# Terraform::VCD::Vapp

Provides a vCloud Director vApp resource. This can be used to create,
modify, and delete vApps.

## Properties

`Name` - (Required) A unique name for the vApp.

`CatalogName` - (Optional) The catalog name in which to find the given vApp Template.

`TemplateName` - (Optional) The name of the vApp Template to use.

`Memory` - (Optional) The amount of RAM (in MB) to allocate to the vApp.

`Cpus` - (Optional) The number of virtual CPUs to allocate to the vApp.

`NetworkName` - (Optional) Name of the network this vApp should join.

`NetworkHref` - (Deprecated) The vCloud Director generated href of the network this vApp should join. If empty it will use the network name and query vCloud Director to discover this.

`Ip` - (Optional) The IP to assign to this vApp. Must be an IP address or one of dhcp, allocated or none. If given the address must be within the `static_ip_pool` set for the network. If left blank, and the network has `dhcp_pool` set with at least one available IP then this will be set with DHCP.

`Metadata` - (Optional) Key value map of metadata to assign to this vApp.

`Ovf` - (Optional) Key value map of ovf parameters to assign to VM product section.

`PowerOn` - (Optional) A boolean value stating if this vApp should be powered on. Default to `true`.


## See Also

* [vcd_vapp](https://www.terraform.io/docs/providers/vcd/r/vapp.html) in the _Terraform Provider Documentation_