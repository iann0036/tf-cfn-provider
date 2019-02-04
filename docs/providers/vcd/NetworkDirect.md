# Terraform::VCD::NetworkDirect

Provides a vCloud Director Org VDC Network directly connected to an external network. This can be used to create,
modify, and delete internal networks for vApps to connect.

Supported in provider *v2.0+*

## Properties

`Org` - (Optional; *v2.0+*) The name of organization to use, optional if defined at provider level. Useful when
connected as sysadmin working across different organisations.

`Vdc` - (Optional; *v2.0+*) The name of VDC to use, optional if defined at provider level.

`Name` - (Required) A unique name for the network.

`ExternalNetwork` - (Required) The name of the external network.

`Shared` - (Optional) Defines if this network is shared between multiple vDCs
in the vOrg.  Defaults to `false`.


## See Also

* [vcd_network_direct](https://www.terraform.io/docs/providers/vcd/r/network_direct.html) in the _Terraform Provider Documentation_