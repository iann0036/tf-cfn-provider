# Terraform::SelVPC::ResellCrossregionSubnetV2

Manages a V2 Cross-region subnet resource within Resell Selectel VPC.

## Properties

`ProjectId` - (Required) An associated Selectel VPC project. Changing this
creates a new Cross-region subnet.

`Regions` - (Required) An array of regions where the Cross-region subnet resides.
Changing this creates a new Cross-region subnet. The structure is described below.

`Cidr` - (Required) A cross-region subnet CIDR representation. Changing this
creates a new Cross-region subnet.

### Regions Properties

`Region` - (Required) A region of where the Cross-region subnet resides.
Changing this creates a new Cross-region subnet.


## Return Values

### Fn::GetAtt

`Servers` - Shows information about servers that use this Cross-region subnet. Contains.

`Status` - Shows if the Cross-region subnet is used or not.

`Subnets` - Shows information about OpenStack Networking subnets that use this.

`VlanId` - Shows id of the associated VLAN in the OpenStack Networking service for.

## See Also

* [selvpc_resell_crossregion_subnet_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_crossregion_subnet_v2.html) in the _Terraform Provider Documentation_