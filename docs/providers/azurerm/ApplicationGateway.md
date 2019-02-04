# Terraform::AzureRM::ApplicationGateway

Manages an Application Gateway.

## Properties

`Name` - (Required) The name of the Application Gateway. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.

`Location` - (Required) The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.

`BackendAddressPool` - (Required) One or more `BackendAddressPool` blocks as defined below.

`BackendHttpSettings` - (Required) One or more `BackendHttpSettings` blocks as defined below.

`FrontendIpConfiguration` - (Required) One or more `FrontendIpConfiguration` blocks as defined below.

`FrontendPort` - (Required) One or more `FrontendPort` blocks as defined below.

`GatewayIpConfiguration` - (Required) One or more `GatewayIpConfiguration` blocks as defined below.

`HttpListener` - (Required) One or more `HttpListener` blocks as defined below.

`RequestRoutingRule` - (Required) One or more `RequestRoutingRule` blocks as defined below.

`Sku` - (Required) A `Sku` block as defined below.

`AuthenticationCertificate` - (Optional) One or more `AuthenticationCertificate` blocks as defined below.

`DisabledSslProtocols` - (Optional) A list of SSL Protocols which should be disabled on this Application Gateway. Possible values are `TLSv1_0`, `TLSv1_1` and `TLSv1_2`.

`Probe` - (Optional) One or more `Probe` blocks as defined below.

`SslCertificate` - (Optional) One or more `SslCertificate` blocks as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`UrlPathMap` - (Optional) One or more `UrlPathMap` blocks as defined below.

`WafConfiguration` - (Optional) A `WafConfiguration` block as defined below.

`CustomErrorConfiguration` - (Optional) One or more `CustomErrorConfiguration` blocks as defined below.

### AuthenticationCertificate Properties

`Name` - (Required) The Name of the Authentication Certificate to use.

`Data` - (Required) The contents of the Authentication Certificate which should be used.

`Name` - (Required) The name of the Authentication Certificate.

### BackendAddressPool Properties

`Name` - (Required) The name of the Backend Address Pool.

`Fqdns` - (Optional) A list of FQDN's which should be part of the Backend Address Pool.

`FqdnList` - (Optional **Deprecated**) A list of FQDN's which should be part of the Backend Address Pool. This field has been deprecated in favour of `Fqdns` and will be removed in v2.0 of the AzureRM Provider.

`IpAddresses` - (Optional) A list of IP Addresses which should be part of the Backend Address Pool.

`IpAddressList` - (Optional **Deprecated**) A list of IP Addresses which should be part of the Backend Address Pool. This field has been deprecated in favour of `IpAddresses` and will be removed in v2.0 of the AzureRM Provider.

### BackendHttpSettings Properties

`CookieBasedAffinity` - (Required) Is Cookie-Based Affinity enabled? Possible values are `Enabled` and `Disabled`.

`Name` - (Required) The name of the Backend HTTP Settings Collection.

`Port` - (Required) The port which should be used for this Backend HTTP Settings Collection.

`ProbeName` - (Required) The name of an associated HTTP Probe.

`Protocol` - (Required) The Protocol which should be used. Possible values are `Http` and `Https`.

`RequestTimeout` - (Required) The request timeout in seconds, which must be between 1 and 86400 seconds.

`PickHostNameFromBackendAddress` - (Optional) Whether host header should be picked from the host name of the backend server. Defaults to `false`.

`AuthenticationCertificate` - (Optional) One or more `AuthenticationCertificate` blocks.

### FrontendIpConfiguration Properties

`Name` - (Required) The name of the Frontend IP Configuration.

`SubnetId` - (Required) The ID of the Subnet which the Application Gateway should be connected to.

`PrivateIpAddress` - (Optional) The Private IP Address to use for the Application Gateway.

`PublicIpAddressId` - (Optional) The ID of a Public IP Address which the Application Gateway should use.

