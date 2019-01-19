# Terraform::OCI::LoadBalancerBackendSet

Other supported legacy names/aliases:
  * `oci_load_balancer_backendset`

This resource provides the Backend Set resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a backend set to a load balancer.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Backup` - Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as "backup" fail the health check policy.  Example: `false`.

`Drain` - Whether the load balancer should drain this server. Servers marked "drain" receive no new incoming traffic.  Example: `false`.

`IpAddress` - The IP address of the backend server.  Example: `10.0.0.3`.

`Name` - A friendly name for the backend set. It must be unique and it cannot be changed.

`Offline` - Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.  Example: `false`.

`Port` - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the `Backend` object.  Example: `8080`.

`Weight` - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. For more information on load balancing policies, see [How Load Balancing Policies Work](https://docs.cloud.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).  Example: `3`.

`IntervalMs` - The interval between health checks, in milliseconds. The default is 30000 (30 seconds).  Example: `30000`.

`Protocol` - The protocol the health check must use; either HTTP or TCP.  Example: `HTTP`.

`ResponseBodyRegex` - A regular expression for parsing the response body from the backend server.  Example: `^((?!false).|\s)*$`.

`Retries` - The number of retries to attempt before a backend server is considered "unhealthy". Defaults to 3.  Example: `3`.

`ReturnCode` - The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, you can use common HTTP status codes such as "200".  Example: `200`.

`TimeoutInMillis` - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. Defaults to 3000 (3 seconds).  Example: `3000`.

`UrlPath` - The path against which to run the health check.  Example: `/healthcheck`.

`Policy` - The load balancer policy for the backend set. To get a list of available policies, use the [ListPolicies](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.  Example: `LEAST_CONNECTIONS`.

`CookieName` - The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist.  Example: `example_cookie`.

`DisableFallback` - Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.  Example: `false`.

`CertificateName` - A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.  Example: `example_certificate_bundle`.

`VerifyDepth` - The maximum depth for peer certificate chain verification.  Example: `3`.

`VerifyPeerCertificate` - Whether the load balancer listener should verify peer certificates. Defaults to true.   Example: `true`.

## See Also

* [oci_load_balancer_backend_set](https://www.terraform.io/docs/providers/oci/r/load_balancer_backend_set.html) in the _Terraform Provider Documentation_