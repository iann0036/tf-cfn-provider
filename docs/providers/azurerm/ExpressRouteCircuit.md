# Terraform::AzureRM::ExpressRouteCircuit

Manages an ExpressRoute circuit.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Resource ID of the ExpressRoute circuit.

`ServiceProviderProvisioningState` - The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".

`ServiceKey` - The string needed by the service provider to provision the ExpressRoute circuit.

## See Also

* [azurerm_express_route_circuit](https://www.terraform.io/docs/providers/azurerm/r/express_route_circuit.html) in the _Terraform Provider Documentation_