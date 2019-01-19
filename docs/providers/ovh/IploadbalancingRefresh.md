# Terraform::OVH::IploadbalancingRefresh

Applies changes from other ovh_iploadbalancing_* resourcesto the production configuration of loadbalancers.

## Properties

`ServiceName` - (Required) The internal name of your IP load balancing.

`Keepers` - List of values traccked to trigger refresh, used also to form implicit dependencies.


## Return Values

### Fn::GetAtt

`ServiceName` - See Properties above.

`Keepers` - See Properties above.

## See Also

* [ovh_iploadbalancing_refresh](https://www.terraform.io/docs/providers/ovh/r/iploadbalancing_refresh.html) in the _Terraform Provider Documentation_