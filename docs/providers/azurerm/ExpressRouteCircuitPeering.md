# Terraform::AzureRM::ExpressRouteCircuitPeering

Manages an ExpressRoute Circuit Peering.

## Properties

`PeeringType` - (Required) The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.

`ExpressRouteCircuitName` - (Required) The name of the ExpressRoute Circuit in which to create the Peering.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.

`PrimaryPeerAddressPrefix` - (Optional) A `/30` subnet for the primary link.

`SecondaryPeerAddressPrefix` - (Optional) A `/30` subnet for the secondary link.

`VlanId` - (Optional) A valid VLAN ID to establish this peering on.

`SharedKey` - (Optional) The shared key. Can be a maximum of 25 characters.

`PeerAsn` - (Optional) The Either a 16-bit or a 32-bit ASN. Can either be public or private..

`MicrosoftPeeringConfig` - (Optional) A `MicrosoftPeeringConfig` block as defined below. Required when `PeeringType` is set to `MicrosoftPeering`.

### MicrosoftPeeringConfig Properties

`AdvertisedPublicPrefixes` - (Required) A list of Advertised Public Prefixes.


## Return Values

### Fn::GetAtt

`Id` - The Resource ID of the ExpressRoute Circuit Peering.

`AzureAsn` - The ASN used by Azure.

`PrimaryAzurePort` - The Primary Port used by Azure for this Peering.

`SecondaryAzurePort` - The Secondary Port used by Azure for this Peering.

## See Also

* [azurerm_express_route_circuit_peering](https://www.terraform.io/docs/providers/azurerm/r/express_route_circuit_peering.html) in the _Terraform Provider Documentation_