# Terraform::CloudStack::EgressFirewall

Creates egress firewall rules for a given network.

## Properties

`NetworkId` - (Required) The network ID for which to create the egress
firewall rules. Changing this forces a new resource to be created.

`Managed` - (Optional) USE WITH CAUTION! If enabled all the egress firewall
rules for this network will be managed by this resource. This means it will
delete all firewall rules that are not in your config! (defaults false).

`Rule` - (Optional) Can be specified multiple times. Each rule block supports
fields documented below. If `managed = false` at least one rule is required!.

### Rule Properties

`CidrList` - (Required) A CIDR list to allow access to the given ports.

`Protocol` - (Required) The name of the protocol to allow. Valid options are:
`tcp`, `udp` and `icmp`.

`IcmpType` - (Optional) The ICMP type to allow. This can only be specified if
the protocol is ICMP.

`IcmpCode` - (Optional) The ICMP code to allow. This can only be specified if
the protocol is ICMP.

`Ports` - (Optional) List of ports and/or port ranges to allow. This can only
be specified if the protocol is TCP or UDP.


## Return Values

### Fn::GetAtt

`Id` - The network ID for which the egress firewall rules are created.

## See Also

* [cloudstack_egress_firewall](https://www.terraform.io/docs/providers/cloudstack/r/egress_firewall.html) in the _Terraform Provider Documentation_