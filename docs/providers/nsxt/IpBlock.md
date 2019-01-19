# Terraform::NSXT::IpBlock

Provides a resource to configure IP block on NSX-T manager

## Properties

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`Cidr` - (Required) Represents network address and the prefix length which will be associated with a layer-2 broadcast domain.

`Tag` - (Optional) A list of scope + tag pairs to associate with this IP block.


## Return Values

### Fn::GetAtt

`Id` - ID of the IP block.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_ip_block](https://www.terraform.io/docs/providers/nsxt/r/ip_block.html) in the _Terraform Provider Documentation_