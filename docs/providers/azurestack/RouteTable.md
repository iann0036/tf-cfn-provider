# Terraform::AzureStack::RouteTable

Manages a Route Table

## Properties

`Name` - (Required) The name of the route table. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the route table. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Route` - (Optional) Can be specified multiple times to define multiple routes. Each `Route` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Route Properties

`Name` - (Required) The name of the route.

`AddressPrefix` - (Required) The destination CIDR to which the route applies, such as 10.1.0.0/16.

`NextHopType` - (Required) The type of Azure hop the packet should be sent to. Possible values are `VirtualNetworkGateway`, `VnetLocal`, `Internet`, `VirtualAppliance` and `None`.

`NextHopInIpAddress` - (Optional) Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is `VirtualAppliance`.


## Return Values

### Fn::GetAtt

`Id` - The Route Table ID.

`Subnets` - The collection of Subnets associated with this route table.

## See Also

* [azurestack_route_table](https://www.terraform.io/docs/providers/azurestack/r/route_table.html) in the _Terraform Provider Documentation_