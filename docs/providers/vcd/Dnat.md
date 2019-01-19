# Terraform::VCD::Dnat

Provides a vCloud Director DNAT resource. This can be used to create, modify,
and delete destination NATs to map an external IP/port to an internal IP/port.

## Properties

`EdgeGateway` - (Required) The name of the edge gateway on which to apply the DNAT.

`ExternalIp` - (Required) One of the external IPs available on your Edge Gateway.

`Port` - (Required) The port number to map.

`InternalIp` - (Required) The IP of the VM to map to.


## See Also

* [vcd_dnat](https://www.terraform.io/docs/providers/vcd/r/dnat.html) in the _Terraform Provider Documentation_