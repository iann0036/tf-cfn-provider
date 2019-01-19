# Terraform::Alicloud::SlbListener

Provides an Application Load Balancer Listener resource.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about listener and how to use it, to see the following:

* [Configure a HTTP Listener](https://www.alibabacloud.com/help/doc-detail/27592.htm).
* [Configure a HTTPS Listener](https://www.alibabacloud.com/help/doc-detail/27593.htm).
* [Configure a TCP Listener](https://www.alibabacloud.com/help/doc-detail/27594.htm).
* [Configure a UDP Listener](https://www.alibabacloud.com/help/doc-detail/27595.htm).

## Properties

`LoadBalancerId` - (Required, ForceNew) The Load Balancer ID which is used to launch a new listener.

`FrontendPort` - (Required, ForceNew) Port used by the Server Load Balancer instance frontend. Valid value range: [1-65535].

`BackendPort` - (Required, ForceNew) Port used by the Server Load Balancer instance backend. Valid value range: [1-65535].

`Protocol` - (Required, ForceNew) The protocol to listen on. Valid values are [`http`, `https`, `tcp`, `udp`].

`Bandwidth` - (Required) Bandwidth peak of Listener. For the public network instance charged per traffic consumed, the Bandwidth on Listener can be set to -1, indicating the bandwidth peak is unlimited. Valid values are [-1, 1-1000] in Mbps.

`Scheduler` - (Optinal) Scheduling algorithm, Valid values are `wrr` and `wlc`.  Default to "wrr".

`StickySession` - (Optinal) Whether to enable session persistence, Valid values are `on` and `off`. Default to `off`.

`StickySessionType` - (Optinal) Mode for handling the cookie. If `StickySession` is "on", it is mandatory. Otherwise, it will be ignored. Valid values are `insert` and `server`. `insert` means it is inserted from Server Load Balancer; `server` means the Server Load Balancer learns from the backend server.

`CookieTimeout` - (Optinal) Cookie timeout. It is mandatory when `StickySession` is "on" and `StickySessionType` is "insert". Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.

`Cookie` - (Optinal) The cookie configured on the server. It is mandatory when `StickySession` is "on" and `StickySessionType` is "server". Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.

`PersistenceTimeout` - (Optinal) Timeout of connection persistence. Valid value range: [0-3600] in seconds. Default to 0 and means closing it.

`HealthCheck` - (Optinal) Whether to enable health check. Valid values are`on` and `off`. TCP and UDP listener's HealthCheck is always on, so it will be ignore when launching TCP or UDP listener.

`HealthCheckType` - (Optinal) Type of health check. Valid values are: `tcp` and `http`. Default to `tcp` . TCP supports TCP and HTTP health check mode, you can select the particular mode depending on your application.

`HealthCheckDomain` - (Optinal) Domain name used for health check. When it used to launch TCP listener, `HealthCheckType` must be "http". Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.

`HealthCheckUri` - (Optinal) URI used for health check. When it used to launch TCP listener, `HealthCheckType` must be "http". Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&’ are allowed.

`HealthCheckConnectPort` - (Optinal) Port used for health check. Valid value range: [1-65535]. Default to "None" means the backend server port is used.

`HealthyThreshold` - (Optinal) Threshold determining the result of the health check is success. It is required when `HealthCheck` is on. Valid value range: [1-10] in seconds. Default to 3.

`UnhealthyThreshold` - (Optinal) Threshold determining the result of the health check is fail. It is required when `HealthCheck` is on. Valid value range: [1-10] in seconds. Default to 3.

`HealthCheckTimeout` - (Optinal) Maximum timeout of each health check response. It is required when `HealthCheck` is on. Valid value range: [1-300] in seconds. Default to 5. Note: If `HealthCheckTimeout` < `HealthCheckInterval`, its will be replaced by `HealthCheckInterval`.

`HealthCheckInterval` - (Optinal) Time interval of health checks. It is required when `HealthCheck` is on. Valid value range: [1-50] in seconds. Default to 2.

`HealthCheckHttpCode` - (Optinal) Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when `HealthCheck` is on. Default to `http_2xx`.  Valid values are: `http_2xx`,  `http_3xx`, `http_4xx` and `http_5xx`.

`SslCertificateId` - (Optinal) Security certificate ID. It is required when `Protocol` is `https`.

`Gzip` - (Optinal) Whether to enable "Gzip Compression". If enabled, files of specific file types will be compressed, otherwise, no files will be compressed. Default to true. Available in v1.13.0+.

`XForwardedFor` - (Optinal) Whether to set additional HTTP Header field "X-Forwarded-For" (documented below). Available in v1.13.0+.

`AclStatus` - (Optinal) Whether to enable "acl(access control list)", the acl is specified by `AclId`. Valid values are `on` and `off`. Default to `off`.

`AclType` - (Optinal) Mode for handling the acl specified by acl_id. If `AclStatus` is "on", it is mandatory. Otherwise, it will be ignored. Valid values are `white` and `black`. `white` means the Listener can only be accessed by client ip belongs to the acl; `black` means the Listener can not be accessed by client ip belongs to the acl.

`AclId` - (Optinal) the id of access control list to be apply on the listener, is the id of resource alicloud_slb_acl. If `AclStatus` is "on", it is mandatory. Otherwise, it will be ignored.

`EstablishedTimeout` - (Optinal) Timeout of tcp listener established connection idle timeout. Valid value range: [10-900] in seconds. Default to 900.

`IdleTimeout` - (Optinal) Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.

`RequestTimeout` - (Optinal) Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.

`EnableHttp2` - (Optinal) Whether to enable https listener support http2 or not. Valid values are `on` and `off`. Default to `on`.

`TlsCipherPolicy` - (Optinal)  Https listener TLS cipher policy. Valid values are `tls_cipher_policy_1_0`, `tls_cipher_policy_1_1`, `tls_cipher_policy_1_2`, `tls_cipher_policy_1_2_strict`. Default to `tls_cipher_policy_1_0`. Currently the `TlsCipherPolicy` can not be updated when load balancer instance is "Shared-Performance".

`ServerGroupId` - (Optinal) the id of server group to be apply on the listener, is the id of resource `Terraform::Alicloud::SlbServerGroup`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the load balancer listener. It is consist of `LoadBalancerId` and `FrontendPort`: `<load_balancer_id>:<frontend_port>`.

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