# Terraform::Panos::BgpConditionalAdv

This resource allows you to add/update/delete a Panorama BGP conditional advertisement.

~> **Note:** In the PAN-OS GUI, this resource cannot be created without also
creating at least one non-exist filter and one advertise filter.  The API behaves
a little differently:  you can create the conditional advertisement itself, but
the API will start throwing errors if you try to update it and there is not at
least one non-exist filter and one advertise filter.  In order for a conditional
advertisement to be valid, you must specify at least one non-exist and one
advertise filter.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`VirtualRouter` - (Required) The virtual router to add this BGP
conditional advertisement to.

`Name` - (Required) The name.

`Enable` - (Optional, bool) Enable or not (default: `true`).

`UsedBy` - (Optional) List of BGP peer groups that use this rule.


## See Also

* [panos_bgp_conditional_adv](https://www.terraform.io/docs/providers/panos/r/bgp_conditional_adv.html) in the _Terraform Provider Documentation_