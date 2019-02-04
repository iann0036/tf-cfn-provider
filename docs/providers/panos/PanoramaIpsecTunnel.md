# Terraform::Panos::PanoramaIpsecTunnel

This resource allows you to add/update/delete Panorama IPSec tunnels
for templates.

A large number of params have prefixes:

* `ak` - Auto key
* `mk` - Manual key
* `gps` - GlobalProtect Satellite

## Properties

`Name` - (Required) The object's name.

`Template` - (Required) The template name.

`TunnelInterface` - (Required) The tunnel interface.

`AntiReplay` - (Optional, bool) Set to `true` to enable Anti-Replay check
on this tunnel.

`EnableIpv6` - (Optional, PAN-OS 7.0+, bool) Set to `true` to enable IPv6.

`CopyTos` - (Optional, bool) Set to `true` to copy IP TOS bits from inner
packet to IPSec packet (not recommended).

`CopyFlowLabel` - (Optional, PAN-OS 7.0+, bool) Set to `true` to copy IPv6
flow label for 6in6 tunnel from inner packet to IPSec packet (not recommended).

`Disabled` - (Optional, PAN-OS 7.0+, bool) Set to `true` to disable this
IPSec tunnel.

`Type` - (Optional) The type.  Valid values are `auto-key` (the default),
`manual-key`, or `global-protect-satellite`.

`AkIkeGateway` - (Optional) IKE gateway name.

`AkIpsecCryptoProfile` - (Optional) IPSec crypto profile name.

`MkLocalSpi` - (Optional) Outbound SPI, hex format.

`MkRemoteSpi` - (Optional) Inbound SPI, hex format.

`MkLocalAddressIp` - (Optional) Specify exact IP address if interface
has multiple addresses.

`MkLocalAddressFloatingIp` - (Optional) Floating IP address in HA
Active-Active configuration.

`MkProtocol` - (Optional) Manual key protocol.  Valid valies are
`esp` or `ah`.

`MkAuthType` - (Optional) Authentication algorithm.  Valid values are
`md5`, `sha1`, `sha256`, `sha384`, `sha512`, or `none`.

`MkAuthKey` - (Optional) The auth key for the given auth type.

`MkEspEncryptionType` - (Optional) The encryption algorithm.  Valid values
are `des`, `3des`, `aes-128-cbc`, `aes-192-cbc`, `aes-256-cbc`, or `null`.

`MkEspEncryptionKey` - (Optional) The encryption key.

`GpsInterface` - (Optional) Interface to communicate with portal.

`GpsPortalAddress` - (Optional) GlobalProtect portal address.

`GpsPreferIpv6` - (Optional, PAN-OS 8.0+, bool) Prefer to register the
portal in IPv6. Only applicable to FQDN portal-address.

`GpsInterfaceIpIpv4` - (Optional) specify exact IP address if interface
has multiple addresses (IPv4).

`GpsInterfaceIpIpv6` - (Optional, PAN-OS 8.0+) specify exact IP address if interface
has multiple addresses (IPv6).

`GpsInterfaceFloatingIpIpv4` - (Optional, PAN-OS 7.0+) Floating IPv4
address in HA Active-Active configuration.

`GpsInterfaceFloatingIpIpv6` - (Optional, PAN-OS 8.0+) Floating IPv6
address in HA Active-Active configuration.

`GpsPublishConnectedRoutes` - (Optional, bool) Set to `true` to to publish
connected and static routes.

`GpsPublishRoutes` - (Optional, list) Specify list of routes to publish
to Global Protect Gateway.

`GpsLocalCertificate` - (Optional) GlobalProtect satellite certificate
file name.

`GpsCertificateProfile` - (Optional) Profile for authenticating
GlobalProtect gateway certificates.

`EnableTunnelMonitor` - (Optional, bool) Enable tunnel monitoring on this tunnel.

`TunnelMonitorDestinationIp` - (Optional) Destination IP to send ICMP probe.

`TunnelMonitorSourceIp` - (Optional) Source IP to send ICMP probe.

`TunnelMonitorProfile` - (Optional) Tunnel monitor profile.

`TunnelMonitorProxyId` - (Optional, PAN-OS 7.0+) Which proxy-id (or
proxy-id-v6) the monitoring traffic will use.


## See Also

* [panos_panorama_ipsec_tunnel](https://www.terraform.io/docs/providers/panos/r/panorama_ipsec_tunnel.html) in the _Terraform Provider Documentation_