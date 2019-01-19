# Terraform::BIGIP::NetRoute

`Terraform::BIGIP::NetRoute` Manages a route configuration

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Name` - (Required) Name of the route.

`Network` - (Optional) The destination subnet and netmask for the route.

`Network` - (Optional) Specifies a gateway address for the route.


## See Also

* [bigip_net_route](https://www.terraform.io/docs/providers/bigip/r/net_route.html) in the _Terraform Provider Documentation_