`PrivateIpAddressAllocation` - (Optional) The Allocation Method for the Private IP Address. Possible values are `Dynamic` and `Static`.

### FrontendPort Properties

`Name` - (Required) The name of the Frontend Port.

`Port` - (Required) The port used for this Frontend Port.

### GatewayIpConfiguration Properties

`Name` - (Required) The Name of this Gateway IP Configuration.

`SubnetId` - (Required) The ID of a Subnet.

### HttpListener Properties

`Name` - (Required) The Name of the HTTP Listener.

`FrontendIpConfigurationName` - (Required) The Name of the Frontend IP Configuration used for this HTTP Listener.

`FrontendPortName` - (Required) The Name of the Frontend Port use for this HTTP Listener.

`HostName` - (Optional) The Hostname which should be used for this HTTP Listener.

`Protocol` - (Required) The Protocol to use for this HTTP Listener. Possible values are `Http` and `Https`.

`RequireSni` - (Optional) Should Server Name Indication be Required? Defaults to `false`.

`SslCertificateName` - (Optional) The name of the associated SSL Certificate which should be used for this HTTP Listener.

`CustomErrorConfiguration` - (Optional) One or more `CustomErrorConfiguration` blocks as defined below.

`Body` - (Optional) A snippet from the Response Body which must be present in the Response. Defaults to `*`.

`StatusCode` - (Optional) A list of allowed status codes for this Health Probe.

`Name` - (Required) The Name of the Path Rule.

`Paths` - (Required) A list of Paths used in this Path Rule.

`BackendAddressPoolName` - (Required) The Name of the Backend Address Pool to use for this Path Rule.

`BackendHttpSettingsName` - (Required) The Name of the Backend HTTP Settings Collection to use for this Path Rule.

### Probe Properties

`Host` - (Optional) The Hostname used for this Probe. If the Application Gateway is configured for a single site, by default the Host name should be specified as ‘127.0.0.1’, unless otherwise configured in custom probe. Cannot be set if `PickHostNameFromBackendHttpSettings` is set to `true`.

`Interval` - (Required) The Interval between two consecutive probes in seconds. Possible values range from 1 second to a maximum of 86,400 seconds.

`Name` - (Required) The Name of the Probe.

`Protocol` - (Required) The Protocol used for this Probe. Possible values are `Http` and `Https`.

`Path` - (Required) The Path used for this Probe.

`Timeout` - (Required) The Timeout used for this Probe, which indicates when a probe becomes unhealthy. Possible values range from 1 second to a maximum of 86,400 seconds.

`UnhealthyThreshold` - (Required) The Unhealthy Threshold for this Probe, which indicates the amount of retries which should be attempted before a node is deemed unhealthy. Possible values are from 1 - 20 seconds.

`PickHostNameFromBackendHttpSettings` - (Optional) Whether the host header should be picked from the backend http settings. Defaults to `false`.

`Match` - (Optional) A `Match` block as defined above.

`MinimumServers` - (Optional) The minimum number of servers that are always marked as healthy. Defaults to `0`.

### RequestRoutingRule Properties

`Name` - (Required) The Name of this Request Routing Rule.

`RuleType` - (Required) The Type of Routing that should be used for this Rule. Possible values are `Basic` and `PathBasedRouting`.

`HttpListenerName` - (Required) The Name of the HTTP Listener which should be used for this Routing Rule.

`BackendAddressPoolName` - (Optional) The Name of the Backend Address Pool which should be used for this Routing Rule.

`BackendHttpSettingsName` - (Optional) The Name of the Backend HTTP Settings Collection which should be used for this Routing Rule.

`UrlPathMapName` - (Optional) The Name of the URL Path Map which should be associated with this Routing Rule.

### Sku Properties

`Name` - (Required) The Name of the SKU to use for this Application Gateway. Possible values are `Standard_Small`, `Standard_Medium`, `Standard_Large`, `Standard_v2`, `WAF_Medium`, `WAF_Large`, and `WAF_v2`.

