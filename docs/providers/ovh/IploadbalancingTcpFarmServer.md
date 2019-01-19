# Terraform::OVH::IploadbalancingTcpFarmServer

Creates a backend server entry linked to loadbalancing group (farm)

## Properties

`ServiceName` - (Required) The internal name of your IP load balancing.

`FarmId` - ID of the farm this server is attached to.

`DisplayName` - Label for the server.

`Address` - Address of the backend server (IP from either internal or OVH network).

`Status` - backend status - `active` or `inactive`.

`Port` - Port that backend will respond on.

`ProxyProtocolVersion` - version of the PROXY protocol used to pass origin connection information from loadbalancer to recieving service (`v1`, `v2`, `v2-ssl`, `v2-ssl-cn`).

`Weight` - used in loadbalancing algorithm.

`Probe` - defines if backend will be probed to determine health and keep as active in farm if healthy.

`Ssl` - is the connection ciphered with SSL (TLS).

`Backup` - is it a backup server used in case of failure of all the non-backup backends.


## Return Values

### Fn::GetAtt

`ServiceName` - See Properties above.

`FarmId` - See Properties above.

`DisplayName` - See Properties above.

`Address` - See Properties above.

`Status` - See Properties above.

`Port` - See Properties above.

`ProxyProtocolVersion` - See Properties above.

`Weight` - See Properties above.

`Probe` - See Properties above.

`Ssl` - See Properties above.

`Backup` - See Properties above.

`Cookie` - Value of the stickiness cookie used for this backend.

## See Also

* [ovh_iploadbalancing_tcp_farm_server](https://www.terraform.io/docs/providers/ovh/r/iploadbalancing_tcp_farm_server.html) in the _Terraform Provider Documentation_