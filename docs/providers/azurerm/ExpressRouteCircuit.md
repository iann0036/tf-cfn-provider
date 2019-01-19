# Terraform::AzureRM::ExpressRouteCircuit

Manages an ExpressRoute circuit.

## Properties

`Name` - (Required) The name of the ExpressRoute circuit. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ServiceProviderName` - (Required) The name of the ExpressRoute Service Provider.

`PeeringLocation` - (Required) The name of the peering location and **not** the Azure resource location.

`BandwidthInMbps` - (Required) The bandwidth in Mbps of the circuit being created.

`Sku` - (Required) A `Sku` block for the ExpressRoute circuit as documented below.

`AllowClassicOperations` - (Optional) Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Tier` - (Required) The service tier. Possible values are `Standard` or `Premium`.

`Family` - (Required) The billing mode for bandwidth. Possible values are `MeteredData` or `UnlimitedData`.


## Return Values

### Fn::GetAtt

`Id` - The Resource ID of the ExpressRoute circuit.

`ServiceProviderProvisioningState` - The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".

`ServiceKey` - The string needed by the service provider to provision the ExpressRoute circuit.

## See Also

* [azurerm_express_route_circuit](https://www.terraform.io/docs/providers/azurerm/r/express_route_circuit.html) in the _Terraform Provider Documentation_