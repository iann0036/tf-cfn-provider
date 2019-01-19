# Terraform::NSXT::DhcpServerProfile

Provides a resource to configure DHCP server profile on NSX-T manager

## Properties

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`EdgeClusterId` - (Required) Edge cluster uuid.

`EdgeClusterMemberIndexes` - (Optional) Up to 2 edge nodes from the given cluster. If none is provided, the NSX will auto-select two edge-nodes from the given edge cluster. If user provides only one edge node, there will be no HA support.

`Tag` - (Optional) A list of scope + tag pairs to associate with this DHCP profile.


## Return Values

### Fn::GetAtt

`Id` - ID of the DHCP server profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_dhcp_server_profile](https://www.terraform.io/docs/providers/nsxt/r/dhcp_server_profile.html) in the _Terraform Provider Documentation_