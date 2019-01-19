# Terraform::AzureStack::LocalNetworkGateway

Manages a local network gateway connection over which specific connections can be configured.

## Properties

`Name` - (Required) The name of the local network gateway. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the local network gateway.

`Location` - (Required) The location/region where the local network gateway is created. Changing this forces a new resource to be created.

`GatewayAddress` - (Required) The IP address of the gateway to which to connect.

`AddressSpace` - (Required) The list of string CIDRs representing the address spaces the gateway exposes.

`BgpSettings` - (Optional) A `BgpSettings` block as defined below containing the Local Network Gateway's BGP speaker settings.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### BgpSettings Properties

`Asn` - (Required) The BGP speaker's ASN.

`BgpPeeringAddress` - (Required) The BGP peering address and BGP identifier of this BGP speaker.

`PeerWeight` - (Optional) The weight added to routes learned from this BGP speaker.


## Return Values

### Fn::GetAtt

`Id` - The local network gateway unique ID within Azure.

## See Also

* [azurestack_local_network_gateway](https://www.terraform.io/docs/providers/azurestack/r/local_network_gateway.html) in the _Terraform Provider Documentation_