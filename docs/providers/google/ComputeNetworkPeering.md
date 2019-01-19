# Terraform::Google::ComputeNetworkPeering

Manages a network peering within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc/vpc-peering)
and
[API](https://cloud.google.com/compute/docs/reference/latest/networks).

~> **Note:** Both network must create a peering with each other for the peering to be functional.

~> **Note:** Subnets IP ranges across peered VPC networks cannot overlap.

## Properties

`Name` - (Required) Name of the peering.

`Network` - (Required) Resource link of the network to add a peering to.

`PeerNetwork` - (Required) Resource link of the peer network.

`AutoCreateRoutes` - (Optional) If set to `true`, the routes between the two networks will be created and managed automatically. Defaults to `true`.


## Return Values

### Fn::GetAtt

`State` - State for the peering.

`StateDetails` - Details about the current state of the peering.

## See Also

* [google_compute_network_peering](https://www.terraform.io/docs/providers/google/r/compute_network_peering.html) in the _Terraform Provider Documentation_