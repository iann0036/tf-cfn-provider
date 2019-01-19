# Terraform::VCD::Snat

Provides a vCloud Director SNAT resource. This can be used to create, modify,
and delete source NATs to allow vApps to send external traffic.

## Properties

`EdgeGateway` - (Required) The name of the edge gateway on which to apply the SNAT.

`ExternalIp` - (Required) One of the external IPs available on your Edge Gateway.

`InternalIp` - (Required) The IP or IP Range of the VM(s) to map from.


## See Also

* [vcd_snat](https://www.terraform.io/docs/providers/vcd/r/snat.html) in the _Terraform Provider Documentation_