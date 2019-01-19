# Terraform::NSXT::LbFastTcpApplicationProfile

Provides a resource to configure LB fast TCP application profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`CloseTimeout` - (Optional) Timeout in seconds to specify how long a closed TCP connection should be kept for this application before cleaning up the connection. Value can range between 1-60, with a default of 8 seconds.

`IdleTimeout` - (Optional) Timeout in seconds to specify how long an idle TCP connection in ESTABLISHED state should be kept for this application before cleaning up. The default value will be 1800 seconds.

`HaFlowMirroring` - (Optional) A boolean flag which reflects whether flow mirroring is enabled, and all the flows to the bounded virtual server are mirrored to the standby node. By default this is disabled.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb fast tcp profile.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb fast tcp profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_fast_tcp_application_profile](https://www.terraform.io/docs/providers/nsxt/r/lb_fast_tcp_application_profile.html) in the _Terraform Provider Documentation_