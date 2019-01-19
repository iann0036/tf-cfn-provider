# Terraform::Google::ComputeRouterPeer

Manages a Cloud Router BGP peer. For more information see
[the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routers).

## Properties

`Name` - (Required) A unique name for BGP peer, required by GCE. Changing this forces a new peer to be created.

`Router` - (Required) The name of the router in which this BGP peer will be configured. Changing this forces a new peer to be created.

`Interface` - (Required) The name of the interface the BGP peer is associated with. Changing this forces a new peer to be created.

`PeerIpAddress` - (Required) IP address of the BGP interface outside Google Cloud. Changing this forces a new peer to be created.

`PeerAsn` - (Required) Peer BGP Autonomous System Number (ASN). Changing this forces a new peer to be created.

`AdvertisedRoutePriority` - (Optional) The priority of routes advertised to this BGP peer. Changing this forces a new peer to be created.

`Project` - (Optional) The ID of the project in which this peer's router belongs. If it is not provided, the provider project is used. Changing this forces a new peer to be created.

`Region` - (Optional) The region this peer's router sits in. If not specified, the project region will be used. Changing this forces a new peer to be created.


## Return Values

### Fn::GetAtt

`IpAddress` - IP address of the interface inside Google Cloud Platform.

## See Also

* [google_compute_router_peer](https://www.terraform.io/docs/providers/google/r/compute_router_peer.html) in the _Terraform Provider Documentation_