`Tier` - (Required) The Tier of the SKU to use for this Application Gateway. Possible values are `Standard`, `Standard_v2`, `WAF` and `WAF_v2`.

`Capacity` - (Required) The Capacity of the SKU to use for this Application Gateway - which must be between 1 and 10.

### SslCertificate Properties

`Name` - (Required) The Name of the SSL certificate that is unique within this Application Gateway.

`Data` - (Required) PFX certificate.

`Password` - (Required) Password for the pfx file specified in data.

### UrlPathMap Properties

`Name` - (Required) The Name of the URL Path Map.

`DefaultBackendAddressPoolName` - (Required) The Name of the Default Backend Address Pool which should be used for this URL Path Map.

`DefaultBackendHttpSettingsName` - (Required) The Name of the Default Backend HTTP Settings Collection which should be used for this URL Path Map.

`PathRule` - (Required) One or more `PathRule` blocks as defined above.

### WafConfiguration Properties

`Enabled` - (Required) Is the Web Application Firewall be enabled?.

`FirewallMode` - (Required) The Web Application Firewall Mode. Possible values are `Detection` and `Prevention`.

`RuleSetType` - (Required) The Type of the Rule Set used for this Web Application Firewall.

`RuleSetVersion` - (Required) The Version of the Rule Set used for this Web Application Firewall.

`FileUploadLimitMb` - (Optional) The File Upload Limit in MB. Accepted values are in the range `1`MB to `500`MB. Defaults to `100`MB.

### CustomErrorConfiguration Properties

`StatusCode` - (Required) Status code of the application gateway customer error. Possible values are `HttpStatus403` and `HttpStatus502`.

`CustomErrorPageUrl` - (Required) Error page URL of the application gateway customer error.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Custom Error Configuration.

`AuthenticationCertificate` - A list of `AuthenticationCertificate` blocks as defined below.

`BackendAddressPool` - A list of `BackendAddressPool` blocks as defined below.

`BackendHttpSettings` - A list of `BackendHttpSettings` blocks as defined below.

`FrontendIpConfiguration` - A list of `FrontendIpConfiguration` blocks as defined below.

`FrontendPort` - A list of `FrontendPort` blocks as defined below.

`GatewayIpConfiguration` - A list of `GatewayIpConfiguration` blocks as defined below.

`Http2Enabled` - (Optional) Is HTTP2 enabled on the application gateway resource? Defaults to `false`.

`HttpListener` - A list of `HttpListener` blocks as defined below.

`Probe` - A `Probe` block as defined below.

`RequestRoutingRule` - A list of `RequestRoutingRule` blocks as defined below.

`SslCertificate` - A list of `SslCertificate` blocks as defined below.

`UrlPathMap` - A list of `UrlPathMap` blocks as defined below.

`CustomErrorConfiguration` - A list of `CustomErrorConfiguration` blocks as defined below.

`ProbeId` - The ID of the associated Probe.

`FrontendIpConfigurationId` - The ID of the associated Frontend Configuration.

`FrontendPortId` - The ID of the associated Frontend Port.

`SslCertificateId` - The ID of the associated SSL Certificate.

`BackendAddressPoolId` - The ID of the associated Backend Address Pool.

`BackendHttpSettingsId` - The ID of the associated Backend HTTP Settings Configuration.

`HttpListenerId` - The ID of the associated HTTP Listener.

`UrlPathMapId` - The ID of the associated URL Path Map.

`PublicCertData` - The Public Certificate Data associated with the SSL Certificate.

`DefaultBackendAddressPoolId` - The ID of the Default Backend Address Pool.

`DefaultBackendHttpSettingsId` - The ID of the Default Backend HTTP Settings Collection.

`PathRule` - A list of `PathRule` blocks as defined above.

## See Also

* [azurerm_application_gateway](https://www.terraform.io/docs/providers/azurerm/r/application_gateway.html) in the _Terraform Provider Documentation_