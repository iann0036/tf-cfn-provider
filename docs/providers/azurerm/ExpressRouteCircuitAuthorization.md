# Terraform::AzureRM::ExpressRouteCircuitAuthorization

Manages an ExpressRoute Circuit Authorization.

## Properties

`Name` - (Required) The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

`ExpressRouteCircuitName` - (Required) The name of the Express Route Circuit in which to create the Authorization.


## Return Values

### Fn::GetAtt

`Id` - The Resource ID of the ExpressRoute Circuit Authorization.

`AuthorizationKey` - The Authorization Key.

`AuthorizationUseStatus` - The authorization use status.

## See Also

* [azurerm_express_route_circuit_authorization](https://www.terraform.io/docs/providers/azurerm/r/express_route_circuit_authorization.html) in the _Terraform Provider Documentation_