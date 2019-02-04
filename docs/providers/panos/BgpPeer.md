# Terraform::Panos::BgpPeer

This resource allows you to add/update/delete a BGP peer.

## Properties

`VirtualRouter` - (Required) The virtual router to add this BGP
peer to.

`BgpPeerGroup` - (Required) The BGP peer group to put this peer into.

`Name` - (Required) The name.

`Enable` - (Optional, bool) Enable or not (default: `true`).

`PeerAs` - (Optional) Peer AS number.

`LocalAddressInterface` - (Required) Interface to accept BGP session.

`LocalAddressIp` - (Optional) Specify exact IP address if interface has
multiple addresses.

`PeerAddressIp` - (Required) Peer IP address configuration.

`ReflectorClient` - (Optional) This peer is reflector client.  Valid
values are `non-client`, `client`, or `meshed-client`.

`PeeringType` - (Optional) Peering type that affects NOPEER
community value handling.  Valid values are `unspecified` (default) or
`bilateral`.

`MaxPrefixes` - (Optional) Maximum of prefixes to receive from the
peer.  This can be a number such as `"5000"` (default) or `unlimited`.

`AuthProfile` - (Optional) Auth profile.

`KeepAliveInterval` - (Optional, int) Keep alive interval, in
seconds (default: `30`).

`MultiHop` - (Optional, int) IP TTL value used for sending BGP packet.

`OpenDelayTime` - (Optional, int) Open delay time, in seconds.

`HoldTime` - (Optional, int) Hold time, in seconds.

`IdleHoldTime` - (Optional, int) Idle hold time, in seconds.

`AllowIncomingConnections` - (Optional, bool) Allow incoming connections
(default: `true`).

`IncomingConnectionsRemotePort` - (Optional, int) Restrict remote port for
incoming BGP connections.

`AllowOutgoingConnections` - (Optional, bool) Allow outgoing connections
(default: `true`).

`OutgoingConnectionsLocalPort` - (Optional, int) Use specific local
port for outgoing BGP connections.

`BfdProfile` - (Optional, PAN-OS 7.1+) BFD profile.  This can be a specific
BFD profile name, `None` (disables BFD), or `Inherit-vr-global-setting`.

`EnableMpBgp` - (Optional, bool, PAN-OS 8.0+) Enable MP BGP.

`AddressFamilyType` - (Optional, PAN-OS 8.0+) Set the AFI for this
peer.  Valid values are `ipv4` or `ipv6`.

`SubsequentAddressFamilyUnicast` - (Optional, bool, PAN-OS 8.0+) Enable
unicast subsequent address family for this peer.

`SubsequentAddressFamilyMulticast` - (Optional, bool, PAN-OS 8.0+) Enable
multicast subsequent address family for this peer.

`EnableSenderSideLoopDetection` - (Optional, bool, PAN-OS 8.0+) Enable
sender side loop detection.

`MinRouteAdvertisementInterval` - (Optional, int, PAN-OS 8.1+) Minimum
route advertisement interval, in seconds.


## See Also

* [panos_bgp_peer](https://www.terraform.io/docs/providers/panos/r/bgp_peer.html) in the _Terraform Provider Documentation_