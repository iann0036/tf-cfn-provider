# Terraform::NSXT::SpoofguardSwitchingProfile

Provides a resource to configure spoofguard switching profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this spoofguard switching profile.

`AddressBindingWhitelistEnabled` - (Optional) A boolean flag indicating whether this profile overrides the default system wide settings for Spoof Guard when assigned to ports.


## Return Values

### Fn::GetAtt

`Id` - ID of the spoofguard switching profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_spoofguard_switching_profile](https://www.terraform.io/docs/providers/nsxt/r/spoofguard_switching_profile.html) in the _Terraform Provider Documentation_