# Terraform::AzureRM::SubnetRouteTableAssociation

Associates a [Route Table](route_table.html) with a [Subnet](subnet.html) within a [Virtual Network](virtual_network.html).

-> **NOTE:** Subnet `<->` Route Table associations currently need to be configured on both this resource and using the `RouteTableId` field on the `Terraform::AzureRM::Subnet` resource. The next major version of the AzureRM Provider (2.0) will remove the `RouteTableId` field from the `azurermSubnet` resource such that this resource is used to link resources in future.

## Properties

`RouteTableId` - (Required) The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.

`SubnetId` - (Required) The ID of the Subnet. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Subnet.

## See Also

* [azurerm_subnet_route_table_association](https://www.terraform.io/docs/providers/azurerm/r/subnet_route_table_association.html) in the _Terraform Provider Documentation_