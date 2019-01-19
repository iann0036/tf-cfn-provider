# Terraform::SelVPC::ResellVrrpSubnetV2

Manages a V2 VRRP subnet resource within Resell Selectel VPC.

## Properties

`ProjectId` - (Required) An associated Selectel VPC project. Changing this creates a new VRRP subnet.

`MasterRegion` - (Required) A master region of where the VRRP subnet resides. Changing this creates a new VRRP subnet.

`SlaveRegion` - (Required) A slave region of where the VRRP subnet resides. Changing this creates a new VRRP subnet.

`PrefixLength` - (Optional) A prefix length of the VRRP subnet. Defaults to 29. Changing this creates a new VRRP subnet.

`IpVersion` - (Optional) A version of the IP protocol of the VRRP subnet. Defaults to "ipv4". Changing this creates a new VRRP subnet.


## Return Values

### Fn::GetAtt

`Cidr` - Shows VRRP subnet CIDR representation.

`Subnets` - Shows information about OpenStack Networking subnets that use this.

`Status` - Shows if the VRRP subnet is used or not.

`Servers` - Shows information about servers that use this VRRP subnet. Contains.

## See Also

* [selvpc_resell_vrrp_subnet_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_vrrp_subnet_v2.html) in the _Terraform Provider Documentation_