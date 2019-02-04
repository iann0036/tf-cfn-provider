# Terraform::Panos::NatRuleGroup

This resource allows you to add/update/delete a group of NAT rules.

This resource manages clusters of NAT rules in a single vsys,
enforcing both the contents of individual rules as well as their
ordering.  Rules are defined in a `Rule` config block.

Although you cannot modify non-group NAT rules with this
resource, the `PositionKeyword` and `PositionReference` parameters allow you
to reference some other NAT rule that already exists, using it as
a means to ensure some rough placement within the ruleset as a whole.

## Properties

`Vsys` - (Optional) The vsys to put the NAT rule group into (default:
`vsys1`).

`PositionKeyword` - (Optional) A positioning keyword for this group.  This
can be `before`, `directly before`, `after`, `directly after`, `top`,
`bottom`, or left empty (the default) to have no particular placement.  This
param works in combination with the `PositionReference` param.

`PositionReference` - (Optional) Required if `PositionKeyword` is one of the
"above" or "below" variants, this is the name of a non-group rule to use
as a reference to place this group.

`Rule` - (Repeatable) The rule definition (see below).  The rule
ordering will match how they appear in the terraform plan file.

### Rule Properties

`Name` - (Required) The NAT rule's name.

`Description` - (Optional) The description.

`Type` - (Optional). NAT type.  This can be `ipv4` (default), `nat64`, or
`nptv6`.

`Tags` - (Optional) List of administrative tags.

`Disabled` - (Optional) Set to `true` to disable this rule.

`OriginalPacket` - (Required) The original packet specification (see below).

`TranslatedPacket` - (Required) The translated packet spec (see below).

### OriginalPacket Properties

`SourceZones` - (Required) The list of source zone(s).

`DestinationZone` - (Required) The destination zone.

`DestinationInterface` - (Optional) Egress interface from route lookup (default:
`any`).

`Service` - (Optional) Service (default: `any`).

`SourceAddresses` - (Required) List of source address(es).

`DestinationAddresses` - (Required) List of destination address(es).

### TranslatedPacket Properties

`Source` - (Required) The source spec (see below).  Leave this
empty for a destination NAT of "none".

`Destination` - (Required) The destination spec (see below).  Leave this
empty for a destination NAT of "none".

`DynamicIpAndPort` - (Optional) Dynamic IP and port source translation
spec (see below).

`DynamicIp` - (Optional) Dynamic IP source translation spec (see below).

`StaticIp` - (Optional) Static IP source translation spec (see below).

`TranslatedAddress` - (Optional) Translated address source translation type
spec (see below).

`InterfaceAddress` - (Optional) Interface address source translation type
spec (see below).

`TranslatedAddresses` - (Required) List of translated addresses.

`Interface` - (Required) The interface.

`IpAddress` - (Optional) The IP address.

`TranslatedAddresses` - (Optional) The list of translated addresses.

`Fallback` - (Optional) The fallback spec (see below).  Leaving this empty
or omiting it means a fallback of "None".

`TranslatedAddress` - (Optional) The translated address fallback spec (see below).

`InterfaceAddress` - (Optional) The interface address fallback spec (see below).

`TranslatedAddresses` - (Optional) List of source address translation
fallback translated addresses.

`Interface` - (Required) Source address translation fallback interface.

`Type` - (Optional) Type of interface fallback.  Valid values are
`ip` (default) or `floating`.

`IpAddress` - (Optional) IP address of the fallback interface.

`TranslatedAddress` - (Required) The statically translated source
address.

`BiDirectional` - (Optional, bool) Set to `true` to enable
bi-directional source address translation.

`Static` - (Optional) Specifies a static destination NAT (see below).

`Dynamic` - (Optional, PAN-OS 8.1+) Specify a dynamic destination NAT
(see below).

`Address` - (Required) Destination address translation address.

`Port` - (Optional, int) Destination address translation port number.

`Address` - (Required) Destination address translation address.

`Port` - (Optional, int) Destination address translation port number.

`Distribution` - (Optional, PAN-OS 8.1+) Distribution algorithm
for destination address pool.  The PAN-OS 8.1 GUI doesn't seem to set this
anywhere, but this is added here for completeness' sake.  The GUI sets
this to `round-robin` currently.


## See Also

* [panos_nat_rule_group](https://www.terraform.io/docs/providers/panos/r/nat_rule_group.html) in the _Terraform Provider Documentation_