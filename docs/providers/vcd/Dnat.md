# Terraform::VCD::Dnat

Provides a vCloud Director DNAT resource. This can be used to create, modify,
and delete destination NATs to map an external IP/port to an internal IP/port.

## Properties

`EdgeGateway` - (Required) The name of the edge gateway on which to apply the DNAT.

`ExternalIp` - (Required) One of the external IPs available on your Edge Gateway.

`Port` - (Required) The port number to map. -1 translates to "any".

`TranslatedPort` - (Optional) The port number to map.

`InternalIp` - (Required) The IP of the VM to map to.

`Protocol` - (Optional; *v2.0+*) The protocol type. Possible values are TCP, UDP, TCPUDP, ICMP, ANY. TCP is default to be backward compatible with previous version.

`IcmpSubType` - (Optional; *v2.0+*) The name of ICMP type. Possible values are   address-mask-request, destination-unreachable, echo-request, echo-reply, parameter-problem, redirect, router-advertisement, router-solicitation, source-quench, time-exceeded, timestamp-request, timestamp-reply, any.

`Org` - (Optional; *v2.0+*) The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

`Vdc` - (Optional; *v2.0+*) The name of VDC to use, optional if defined at provider level.


## See Also

* [vcd_dnat](https://www.terraform.io/docs/providers/vcd/r/dnat.html) in the _Terraform Provider Documentation_