# Terraform::OPC::LbaasServerPool

The `Terraform::OPC::LbaasServerPool` resource creates and manages a Load Balancer Classic Origin Server Pool for a Load Balancer Classic instance. The Server Pool defines one or more servers (referred to as origin servers) to which the load balancer can distribute requests.

## Properties

`Name` - (Required) The name of the Server Pool.

`LoadBalancer` - (Required) The parent Load Balancer the Origin Server Pool.

`Servers` - (Required) List of servers in the Server Pool. To define the server in the server pool, provide IP address or DNS name of the compute instances, and port for load balancer to direct traffic to, in the format `host:port`.

`Enabled` - (Optional) Boolean flag to enable or disable the Server Pool. Default is `true` (enabled).

`HealthCheck` - (Optional) Enables Load Balancer health check, see [Health Check Attributes](#health-check-attributes).

`Tags` - (Optional) List of tags.

`VnicSet` - (Optional) Fully qualified three part name of a vNICSet to be associated with the server pool vNIC. Load Balancer uses this vNICSet to set the right ACLs to allow egress traffic from the load balancer.


## See Also

* [opc_lbaas_server_pool](https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool.html) in the _Terraform Provider Documentation_