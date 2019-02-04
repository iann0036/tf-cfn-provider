# Terraform::OPC::ComputeSecurityApplication

The ``Terraform::OPC::ComputeSecurityApplication`` resource creates and manages a security application in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Name` - (Required) The unique (within the identity domain) name of the application.

`Protocol` - (Required) The protocol to enable for this application. Must be one of
`tcp`, `udp`, `ah`, `esp`, `icmp`, `icmpv6`, `igmp`, `ipip`, `gre`, `mplsip`, `ospf`, `pim`, `rdp`, `sctp` or `all`.

`Dport` - (Required) The port, or range of ports, to enable for this application, e.g `8080`, `6000-7000`. This must be set if the `Protocol` is set to `tcp` or `udp`.

`Icmptype` - (Optional) The ICMP type to enable for this application, if the `Protocol` is `icmp`. Must be one of
`echo`, `reply`, `ttl`, `traceroute`, `unreachable`.

`Icmpcode` - (Optional) The ICMP code to enable for this application, if the `Protocol` is `icmp`. Must be one of
`admin`, `df`, `host`, `network`, `port` or `Protocol`.


## See Also

* [opc_compute_security_application](https://www.terraform.io/docs/providers/opc/r/compute_security_application.html) in the _Terraform Provider Documentation_