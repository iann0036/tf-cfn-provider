# Terraform::NSXT::LbHttpVirtualServer

Provides a resource to configure lb http virtual server on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Enabled` - (Optional) Whether the virtual server is enabled. Default is true.

`IpAddress` - (Required) Virtual server IP address.

`Port` - (Required) Virtual server port.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb http virtual server.

`AccessLogEnabled` - (Optional) Whether access log is enabled. Default is false.

`ApplicationProfileId` - (Required) The application profile defines the application protocol characteristics.

`DefaultPoolMemberPort` - (Optional) Default pool member port.

`MaxConcurrentConnections` - (Optional) To ensure one virtual server does not over consume resources, affecting other applications hosted on the same LBS, connections to a virtual server can be capped. If it is not specified, it means that connections are unlimited.

`MaxNewConnectionRate` - (Optional) To ensure one virtual server does not over consume resources, connections to a member can be rate limited. If it is not specified, it means that connection rate is unlimited.

`PersistenceProfileId` - (Optional) Persistence profile is used to allow related client connections to be sent to the same backend server.

`PoolId` - (Optional) Pool of backend servers. Server pool consists of one or more servers, also referred to as pool members, that are similarly configured and are running the same application.

`SorryPoolId` - (Optional) When load balancer can not select a backend server to serve the request in default pool or pool in rules, the request would be served by sorry server pool.

`RuleIds` - (Optional) List of load balancer rules that provide customization of load balancing behavior using match/action rules.

`ClientSsl` - (Optional) Client side SSL customization.

`ClientSslProfileId` - (Required) Id of client SSL profile that defines reusable properties.

`DefaultCertificateId` - (Required) Id of certificate that will be used if the server does not host     multiple hostnames on the same IP address or if the client does not support SNI extension.

`CertificateChainDepth` - (Optional) Allowed depth of certificate chain. Default is 3.

`ClientAuth` - (Optional) Whether client authentication is mandatory. Default is false.

`CaIds` - (Optional) List of CA certificate ids for client authentication.

`CrlIds` - (Optional) List of CRL certificate ids for client authentication.

`SniCertificateIds` - (Optional) List of certificates to serve different hostnames.

`ServerSsl` - (Optional) Server side SSL customization.

`ServerSslProfileId` - (Required) Id of server SSL profile that defines reusable properties.

`ServerAuth` - (Optional) Whether server authentication is needed. Default is False. If true, ca_ids should be provided.

`CertificateChainDepth` - (Optional) Allowed depth of certificate chain. Default is 3.

`ClientCertificateId` - (Optional) Whether server authentication is required. Default is false.

`CaIds` - (Optional) List of CA certificate ids for server authentication.

`CrlIds` - (Optional) List of CRL certificate ids for server authentication.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb http virtual server.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_http_virtual_server](https://www.terraform.io/docs/providers/nsxt/r/lb_http_virtual_server.html) in the _Terraform Provider Documentation_