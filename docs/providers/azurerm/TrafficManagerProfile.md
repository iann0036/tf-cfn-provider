# Terraform::AzureRM::TrafficManagerProfile

Manages a Traffic Manager Profile to which multiple endpoints can be attached.

## Properties

`Name` - (Required) The name of the virtual network. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the virtual network.

`ProfileStatus` - (Optional) The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.

`TrafficRoutingMethod` - (Required) Specifies the algorithm used to route traffic, possible values are: - `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint. - `Performance` - Traffic is routed via the User's closest Endpoint - `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value. - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

`Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint. - `Performance` - Traffic is routed via the User's closest Endpoint - `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value. - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

`Performance` - Traffic is routed via the User's closest Endpoint - `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value. - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

`Weighted` - Traffic is spread across Endpoints proportional to their `weight` value. - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

`Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.

`DnsConfig` - (Required) This block specifies the DNS configuration of the Profile, it supports the fields documented below.

`MonitorConfig` - (Required) This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### DnsConfig Properties

`RelativeName` - (Required) The relative domain name, this is combined with the domain name used by Traffic Manager to form the FQDN which is exported as documented below. Changing this forces a new resource to be created.

`Ttl` - (Required) The TTL value of the Profile used by Local DNS resolvers and clients.

### MonitorConfig Properties

`Protocol` - (Required) The protocol used by the monitoring checks, supported values are `HTTP`, `HTTPS` and `TCP`.

`Port` - (Required) The port number used by the monitoring checks.

`Path` - (Optional) The path used by the monitoring checks. Required when `Protocol` is set to `HTTP` or `HTTPS` - cannot be set when `Protocol` is set to `TCP`.


## Return Values

### Fn::GetAtt

`Id` - The Traffic Manager Profile id.

`Fqdn` - The FQDN of the created Profile.

## See Also

* [azurerm_traffic_manager_profile](https://www.terraform.io/docs/providers/azurerm/r/traffic_manager_profile.html) in the _Terraform Provider Documentation_