# Terraform::OCI::LoadBalancerBackend

This resource provides the Backend resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a backend server to a backend set.

## Properties

`BackendsetName` - (Required) The name of the backend set to add the backend server to.  Example: `example_backend_set`.

`Backup` - (Optional) (Updatable) Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "backup" fail the health check policy.  Example: `false`.

`Drain` - (Optional) (Updatable) Whether the load balancer should drain this server. Servers marked "drain" receive no new incoming traffic.  Example: `false`.

`IpAddress` - (Required) The IP address of the backend server.  Example: `10.0.0.3`.

`LoadBalancerId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend set and servers.

`Offline` - (Optional) (Updatable) Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`.

`Port` - (Required) The communication port for the backend server.  Example: `8080`.

`Weight` - (Optional) (Updatable) The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).  Example: `3`.


## Return Values

### Fn::GetAtt

`Drain` - Whether the load balancer should drain this server. Servers marked "drain" receive no new incoming traffic.  Example: `false`.

`Name` - A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.  Example: `10.0.0.3:8080`.

`Weight` - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).  Example: `3`.

`Backup` - Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "backup" fail the health check policy.  Example: `false`.

`Offline` - Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`.

`IpAddress` - The IP address of the backend server.  Example: `10.0.0.3`.

`Port` - The communication port for the backend server.  Example: `8080`.

## See Also

* [oci_load_balancer_backend](https://www.terraform.io/docs/providers/oci/r/load_balancer_backend.html) in the _Terraform Provider Documentation_