# Terraform::OVH::IploadbalancingTcpFarm

Creates a backend server group (farm) to be used by loadbalancing frontend(s)

## Properties

`ServiceName` - (Required) The internal name of your IP load balancing.

`Balance` - Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`).

`DisplayName` - Readable label for loadbalancer farm.

`Port` - Port attached to your farm ([1..49151]). Inherited from frontend if null.

`Stickiness` - 	Stickiness type. No stickiness if null (`sourceIp`).

`VrackNetworkId` - Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack.

`Zone` - (Required) Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`).

`Probe` - define a backend healthcheck probe.

`Type` - (Required) Valid values : `http`, `internal`, `mysql`, `oko`, `pgsql`, `smtp`, `tcp`.

`Interval` - probe interval, Value between 30 and 3600 seconds, default 30.

`Match` - What to mach `Pattern` against (`contains`, `default`, `internal`, `matches`, `status`).

`Port` - Port for backends to recieve traffic on.

`Negate` - Negate probe result.

`Pattern` - Pattern to match against `Match`.

`ForceSsl` - Force use of SSL (TLS).

`Url` - URL for HTTP probe type.

`Method` - HTTP probe method (`GET`, `HEAD`, `OPTIONS`, `internal`).


## Return Values

### Fn::GetAtt

`ServiceName` - See Properties above.

`Balance` - See Properties above.

`DisplayName` - See Properties above.

`Port` - See Properties above.

`Stickiness` - See Properties above.

`VrackNetworkId` - See Properties above.

`Zone` - See Properties above.

`Probe` - See Properties above.

`Type` - See Properties above.

`Interval` - See Properties above.

`Match` - See Properties above.

`Negate` - See Properties above.

`Pattern` - See Properties above.

`ForceSsl` - See Properties above.

`Url` - See Properties above.

`Method` - See Properties above.

## See Also

* [ovh_iploadbalancing_tcp_farm](https://www.terraform.io/docs/providers/ovh/r/iploadbalancing_tcp_farm.html) in the _Terraform Provider Documentation_