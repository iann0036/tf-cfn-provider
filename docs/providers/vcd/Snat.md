# Terraform::VCD::Snat

Provides a vCloud Director SNAT resource. This can be used to create, modify,
and delete source NATs to allow vApps to send external traffic.

## Properties

`EdgeGateway` - (Required) The name of the edge gateway on which to apply the SNAT.

`ExternalIp` - (Required) One of the external IPs available on your Edge Gateway.

`InternalIp` - (Required) The IP or IP Range of the VM(s) to map from.

`Org` - (Optional; *v2.0+*) The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

`Vdc` - (Optional; *v2.0+*) The name of VDC to use, optional if defined at provider level.


## See Also

* [vcd_snat](https://www.terraform.io/docs/providers/vcd/r/snat.html) in the _Terraform Provider Documentation_