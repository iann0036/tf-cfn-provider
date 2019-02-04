# Terraform::OCI::LoadBalancerListener

This resource provides the Listener resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a listener to a load balancer.

## Properties

`ConnectionConfiguration` - (Optional) (Updatable)
* `IdleTimeoutInSeconds` - (Required) (Updatable) The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.

`IdleTimeoutInSeconds` - (Required) (Updatable) The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.

`DefaultBackendSetName` - (Required) (Updatable) The name of the associated backend set.  Example: `example_backend_set`.

`HostnameNames` - (Optional) (Updatable) An array of hostname resource names.

`LoadBalancerId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a listener.

`Name` - (Required) A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_listener`.

`PathRouteSetName` - (Optional) (Updatable) The name of the set of path-based routing rules, [PathRouteSet](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/), applied to this listener's traffic.  Example: `example_path_route_set`.

`Port` - (Required) (Updatable) The communication port for the listener.  Example: `80`.

`Protocol` - (Required) (Updatable) The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols) operation.  Example: `HTTP`.

`RuleSetNames` - (Optional) (Updatable) The names of the [rule sets](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.  Example: ["example_rule_set"].

`SslConfiguration` - (Optional) (Updatable)
* `CertificateName` - (Required) (Updatable) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.  Example: `example_certificate_bundle`
* `VerifyDepth` - (Optional) (Updatable) The maximum depth for peer certificate chain verification.  Example: `3`
* `VerifyPeerCertificate` - (Optional) (Updatable) Whether the load balancer listener should verify peer certificates.  Example: `true`.

`CertificateName` - (Required) (Updatable) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.  Example: `example_certificate_bundle`
* `VerifyDepth` - (Optional) (Updatable) The maximum depth for peer certificate chain verification.  Example: `3`
* `VerifyPeerCertificate` - (Optional) (Updatable) Whether the load balancer listener should verify peer certificates.  Example: `true`.

`VerifyDepth` - (Optional) (Updatable) The maximum depth for peer certificate chain verification.  Example: `3`
* `VerifyPeerCertificate` - (Optional) (Updatable) Whether the load balancer listener should verify peer certificates.  Example: `true`.

`VerifyPeerCertificate` - (Optional) (Updatable) Whether the load balancer listener should verify peer certificates.  Example: `true`.


## Return Values

### Fn::GetAtt

`IdleTimeoutInSeconds` - The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.  The default values are:  *  300 seconds for TCP  *  60 seconds for HTTP and WebSocket protocols.  Note: The protocol is set at the listener.  Modify this parameter if the client or backend server stops transmitting data for more than the default time. Some examples include:  *  The client sends a database query to the backend server and the database takes over 300 seconds to execute.    Therefore, the backend server does not transmit any data within 300 seconds.  *  The client uploads data using the HTTP protocol. During the upload, the backend does not transmit any data    to the client for more than 60 seconds.  *  The client downloads data using the HTTP protocol.  After the initial request, it stops transmitting data to    the backend server for more than 60 seconds.  *  The client starts transmitting data after establishing a WebSocket connection, but the backend server does    not transmit data for more than 60 seconds.  *  The backend server starts transmitting data after establishing a WebSocket connection, but the client does    not transmit data for more than 60 seconds.  The maximum value is 7200 seconds. Contact My Oracle Support to file a service request if you want to increase this limit for your tenancy. For more information, see [Service Limits](https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/servicelimits.htm).  Example: `1200`.

`DefaultBackendSetName` - The name of the associated backend set.  Example: `example_backend_set`.

`HostnameNames` - An array of hostname resource names.

`LoadBalancerId` - The [OCID](https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a listener.

`Name` - A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `My listener`.

`PathRouteSetName` - The name of the set of path-based routing rules, [PathRouteSet](https://docs.us-phoenix-1.oraclecloud.com/api/#/en/loadbalancer/20170115/PathRouteSet/), applied to this listener's traffic.  Example: `path-route-set-001`.

`Port` - The communication port for the listener.  Example: `80`.

`Protocol` - The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the [ListProtocols](https://docs.us-phoenix-1.oraclecloud.com/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols) operation.  Example: `HTTP`.

`CertificateName` - A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.  Example: `example_certificate_bundle`.

`VerifyDepth` - The maximum depth for peer certificate chain verification.  Example: `3`.

`VerifyPeerCertificate` - Whether the load balancer listener should verify peer certificates.  Example: `true`.

## See Also

* [oci_load_balancer_listener](https://www.terraform.io/docs/providers/oci/r/load_balancer_listener.html) in the _Terraform Provider Documentation_