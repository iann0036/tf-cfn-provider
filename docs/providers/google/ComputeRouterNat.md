# Terraform::Google::ComputeRouterNat

Manages a Cloud NAT. For more information see
[the official documentation](https://cloud.google.com/nat/docs/overview)
and
[API](https://cloud.google.com/compute/docs/reference/rest/beta/routers).

## Properties

`Name` - (Required) The `self_link` of the subnetwork to NAT.

`Router` - (Required) The name of the router in which this NAT will be configured. Changing this forces a new NAT to be created.

`NatIpAllocateOption` - (Required) How external IPs should be allocated for this NAT. Valid values are `AUTO_ONLY` or `MANUAL_ONLY`. Changing this forces a new NAT to be created.

`SourceSubnetworkIpRangesToNat` - (Required) How NAT should be configured per Subnetwork. Valid values include: `ALL_SUBNETWORKS_ALL_IP_RANGES`, `ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES`, `LIST_OF_SUBNETWORKS`. Changing this forces a new NAT to be created.

`NatIps` - (Optional) List of `self_link`s of external IPs. Only valid if `NatIpAllocateOption` is set to `MANUAL_ONLY`. Changing this forces a new NAT to be created.

`Subnetwork` - (Optional) One or more subnetwork NAT configurations. Only used if `SourceSubnetworkIpRangesToNat` is set to `LIST_OF_SUBNETWORKS`. See the section below for details on configuration.

`MinPortsPerVm` - (Optional) Minimum number of ports allocated to a VM from this NAT config. If not set, a default number of ports is allocated to a VM. Changing this forces a new NAT to be created.

`UdpIdleTimeoutSec` - (Optional) Timeout (in seconds) for UDP connections. Defaults to 30s if not set. Changing this forces a new NAT to be created.

`IcmpIdleTimeoutSec` - (Optional) Timeout (in seconds) for ICMP connections. Defaults to 30s if not set. Changing this forces a new NAT to be created.

`TcpEstablishedIdleTimeoutSec` - (Optional) Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set. Changing this forces a new NAT to be created.

`TcpTransitoryIdleTimeoutSec` - (Optional) Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set. Changing this forces a new NAT to be created.

`Project` - (Optional) The ID of the project in which this NAT's router belongs. If it is not provided, the provider project is used. Changing this forces a new NAT to be created.

`Region` - (Optional) The region this NAT's router sits in. If not specified, the project region will be used. Changing this forces a new NAT to be created.

`SourceIpRangesToNat` - (Required) List of options for which source IPs in the subnetwork should have NAT enabled. Supported values include: `ALL_IP_RANGES`, `LIST_OF_SECONDARY_IP_RANGES`, `PRIMARY_IP_RANGE`.

`SecondaryIpRangeNames` - (Optional) List of the secondary ranges of the subnetwork that are allowed to use NAT. This can be populated only if `LIST_OF_SECONDARY_IP_RANGES` is one of the values in `SourceIpRangesToNat`.


## See Also

* [google_compute_router_nat](https://www.terraform.io/docs/providers/google/r/compute_router_nat.html) in the _Terraform Provider Documentation_