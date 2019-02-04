# Terraform::Panos::NatRule

This resource allows you to add/update/delete NAT rules.

~> **Note:** This resource has been deprecated.  Please use
`Terraform::Panos::NatRuleGroup` instead.

~> **Note:** `Terraform::Panos::NatPolicy` is known as `panosNatRule`.

The prefix `sat` stands for "Source Address Translation" while the prefix "dat"
stands for "Destination Address Translation".  The order of the params in
this resource and their naming matches how the params are presented in
the GUI.  Thus, having a GUI window open while creating your resource
definition will simplify the process.

Note that while many of the params for this resource are optional in an
absolute sense, depending on what type of NAT you wish to configure, certain
params may become necessary to correctly configure the NAT rule.

## Properties

`Name` - (Required) The NAT rule's name.

`Vsys` - (Optional) The vsys to put the NAT rule into (default:
`vsys1`).

`Rulebase` - (Optional, Deprecated) The rulebase.  For firewalls, there is only the
`Rulebase` value (default), but on Panorama, there is also `pre-rulebase`
and `post-rulebase`.

`Description` - (Optional) The description.

`Type` - (Optional). NAT type.  This can be `ipv4` (default), `nat64`, or
`nptv6`.

`SourceZones` - (Required) The list of source zone(s).

`DestinationZone` - (Required) The destination zone.

`ToInterface` - (Optional) Egress interface from route lookup (default:
`any`).

`Service` - (Optional) Service (default: `any`).

`SourceAddresses` - (Required) List of source address(es).

`DestinationAddresses` - (Required) List of destination address(es).

`SatType` - (Optional) Type of source address translation.  This can be
`none` (default), `dynamic-ip-and-port`, `dynamic-ip`, or `static-ip`.

`SatAddressType` - (Optional) Source address translation address type.
This can be `interface-address` or `translated-address`.

`SatTranslatedAddresses` - (Optional) Source address translation list of
translated addresses.

`SatInterface` - (Optional) Source address translation interface.

`SatIpAddress` - (Optional) Source address translation IP address.

`SatFallbackType` - (Optional) Source address translation fallback type.
This can be `none`, `interface-address`, or `translated-address`.

`SatFallbackTranslatedAddresses` - (Optional) Source address translation
list of fallback translated addresses.

`SatFallbackInterface` - (Optional) Source address translation fallback
interface.

`SatFallbackIpType` - (Optional) Source address translation fallback
IP type.  This can be `ip` or `floating`.

`SatFallbackIpAddress` - (Optional) The source address translation
fallback IP address.

`SatStaticTranslatedAddress` - (Optional) The statically translated source
address.

`SatStaticBiDirectional` - (Optional) Set to `true` to enable
bi-directional source address translation.

`DatType` - (Optional) Destination address translation type.  This should
be either `static` or `dynamic`.  The `dynamic` option is only available on
PAN-OS 8.1+.

`DatAddress` - (Optional) Destination address translation's address.  Requires
`DatType` be set to "static" or "dynamic".

`DatPort` - (Optional) Destination address translation's port number.  Requires
`DatType` be set to "static" or "dynamic".

`DatDynamicDistribution` - (Optional, PAN-OS 8.1+) Distribution algorithm
for destination address pool.  The PAN-OS 8.1 GUI doesn't seem to set this
anywhere, but this is added here for completeness' sake.  Requires `DatType`
of "dynamic".

`Disabled` - (Optional) Set to `true` to disable this rule.

`Tags` - (Optional) List of administrative tags.


## See Also

* [panos_nat_rule](https://www.terraform.io/docs/providers/panos/r/nat_rule.html) in the _Terraform Provider Documentation_