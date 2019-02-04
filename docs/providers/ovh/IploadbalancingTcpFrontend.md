# Terraform::OVH::IploadbalancingTcpFrontend

Creates a backend server group (frontend) to be used by loadbalancing frontend(s)

## Properties

`ServiceName` - (Required) The internal name of your IP load balancing.

`DisplayName` - Human readable name for your frontend, this field is for you.

`Port` - Port(s) attached to your frontend. Supports single port (numerical value),
range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
and/or 'range'. Each port must be in the [1;49151] range.

`Zone` - (Required) Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`).

`AllowedSource` - Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.

`DedicatedIpfo` - Only attach frontend on these ip. No restriction if null. List of Ip blocks.

`DefaultFarmId` - Default TCP Farm of your frontend.

`DefaultSslId` - Default ssl served to your customer.

`Disabled` - Disable your frontend. Default: 'false'.

`Ssl` - SSL deciphering. Default: 'false'.


## Return Values

### Fn::GetAtt

`Id` - Id of your frontend.

`DisplayName` - See Properties above.

`AllowedSource` - See Properties above.

`DedicatedIpfo` - See Properties above.

`DefaultFarmId` - See Properties above.

`DefaultSslId` - See Properties above.

`Disabled` - See Properties above.

`Ssl` - See Properties above.

## See Also

* [ovh_iploadbalancing_tcp_frontend](https://www.terraform.io/docs/providers/ovh/r/iploadbalancing_tcp_frontend.html) in the _Terraform Provider Documentation_