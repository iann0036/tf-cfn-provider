# Terraform::Panos::BgpAuthProfile

This resource allows you to add/update/delete a BGP auth profile.

## Properties

`VirtualRouter` - (Required) The virtual router to add this BGP
auth profile to.

`Name` - (Required) The name.

`Secret` - (Optional) Shared secret for the TCP MD5 authentication.


## See Also

* [panos_bgp_auth_profile](https://www.terraform.io/docs/providers/panos/r/bgp_auth_profile.html) in the _Terraform Provider Documentation_