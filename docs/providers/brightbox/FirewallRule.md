# Terraform::Brightbox::FirewallRule

Provides a Brightbox Firewall Rule resource.

## Properties

`FirewallPolicy` - (Required) The ID of the firewall policy this rule belongs to.

`Protocol` - (Optional) Protocol Number or one of `tcp`, `udp`, `icmp`.

`Source` - (Optional) Subnet, ServerGroup or ServerID. `any`,`10.1.1.23/32` or `srv-4ktk4`.

`SourcePort` - (Optional) single port, multiple ports or range separated by `-` or `:`; upto 255 characters. Example - `80`, `80,443,21` or `3000-3999`.

`Destination` - (Optional) Subnet, ServerGroup or ServerID. `any`,`10.1.1.23/32` or `srv-4ktk4`.

`DestinationPort` - (Optional) single port, multiple ports or range separated by `-` or `:`; upto 255 characters. Example - `80`, `80,443,21` or `3000-3999`.

`IcmpTypeName` - (Optional) ICMP type name. `echo-request`, `echo-reply`. Only allowed if protocol is `icmp`.

`Description` - (Optional) A further description of the Firewall Rule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Firewall Rule.

## See Also

* [brightbox_firewall_rule](https://www.terraform.io/docs/providers/brightbox/r/firewall_rule.html) in the _Terraform Provider Documentation_