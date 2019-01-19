# Terraform::AzureRM::ApplicationGateway

Manages an Application Gateway.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the URL Path Map.

`AuthenticationCertificate` - A list of `authentication_certificate` blocks as defined below.

`BackendAddressPool` - A list of `backend_address_pool` blocks as defined below.

`BackendHttpSettings` - A list of `backend_http_settings` blocks as defined below.

`FrontendIpConfiguration` - A list of `frontend_ip_configuration` blocks as defined below.

`FrontendPort` - A list of `frontend_port` blocks as defined below.

`GatewayIpConfiguration` - A list of `gateway_ip_configuration` blocks as defined below.

`HttpListener` - A list of `http_listener` blocks as defined below.

`Probe` - A `probe` block as defined below.

`RequestRoutingRule` - A list of `request_routing_rule` blocks as defined below.

`SslCertificate` - A list of `ssl_certificate` blocks as defined below.

`UrlPathMap` - A list of `url_path_map` blocks as defined below.

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

`PathRule` - A list of `path_rule` blocks as defined above.

## See Also

* [azurerm_application_gateway](https://www.terraform.io/docs/providers/azurerm/r/application_gateway.html) in the _Terraform Provider Documentation_