# Terraform::OpenTelekomCloud::ElbListener

Manages an elastic loadbalancer listener resource within OpentelekomCloud.

## Properties

`Region` - (Optional) The region in which to create the elb listener. If omitted, the `Region` argument of the provider is used. Changing this creates a new elb listener.

`Name` - (Required) Specifies the load balancer name. The name is a string of 1 to 64 characters that consist of letters, digits, underscores (_), and hyphens (-).

`Description` - (Optional) Provides supplementary information about the listener. The value is a string of 0 to 128 characters and cannot be <>.

`LoadbalancerId` - (Required) Specifies the ID of the load balancer to which the listener belongs.  Changing this creates a new elb listener.

`Protocol` - (Required) Specifies the listening protocol used for layer 4 or 7. The value can be HTTP, TCP, HTTPS, or UDP.  Changing this creates a new elb listener.

`ProtocolPort` - (Required) Specifies the listening port. The value ranges from 1 to 65535.

`BackendProtocol` - (Required) Specifies the backend protocol. If the value of protocol is UDP, the value of this parameter can only be UDP. The value can be HTTP, TCP, or UDP.  Changing this creates a new elb listener.

`BackendPort` - (Required) Specifies the backend port. The value ranges from 1 to 65535.

`LbAlgorithm` - (Required) Specifies the load balancing algorithm for the listener. The value can be roundrobin, leastconn, or source.

`SessionSticky` - (Optional) Specifies whether to enable sticky session. The value can be true or false. The Sticky session is enabled when the value is true, and is disabled when the value is false. If the value of protocol is HTTP, HTTPS, or TCP, and the value of lb_algorithm is not roundrobin, the value of this parameter can only be false.  Changing this creates a new elb listener.

`StickySessionType` - (Optional) Specifies the cookie processing method. The value is insert. insert indicates that the cookie is inserted by the load balancer. This parameter is valid when protocol is set to HTTP, and session_sticky to true. The default value is insert. This parameter is invalid when protocol is set to TCP or UDP, which means the parameter is empty.  Changing this creates a new elb listener.

`CookieTimeout` - (Optional) Specifies the cookie timeout period (minutes). This parameter is valid when protocol is set to HTTP, session_sticky to true, and sticky_session_type to insert. This parameter is invalid when protocol is set to TCP or UDP. The value ranges from 1 to 1440.  Changing this creates a new elb listener.

`TcpTimeout` - (Optional) Specifies the TCP timeout period (minutes). This parameter is valid when protocol is set to TCP. The value ranges from 1 to 5.

`TcpDraining` - (Optional) Specifies whether to maintain the TCP connection to the backend ECS after the ECS is deleted. This parameter is valid when protocol is set to TCP. The value can be true or false.

`TcpDrainingTimeout` - (Optional) Specifies the timeout duration (minutes) for the TCP connection to the backend ECS after the ECS is deleted. This parameter is valid when protocol is set to TCP, and tcp_draining to true. The value ranges from 0 to 60.

`CertificateId` - (Optional) Specifies the ID of the SSL certificate used for security authentication when HTTPS is used to make API calls. This parameter is mandatory if the value of protocol is HTTPS. The value can be obtained by viewing the details of the SSL certificate.  Changing this creates a new elb listener.

`UdpTimeout` - (Optional) Specifies the UDP timeout duration (minutes). This parameter is valid when protocol is set to UDP. The value ranges from 1 to 1440.

`SslProtocols` - (Optional) Specifies the SSL protocol standard supported by a tracker, which is used for enabling specified encryption protocols. This parameter is valid only when the value of protocol is set to HTTPS. The value is TLSv1.2 or TLSv1.2 TLSv1.1 TLSv1. The default value is TLSv1.2. Changing this creates a new elb listener.

`SslCiphers` - (Optional) Specifies the cipher suite of an encryption protocol. This parameter is valid only when the value of protocol is set to HTTPS. The value is Default, Extended, or Strict. The default value is Default. The value can only be set to Extended if the value of ssl_protocols is set to TLSv1.2 TLSv1.1 TLSv1.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`LoadbalancerId` - See Properties above.

`Protocol` - See Properties above.

`ProtocolPort` - See Properties above.

`BackendProtocol` - See Properties above.

`BackendPort` - See Properties above.

`LbAlgorithm` - See Properties above.

`SessionSticky` - See Properties above.

`StickySessionType` - See Properties above.

`CookieTimeout` - See Properties above.

`TcpTimeout` - See Properties above.

`TcpDraining` - See Properties above.

`TcpDrainingTimeout` - See Properties above.

`CertificateId` - See Properties above.

`UdpTimeout` - See Properties above.

`SslProtocols` - See Properties above.

`SslCiphers` - See Properties above.

`Id` - Specifies the listener ID.

`AdminStateUp` - Specifies the status of the load balancer. Value range:.

## See Also

* [opentelekomcloud_elb_listener](https://www.terraform.io/docs/providers/opentelekomcloud/r/elb_listener.html) in the _Terraform Provider Documentation_