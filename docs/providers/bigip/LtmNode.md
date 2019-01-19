# Terraform::BIGIP::LtmNode

`Terraform::BIGIP::LtmNode` Manages a node configuration

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the node.

`Address` - (Required) IP or hostname of the node.

`ConnectionLimit` - (Optional) Specifies the maximum number of connections allowed for the node or node address.

`DynamicRatio` - (Optional) Specifies the fixed ratio value used for a node during ratio load balancing.

`Monitor` - (Optional) specifies the name of the monitor or monitor rule that you want to associate with the node.

`RateLimit` - (Optional) Specifies the maximum number of connections per second allowed for a node or node address. The default value is 'disabled'.

`State` - (Optional) Default is "user-up" you can set to "user-down" if you want to disable.

`Interval` - (Optional) Specifies the amount of time before sending the next DNS query. Default is 3600. This needs to be specified inside the fqdn (fully qualified domain name).

`AddressFamily` - (Optional) Specifies the node's address family. The default is 'unspecified', or IP-agnostic. This needs to be specified inside the fqdn (fully qualified domain name).


## See Also

* [bigip_ltm_node](https://www.terraform.io/docs/providers/bigip/r/ltm_node.html) in the _Terraform Provider Documentation_