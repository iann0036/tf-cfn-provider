# Terraform::OPC::LbaasLoadBalancer

The `Terraform::OPC::LbaasLoadBalancer` resource creates and manages a Load Balancer Classic instance in an Oracle Cloud Infrastructure Classic Compute region. You must define server pools, create at least one listener, and optionally define the policies for the load balancer before it will be operational.

## Properties

`Name` - (Required) The name of the Load Balancer.

`Region` - (Required) The region in which to create the Load Balancer, e.g. `uscom-central-1`.

`Scheme` - (Required) Set to either `INTERNET_FACING` or `INTERNAL`.

`Description` - (Optional) A short description for the load balancer. The description must not exceed 1000 characters.

`Enabled` - (Optional) Boolean flag to enable or disable the Load Balancer. Default is `true` (enabled).

`IpNetwork` - (Optional) Fully qualified three part name of the IP network to be associated with the load balancer.

`ParentLoadBalancer` - (Optional) Select a parent load balancer if you want to create a dependent load balancer.

`PermittedClients` - (Optional) List of permitted client IP addresses or CIDR ranges which can connect to this load balancer on the configured Listener ports. If not set all connections are permitted.

`PermittedMethods` - (Optional) List of permitted HTTP methods. e.g. `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD` or you can also create your own custom methods. Requests with methods not listed in this field will result in a 403 (unauthorized access) response.

`Tags` - (Optional) List of tags.


## See Also

* [opc_lbaas_load_balancer](https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer.html) in the _Terraform Provider Documentation_