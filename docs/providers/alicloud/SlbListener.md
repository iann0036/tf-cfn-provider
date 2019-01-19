# Terraform::Alicloud::SlbListener

Provides an Application Load Balancer Listener resource.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about listener and how to use it, to see the following:

* [Configure a HTTP Listener](https://www.alibabacloud.com/help/doc-detail/27592.htm).
* [Configure a HTTPS Listener](https://www.alibabacloud.com/help/doc-detail/27593.htm).
* [Configure a TCP Listener](https://www.alibabacloud.com/help/doc-detail/27594.htm).
* [Configure a UDP Listener](https://www.alibabacloud.com/help/doc-detail/27595.htm).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the load balancer listener. It is consist of `load_balancer_id` and `frontend_port`: `<load_balancer_id>:<frontend_port>`.

`LoadBalancerId` - The Load Balancer ID which is used to launch a new listener.

`FrontendPort` - Port used by the Server Load Balancer instance frontend.

`BackendPort` - Port used by the Server Load Balancer instance backend.

`Protocol` - The protocol to listen on.

`Bandwidth` - Bandwidth peak of Listener.

`Scheduler` - Scheduling algorithm.

`StickySession` - Whether to enable session persistence.

`StickySessionType` - Mode for handling the cookie.

`CookieTimeout` - Cookie timeout.

`Cookie` - The cookie configured on the server.

`PersistenceTimeout` - Timeout of connection persistence.

`HealthCheck` - Whether to enable health check.

`HealthCheckType` - Type of health check.

`HealthCheckDomain` - Domain name used for health check.

`HealthCheckUri` - URI used for health check.

`HealthCheckConnectPort` - Port used for health check.

`HealthyThreshold` - Threshold determining the result of the health check is success.

`UnhealthyThreshold` - Threshold determining the result of the health check is fail.

`HealthCheckTimeout` - Maximum timeout of each health check response.

`HealthCheckInterval` - Time interval of health checks.

`HealthCheckHttpCode` - Regular health check HTTP status code.

`SslCertificateId` - (Optinal) Security certificate ID.

## See Also

* [alicloud_slb_listener](https://www.terraform.io/docs/providers/alicloud/r/slb_listener.html) in the _Terraform Provider Documentation_