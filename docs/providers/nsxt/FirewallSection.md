# Terraform::NSXT::FirewallSection

This resource provides a way to configure a firewall section on the NSX manager. A firewall section is a collection of firewall rules that are grouped together.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the firewall section.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`IsDefault` - A boolean flag which reflects whether a firewall section is default section or not. Each Layer 3 and Layer 2 section will have at least and at most one default section.

## See Also

* [nsxt_firewall_section](https://www.terraform.io/docs/providers/nsxt/r/firewall_section.html) in the _Terraform Provider Documentation_