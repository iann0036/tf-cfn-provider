# Terraform::AzureRM::TrafficManagerEndpoint

Manages a Traffic Manager Endpoint.

## Properties

`Name` - (Required) The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the Traffic Manager endpoint.

`ProfileName` - (Required) The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.

`EndpointStatus` - (Optional) The status of the Endpoint, can be set to
either `Enabled` or `Disabled`. Defaults to `Enabled`.

`Type` - (Required) The Endpoint type, must be one of:
- `AzureEndpoints`
- `ExternalEndpoints`
- `NestedEndpoints`.

`Target` - (Optional) The FQDN DNS name of the target. This argument must be
provided for an endpoint of type `ExternalEndpoints`, for other types it
will be computed.

`TargetResourceId` - (Optional) The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
`AzureEndpoints` or `NestedEndpoints`.

`Weight` - (Optional) Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  `Weighted` traffic
routing method. Supports values between 1 and 1000.

`Priority` - (Optional) Specifies the priority of this Endpoint, this must be
specified for Profiles using the `Priority` traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.

`EndpointLocation` - (Optional) Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the `Performance` routing method
if the Endpoint is of either type `NestedEndpoints` or `ExternalEndpoints`.
For Endpoints of type `AzureEndpoints` the value will be taken from the
location of the Azure target resource.

`MinChildEndpoints` - (Optional) This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type `NestedEndpoints`
and defaults to `1`.

`GeoMappings` - (Optional) A list of Geographic Regions used to distribute traffic, such as `WORLD`, `UK` or `DE`. The same location can't be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault).


## Return Values

### Fn::GetAtt

`Id` - The Traffic Manager Endpoint id.

## See Also

* [azurerm_traffic_manager_endpoint](https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_endpoint.html) in the _Terraform Provider Documentation_