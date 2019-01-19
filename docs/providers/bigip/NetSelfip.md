# Terraform::BIGIP::NetSelfip

`Terraform::BIGIP::NetSelfip` Manages a selfip configuration

Resource should be named with their "full path". The full path is the combination of the partition + name of the resource, for example /Common/my-selfip.

## Properties

`Name` - (Required) Name of the selfip.

`Ip` - (Required) The Self IP's address and netmask.

`Vlan` - (Required) Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.

`TrafficGroup` - (Optional) Specifies the traffic group, defaults to `traffic-group-local-only` if not specified.


## See Also

* [bigip_net_selfip](https://www.terraform.io/docs/providers/bigip/r/net_selfip.html) in the _Terraform Provider Documentation_