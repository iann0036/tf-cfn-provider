# Terraform::NSXT::LbUdpVirtualServer

Provides a resource to configure lb udp virtual server on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Enabled` - (Optional) Whether the virtual server is enabled. Default is true.

`IpAddress` - (Required) Virtual server IP address.

`Ports` - (Required) List of virtual server port.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb udp virtual server.

`AccessLogEnabled` - (Optional) Whether access log is enabled. Default is false.

`ApplicationProfileId` - (Required) The application profile defines the application protocol characteristics.

`DefaultPoolMemberPorts` - (Optional) List of default pool member ports.

`MaxConcurrentConnections` - (Optional) To ensure one virtual server does not over consume resources, affecting other applications hosted on the same LBS, connections to a virtual server can be capped. If it is not specified, it means that connections are unlimited.

`MaxNewConnectionRate` - (Optional) To ensure one virtual server does not over consume resources, connections to a member can be rate limited. If it is not specified, it means that connection rate is unlimited.

`PersistenceProfileId` - (Optional) Persistence profile is used to allow related client connections to be sent to the same backend server. Only source ip persistence profile is accepted.

`PoolId` - (Optional) Pool of backend servers. Server pool consists of one or more servers, also referred to as pool members, that are similarly configured and are running the same application.

`SorryPoolId` - (Optional) When load balancer can not select a backend server to serve the request in default pool or pool in rules, the request would be served by sorry server pool.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb udp virtual server.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_udp_virtual_server](https://www.terraform.io/docs/providers/nsxt/r/lb_udp_virtual_server.html) in the _Terraform Provider Documentation_