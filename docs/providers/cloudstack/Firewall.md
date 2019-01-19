# Terraform::CloudStack::Firewall

Creates firewall rules for a given IP address.

## Properties

`IpAddressId` - (Required) The IP address ID for which to create the firewall rules. Changing this forces a new resource to be created.

`Managed` - (Optional) USE WITH CAUTION! If enabled all the firewall rules for this IP address will be managed by this resource. This means it will delete all firewall rules that are not in your config! (defaults false).

`Rule` - (Optional) Can be specified multiple times. Each rule block supports fields documented below. If `managed = false` at least one rule is required!.

`CidrList` - (Required) A CIDR list to allow access to the given ports.

`Protocol` - (Required) The name of the protocol to allow. Valid options are: `tcp`, `udp` and `icmp`.

`IcmpType` - (Optional) The ICMP type to allow. This can only be specified if the protocol is ICMP.

`IcmpCode` - (Optional) The ICMP code to allow. This can only be specified if the protocol is ICMP.

`Ports` - (Optional) List of ports and/or port ranges to allow. This can only be specified if the protocol is TCP or UDP.


## Return Values

### Fn::GetAtt

`Id` - The IP address ID for which the firewall rules are created.

## See Also

* [cloudstack_firewall](https://www.terraform.io/docs/providers/cloudstack/r/firewall.html) in the _Terraform Provider Documentation_