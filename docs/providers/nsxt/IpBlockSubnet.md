# Terraform::NSXT::IpBlockSubnet

Provides a resource to configure IP block subnet on NSX-T manager

## Properties

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`BlockId` - (Required) Block id for which the subnet is created.

`Size` - (Required) Represents the size or number of IP addresses in the subnet.

`Tag` - (Optional) A list of scope + tag pairs to associate with this IP block subnet.


## Return Values

### Fn::GetAtt

`Id` - ID of the IP block subnet.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`AllocationRange` - A collection of IPv4 IP ranges used for IP allocation.

`Cidr` - Represents the size or number of IP addresses in the subnet. All subnets of the same block must have the same size, which must be a power of 2.

## See Also

* [nsxt_ip_block_subnet](https://www.terraform.io/docs/providers/nsxt/r/ip_block_subnet.html) in the _Terraform Provider Documentation_