# Terraform::SelVPC::ResellSubnetV2

Manages a V2 subnet resource within Resell Selectel VPC.

## Properties

`ProjectId` - (Required) An associated Selectel VPC project. Changing this
creates a new subnet.

`Region` - (Required) A region of where the subnet resides. Changing this
creates a new subnet.

`PrefixLength` - (Optional) A prefix length of the subnet. Defaults to 29.
Changing this creates a new subnet.

`IpVersion` - (Optional) A version of the IP protocol of the subnet. Defaults
to "ipv4". Changing this creates a new subnet.


## Return Values

### Fn::GetAtt

`Cidr` - Shows subnet CIDR representation.

`NetworkId` - Shows associated OpenStack Networking service network ID.

`SubnetId` - Shows associated OpenStack Networking service subnet ID.

`Status` - Shows if the subnet is used or not.

`Servers` - Shows information about servers that use this subnet. Contains.

## See Also

* [selvpc_resell_subnet_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_subnet_v2.html) in the _Terraform Provider Documentation_