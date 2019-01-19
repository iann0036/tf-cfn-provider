# Terraform::CLC::LoadBalancerPool

Manages a CLC load balancer pool. Manage related frontend with [clc_load_balancer](load_balancer.html)

See also [Complete API documentation](https://www.ctl.io/api-docs/v2/#shared-load-balancer).

## Properties

`LoadBalancer` - (Required, string) The id of the load balancer.

`DataCenter` - (Required, string) The datacenter location for this pool.

`Port` - (Required, int) Either 80 or 443.

`Method` - (Optional, string) The configured balancing method. Either "roundRobin" (default) or "leastConnection".

`Persistence` - (Optional, string) The configured persistence method. Either "standard" (default) or "sticky".


## See Also

* [clc_load_balancer_pool](https://www.terraform.io/docs/providers/clc/r/load_balancer_pool.html) in the _Terraform Provider Documentation_