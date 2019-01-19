# Terraform::NSXT::IpDiscoverySwitchingProfile

Provides a resource to configure IP discovery switching profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this IP discovery switching profile.

`ArpSnoopingEnabled` - (Optional) A boolean flag iIndicates whether ARP snooping is enabled.

`VmToolsEnabled` - (Optional) A boolean flag iIndicates whether VM tools will be enabled. This option is only supported on ESX where vm-tools is installed.

`DhcpSnoopingEnabled` - (Optional) A boolean flag iIndicates whether DHCP snooping is enabled.

`ArpBindingsLimit` - (Optional) Limit for the amount of ARP bindings.


## Return Values

### Fn::GetAtt

`Id` - ID of the IP discovery switching profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_ip_discovery_switching_profile](https://www.terraform.io/docs/providers/nsxt/r/ip_discovery_switching_profile.html) in the _Terraform Provider Documentation_