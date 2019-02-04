# Terraform::VCD::NetworkIsolated

Provides a vCloud Director Org VDC isolated Network. This can be used to create,
modify, and delete internal networks for vApps to connect. This network is not attached to external networks or routers.

Supported in provider *v2.0+*

## Properties

`Org` - (Optional; *v2.0+*) The name of organization to use, optional if defined at provider level. Useful when
connected as sysadmin working across different organisations.

`Vdc` - (Optional; *v2.0+*) The name of VDC to use, optional if defined at provider level.

`Name` - (Required) A unique name for the network.

`Netmask` - (Optional) The netmask for the new network. Defaults to `255.255.255.0`.

`Dns1` - (Optional) First DNS server to use. Defaults to `8.8.8.8`.

`Dns2` - (Optional) Second DNS server to use. Defaults to `8.8.4.4`.

`DnsSuffix` - (Optional) A FQDN for the virtual machines on this network.

`Shared` - (Optional) Defines if this network is shared between multiple vDCs
in the vOrg.  Defaults to `false`.

`DhcpPool` - (Optional) A range of IPs to issue to virtual machines that don't
have a static IP; see [IP Pools](#ip-pools) below for details.

`StaticIpPool` - (Optional) A range of IPs permitted to be used as static IPs for
virtual machines; see [IP Pools](#ip-pools) below for details.


## See Also

* [vcd_network_isolated](https://www.terraform.io/docs/providers/vcd/r/network_isolated.html) in the _Terraform Provider Documentation_