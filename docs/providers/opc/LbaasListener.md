# Terraform::OPC::LbaasListener

The `Terraform::OPC::LbaasListener` resource creates and manages a Load Balancer Classic Listener for a Load Balancer Classic instance.

## Properties

`Name` - (Required) The name of the Listener.

`LoadBalancer` - (Required) The parent Load Balancer the Listener.

`BalancerProtocol` - (Required)  transport protocol that will be accepted for all incoming requests to the selected load balancer listener. `HTTP` or `HTTPS`. If set to HTTPS then you must also set the server `Certificates`.

`Port` - (Required) The port on which the Load Balancer is listening.

`ServerProtocol` - (Required) The protocol to be used for routing traffic to the origin servers in the server pool. `HTTP` or `HTTPS`. If set to `HTTPS` then you must include a Trusted Certificate Policy in the `policies`.

`Enabled` - (Optional) Boolean flag to enable or disable the Listener. Default is `true` (enabled).

`PathPrefixes` - (Optional) List of paths to configure the listener to accept only requests that are targeted to a specific path within the URI of the request.

`Polices` - (Optional) List of the Load Balancer Policy URIs to apply to the listener.

`ServerPool` - (Optional) URI of the Server Pool resource to which the load balancer distributes requests.

`Certificates` - (Optional) The URI of the server security certificate.

`Tags` - (Optional) List of tags.

`VirtualHosts` - (Optional) Configure the listener to only accept URI requests that include the host names listed in this field.


## See Also

* [opc_lbaas_listener](https://www.terraform.io/docs/providers/opc/r/lbaas_listener.html) in the _Terraform Provider Documentation_