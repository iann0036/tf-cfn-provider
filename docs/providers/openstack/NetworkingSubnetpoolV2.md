# Terraform::OpenStack::NetworkingSubnetpoolV2

Manages a V2 Neutron subnetpool resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client. A Networking client is needed to create a Neutron subnetpool. If omitted, the `Region` argument of the provider is used. Changing this creates a new subnetpool.

`Name` - (Required) The name of the subnetpool. Changing this updates the name of the existing subnetpool.

`DefaultQuota` - (Optional) The per-project quota on the prefix space that can be allocated from the subnetpool for project subnets. Changing this updates the default quota of the existing subnetpool.

`ProjectId` - (Optional) The owner of the subnetpool. Required if admin wants to create a subnetpool for another project. Changing this creates a new subnetpool.

`Prefixes` - (Required) A list of subnet prefixes to assign to the subnetpool. Neutron API merges adjacent prefixes and treats them as a single prefix. Each subnet prefix must be unique among all subnet prefixes in all subnetpools that are associated with the address scope. Changing this updates the prefixes list of the existing subnetpool.

`DefaultPrefixlen` - (Optional) The size of the prefix to allocate when the cidr or prefixlen attributes are omitted when you create the subnet. Defaults to the MinPrefixLen. Changing this updates the default prefixlen of the existing subnetpool.

`MinPrefixlen` - (Optional) The smallest prefix that can be allocated from a subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default is 64. Changing this updates the min prefixlen of the existing subnetpool.

`MaxPrefixlen` - (Optional) The maximum prefix size that can be allocated from the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools, default is 128. Changing this updates the max prefixlen of the existing subnetpool.

`AddressScopeId` - (Optional) The Neutron address scope to assign to the subnetpool. Changing this updates the address scope id of the existing subnetpool.

`Shared` - (Optional) Indicates whether this subnetpool is shared across all projects. Changing this updates the shared status of the existing subnetpool.

`Description` - (Optional) The human-readable description for the subnetpool. Changing this updates the description of the existing subnetpool.

`IsDefault` - (Optional) Indicates whether the subnetpool is default subnetpool or not. Changing this updates the default status of the existing subnetpool.

`ValueSpecs` - (Optional) Map of additional options.

`Tags` - (Optional) A set of string tags for the subnetpool.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`DefaultQuota` - See Properties above.

`ProjectId` - See Properties above.

`CreatedAt` - The time at which subnetpool was created.

`UpdatedAt` - The time at which subnetpool was created.

`Prefixes` - See Properties above.

`DefaultPrefixlen` - See Properties above.

`MinPrefixlen` - See Properties above.

`MaxPrefixlen` - See Properties above.

`AddressScopeId` - See Properties above.

`IpVersion` - The IP protocol version.

`Shared` - See Properties above.

`Description` - See Properties above.

`IsDefault` - See Properties above.

`RevisionNumber` - The revision number of the subnetpool.

`ValueSpecs` - See Properties above.

`Tags` - See Properties above.

## See Also

* [openstack_networking_subnetpool_v2](https://www.terraform.io/docs/providers/openstack/r/networking_subnetpool_v2.html) in the _Terraform Provider Documentation_