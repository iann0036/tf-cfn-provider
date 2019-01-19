# Terraform::VCD::Network

Provides a vCloud Director VDC Network. This can be used to create,
modify, and delete internal networks for vApps to connect.

## Properties

`Name` - (Required) A unique name for the network.

`EdgeGateway` - (Required) The name of the edge gateway.

`Netmask` - (Optional) The netmask for the new network. Defaults to `255.255.255.0`.

`Dns1` - (Optional) First DNS server to use. Defaults to `8.8.8.8`.

`Dns2` - (Optional) Second DNS server to use. Defaults to `8.8.4.4`.

`DnsSuffix` - (Optional) A FQDN for the virtual machines on this network.

`Shared` - (Optional) Defines if this network is shared between multiple vDCs in the vOrg.  Defaults to `false`.

`DhcpPool` - (Optional) A range of IPs to issue to virtual machines that don't have a static IP; see [IP Pools](#ip-pools) below for details.

`StaticIpPool` - (Optional) A range of IPs permitted to be used as static IPs for virtual machines; see [IP Pools](#ip-pools) below for details.


## See Also

* [vcd_network](https://www.terraform.io/docs/providers/vcd/r/network.html) in the _Terraform Provider Documentation_