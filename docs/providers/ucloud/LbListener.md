# Terraform::UCloud::LbListener

Provides a Load Balancer Listener resource.

## Properties

`LoadBalancerId` - (Required) The ID of load balancer instance.

`Protocol` - (Required) Listener protocol. Possible values: `http`, `https` if `ListenType` is `request_proxy`, `tcp` and `udp` if `ListenType` is `packets_transmit`.

`Name` - (Optional) The name of the listener. (Default: `Listener`).

`ListenType` - (Optional) The type of listener. Possible values are `request_proxy` and `packets_transmit`. (Default: `packets_transmit`).

`Port` - (Optional) Port opened on the listeners to receive requests, range: 1-65535. (Default: `80`).

`IdleTimeout` - (Optional) Amount of time in seconds to wait for the response for in between two sessions if `ListenType` is `request_proxy`, range: 0-86400. (Default: `60`). Amount of time in seconds to wait for one session if `ListenType` is `packets_transmit`, range: 60-900. The session will be closed as soon as no response if it is `0`.

`Method` - (Optional) The load balance method in which the listener is. Possible values are: `roundrobin`, `source`, `consistent_hash`, `source_port` , `consistent_hash_port`, `weight_roundrobin` and `leastconn`. (Default: `roundrobin`). - The `consistent_hash`, `source_port` , `consistent_hash_port`, `roundrobin`, `source` and `weight_roundrobin` are valid if `ListenType` is `packets_transmit`. - The `Roundrobin`, `Source` and `WeightRoundrobin` and `Leastconn` are vaild if `ListenType` is `request_proxy`.

`Persistence` - (Optional) Indicate whether the persistence session is enabled, it is invaild if `PersistenceType` is `none`, an auto-generated string will be exported if `PersistenceType` is `server_insert`, a custom string will be exported if `PersistenceType` is `user_defined`.

`PersistenceType` - (Optional) The type of session persistence of listener. Possible values are: `none` as disabled, `server_insert` as auto-generated string and `user_defined` as cutom string. (Default: `none`).

`HealthCheckType` - (Optional) Health check method. Possible values are `Port` as port checking and `Path` as http checking.

`Path` - (Optional) Health check path checking.

`Domain` - (Optional) Health check domain checking.


## Return Values

### Fn::GetAtt

`Status` - Listener status. Possible values are: `allNormal` for all resource functioning well, `partNormal` for partial resource functioning well and `allException` for all resource functioning exceptional.

## See Also

* [ucloud_lb_listener](https://www.terraform.io/docs/providers/ucloud/r/lb_listener.html) in the _Terraform Provider Documentation_