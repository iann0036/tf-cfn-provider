# Terraform::NSXT::IpSet

This resources provides a way to configure an IP set in NSX. An IP set is a collection of IP addresses. It is often used in the configuration of the NSX firewall.

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this IP set.

`IpAddresses` - (Optional) IP addresses.


## Return Values

### Fn::GetAtt

`Id` - ID of the IP set.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_ip_set](https://www.terraform.io/docs/providers/nsxt/r/ip_set.html) in the _Terraform Provider Documentation_