# Terraform::Packet::BgpSession

Provides a resource to manage BGP sessions in Packet Host. Refer to [Packet BGP documentation](https://support.packet.com/kb/articles/bgp) for more details.

You need to have BGP config enabled in your project.

BGP session must be linked to a device running [BIRD](https://bird.network.cz) or other BGP routing daemon which will control route advertisements via the session to Packet's upstream routers.

## Properties

`DeviceId` - (Required) ID of device.

`AddressFamily` - `ipv4` or `ipv6`.


## See Also

* [packet_bgp_session](https://www.terraform.io/docs/providers/packet/r/bgp_session.html) in the _Terraform Provider Documentation_