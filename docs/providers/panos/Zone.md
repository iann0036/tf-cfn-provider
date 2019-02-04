# Terraform::Panos::Zone

This resource allows you to add/update/delete zones.

This resource has some overlap with the `Terraform::Panos::ZoneEntry`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::Zone` spec does not define the
`Interfaces` field.

## Properties

`Name` - (Required) The zone's name.

`Vsys` - (Optional) The vsys to put the zone into (default: `vsys1`).

`Mode` - (Required) The zone's mode.  This can be `layer3`, `layer2`,
`virtual-wire`, `tap`, or `tunnel`.

`ZoneProfile` - (Optional) The zone protection profile.

`LogSetting` - (Optional) Log setting.

`EnableUserId` - (Optional) Boolean to enable user identification.

`Interfaces` - (Optional) List of interfaces to associated with this zone.

`IncludeAcls` - (Optional) Users from these addresses/subnets will
be identified.  This can be an address object, an address group, a single
IP address, or an IP address subnet.

`ExcludeAcls` - (Optional) Users from these addresses/subnets will not
be identified.  This can be an address object, an address group, a single
IP address, or an IP address subnet.


## See Also

* [panos_zone](https://www.terraform.io/docs/providers/panos/r/zone.html) in the _Terraform Provider Documentation_