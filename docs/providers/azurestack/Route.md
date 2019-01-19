# Terraform::AzureStack::Route

Manages a Route within a Route Table.

## Properties

`Name` - (Required) The name of the route. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the route. Changing this forces a new resource to be created.

`RouteTableName` - (Required) The name of the route table within which create the route. Changing this forces a new resource to be created.

`AddressPrefix` - (Required) The destination CIDR to which the route applies, such as `10.1.0.0/16`.

`NextHopType` - (Required) The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`.

`NextHopInIpAddress` - (Optional) Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.


## Return Values

### Fn::GetAtt

`Id` - The Route ID.

## See Also

* [azurestack_route](https://www.terraform.io/docs/providers/azurestack/r/route.html) in the _Terraform Provider Documentation_