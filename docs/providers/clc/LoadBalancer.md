# Terraform::CLC::LoadBalancer

Manages a CLC load balancer. Manage connected backends with [clc_load_balancer_pool](load_balancer_pool.html)

See also [Complete API documentation](https://www.ctl.io/api-docs/v2/#shared-load-balancer).

## Properties

`Name` - (Required, string) The name of the load balancer.

`DataCenter` - (Required, string) The datacenter location of both parent group and this group.

`Status` - (Required, string) Either "enabled" or "disabled".

`Description` - (Optional, string) Description for server group (visible in control portal only).

`IpAddress` - (Computed) The IP of the load balancer.


## See Also

* [clc_load_balancer](https://www.terraform.io/docs/providers/clc/r/load_balancer.html) in the _Terraform Provider Documentation_