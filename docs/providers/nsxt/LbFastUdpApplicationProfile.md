# Terraform::NSXT::LbFastUdpApplicationProfile

Provides a resource to configure LB fast UDP application profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`IdleTimeout` - (Optional) Timeout in seconds to specify how long an idle UDP connection in ESTABLISHED state should be kept for this application before cleaning up. The default value will be 300 seconds.

`HaFlowMirroring` - (Optional) A boolean flag which reflects whether flow mirroring is enabled, and all the flows to the bounded virtual server are mirrored to the standby node. By default this is disabled.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb fast udp profile.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb fast udp profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_fast_udp_application_profile](https://www.terraform.io/docs/providers/nsxt/r/lb_fast_udp_application_profile.html) in the _Terraform Provider Documentation_