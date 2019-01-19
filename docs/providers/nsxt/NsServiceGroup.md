# Terraform::NSXT::NsServiceGroup

Provides a resource to configure NS service group on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this NS service group.

`Members` - (Required) List of NSServices IDs that can be added as members to an NSServiceGroup. All members should be of the same L2 type: Ethernet, or Non Ethernet.


## Return Values

### Fn::GetAtt

`Id` - ID of the NS service group.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_ns_service_group](https://www.terraform.io/docs/providers/nsxt/r/ns_service_group.html) in the _Terraform Provider Documentation_