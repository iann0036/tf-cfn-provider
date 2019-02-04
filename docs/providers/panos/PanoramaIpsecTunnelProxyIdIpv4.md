# Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4

This resource allows you to add/update/delete Panorama IPSec tunnel proxy IDs
to a parent auto key IPSec tunnel for templates.

## Properties

`Template` - (Required) The template name.

`Name` - (Required) The object's name.

`IpsecTunnel` - (Required) The auto key IPSec tunnel to attach this
proxy ID to.

`Local` - (Optional) IP subnet or IP address represents local network.

`Remote` - (Optional) IP subnet or IP address represents remote network.

`ProtocolAny` - (Optional, bool) Set to `true` for any IP protocol.

`ProtocolNumber` - (Optional, int) IP protocol number.

`ProtocolTcpLocal` - (Optional, int) Local TCP port number.

`ProtocolTcpRemote` - (Optional, int) Remote TCP port number.

`ProtocolUdpLocal` - (Optional, int) Local UDP port number.

`ProtocolUdpRemote` - (Optional, int) Remote UDP port number.


## See Also

* [panos_panorama_ipsec_tunnel_proxy_id_ipv4](https://www.terraform.io/docs/providers/panos/r/panorama_ipsec_tunnel_proxy_id_ipv4.html) in the _Terraform Provider Documentation_