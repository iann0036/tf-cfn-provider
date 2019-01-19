# Terraform::Panos::PanoramaNatRule

This resource allows you to add/update/delete Panorama NAT rules.

~> **Note:** `panos_panorama_nat_policy` is known as `panos_panorama_nat_rule`.

The prefix `sat` stands for "Source Address Translation" while the prefix "dat"
stands for "Destination Address Translation".  The order of the params in
this resource and their naming matches how the params are presented in
the GUI.  Thus, having a GUI window open while creating your resource
definition will simplify the process.

Note that while many of the params for this resource are optional in an
absolute sense, depending on what type of NAT you wish to configure, certain
params may become necessary to correctly configure the NAT rule.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_panorama_nat_rule](https://www.terraform.io/docs/providers/panos/r/panorama_nat_rule.html) in the _Terraform Provider Documentation_