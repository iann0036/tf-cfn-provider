# Terraform::Panos::NatRule

This resource allows you to add/update/delete NAT rules.

~> **Note:** `panos_nat_policy` is known as `panos_nat_rule`.

The prefix `sat` stands for "Source Address Translation" while the prefix "dat"
stands for "Destination Address Translation".  The order of the params in
this resource and their naming matches how the params are presented in
the GUI.  Thus, having a GUI window open while creating your resource
definition will simplify the process.

Note that while many of the params for this resource are optional in an
absolute sense, depending on what type of NAT you wish to configure, certain
params may become necessary to correctly configure the NAT rule.

## Properties

TBC

## See Also

* [panos_nat_rule](https://www.terraform.io/docs/providers/panos/r/nat_rule.html) in the _Terraform Provider Documentation_