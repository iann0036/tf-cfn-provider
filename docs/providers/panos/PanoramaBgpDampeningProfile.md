# Terraform::Panos::PanoramaBgpDampeningProfile

This resource allows you to add/update/delete a Panorama BGP dampening profile.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`VirtualRouter` - (Required) The virtual router to add this BGP
dampening profile to.

`Name` - (Required) The name.

`Enable` - (Optional, bool) Enable or not (default: `true`).

`Cutoff` - (Optional, float) Cutoff threshold value (default: `1.25`).

`Reuse` - (Optional, float) Reuse threshold value (default: `0.5`).

`MaxHoldTime` - (Optional, int) Maximum hold-down time, in
seconds (default: `900`).

`DecayHalfLifeReachable` - (Optional, int) Decay half-life while
reachable, in seconds (default: `300`).

`DecayHalfLifeUnreachable` - (Optional, int) Decay half-life while
unreachable, in seconds (default: `900`).


## See Also

* [panos_panorama_bgp_dampening_profile](https://www.terraform.io/docs/providers/panos/r/panorama_bgp_dampening_profile.html) in the _Terraform Provider Documentation_