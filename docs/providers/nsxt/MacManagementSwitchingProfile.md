# Terraform::NSXT::MacManagementSwitchingProfile

Provides a resource to configure MAC management switching profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this MAC management switching profile.

`MacChangeAllowed` - (Optional) A boolean flag indicating allowing source MAC address change.

`MacLearning` - (Optional) Mac learning configuration:.

`Enabled` - (Optional) A boolean flag indicating allowing source MAC address learning.

`UnicastFloodingAllowed` - (Optional) A boolean flag indicating allowing flooding for unlearned MAC for ingress traffic. Can be True only if mac_learning is enabled.

`Limit` - (Optional) The maximum number of MAC addresses that can be learned on this port.

`LimitPolicy` - (Optional) The policy after MAC Limit is exceeded: ALLOW/DROP.


## Return Values

### Fn::GetAtt

`Id` - ID of the MAC management switching profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_mac_management_switching_profile](https://www.terraform.io/docs/providers/nsxt/r/mac_management_switching_profile.html) in the _Terraform Provider Documentation_