# Terraform::NSXT::IpPool

Provides a resource to configure IP pool on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this IP pool.

`Subnet` - (Optional) Subnets can be IPv4 or IPv6 and they should not overlap. The maximum number will not exceed 5 subnets. Each subnet has the following arguments:.

`AllocationRanges` - (Required) A collection of IPv4 Pool Ranges.

`Cidr` - (Required) Network address and the prefix length which will be associated with a layer-2 broadcast domainIPv4 Pool Ranges.

`DnsNameservers` - (Optional) A collection of up to 3 DNS servers for the subnet.

`DnsSuffix` - (Optional) The DNS suffix for the DNS server.

`GatewayIp` - (Optional) The default gateway address on a layer-3 router.


## Return Values

### Fn::GetAtt

`Id` - ID of the IP pool.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_ip_pool](https://www.terraform.io/docs/providers/nsxt/r/ip_pool.html) in the _Terraform Provider Documentation_