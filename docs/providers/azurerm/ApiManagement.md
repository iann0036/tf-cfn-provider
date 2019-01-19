# Terraform::AzureRM::ApiManagement

Manages an API Management Service.

## Properties

`ResourceGroupName` - (Required) The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.

`PublisherName` - (Required) The name of publisher/company.

`PublisherEmail` - (Required) The email of publisher/company.

`Sku` - (Required) A `Sku` block as documented below.

`AdditionalLocation` - (Optional) One or more `AdditionalLocation` blocks as defined below.

`Identity` - (Optional) An `Identity` block is documented below.

`HostnameConfiguration` - (Optional) A `HostnameConfiguration` block as defined below.

`NotificationSenderEmail` - (Optional) Email address from which the notification will be sent.

`Security` - (Optional) A `Security` block as defined below.

`Tags` - (Optional) A mapping of tags assigned to the resource.

### AdditionalLocation Properties

`Location` - (Required) The name of the Azure Region in which the API Management Service should be expanded to.

### Security Properties

`DisableBackendSsl30` - (Optional) Should SSL 3.0 be disabled on the backend of the gateway? Defaults to `false`.

`DisableBackendTls10` - (Optional) Should TLS 1.0 be disabled on the backend of the gateway? Defaults to `false`.

`DisableBackendTls11` - (Optional) Should TLS 1.1 be disabled on the backend of the gateway? Defaults to `false`.

`DisableFrontendSsl30` - (Optional) Should SSL 3.0 be disabled on the frontend of the gateway? Defaults to `false`.

`DisableFrontendTls10` - (Optional) Should TLS 1.0 be disabled on the frontend of the gateway? Defaults to `false`.

`DisableFrontendTls11` - (Optional) Should TLS 1.1 be disabled on the frontend of the gateway? Defaults to `false`.

`DisableTripleDesChipers` - (Optional) Should the `TLS_RSA_WITH_3DES_EDE_CBC_SHA` cipher be disabled for alL TLS versions (1.0, 1.1 and 1.2)? Defaults to `false`.

### Proxy Properties

`Certificate` - (Optional) The Base64 Encoded Certificate.

`CertificatePassword` - (Optional) The password associated with the certificate provided above.

`HostName` - (Required) The Hostname to use for the Management API.

`KeyVaultId` - (Optional) The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type `application/x-pkcs12`.

`NegotiateClientCertificate` - (Optional) Should Client Certificate Negotiation be enabled for this Hostname? Defaults to `false`.

`DefaultSslBinding` - (Optional) Is the certificate associated with this Hostname the Default SSL Certificate? This is used when an SNI header isn't specified by a client. Defaults to `false`.

### Certificate Properties

`EncodedCertificate` - (Required) The Base64 Encoded PFX Certificate.

`StoreName` - (Required) The name of the Certificate Store where this certificate should be stored. Possible values are `CertificateAuthority` and `Root`.

### HostnameConfiguration Properties

`Management` - (Optional) One or more `Management` blocks as documented below.

`Portal` - (Optional) One or more `Portal` blocks as documented below.

`Proxy` - (Optional) One or more `Proxy` blocks as documented below.

`Scm` - (Optional) One or more `Scm` blocks as documented below.

### Sku Properties

`Name` - (Required) Specifies the Pricing Tier for the API Management Service. Possible values include: `Developer`, `Basic`, `Standard` and `Premium`.

`Capacity` - (Required) Specifies the Pricing Capacity for the API Management Service.

### Identity Properties

`Type` - (Required) Specifies the type of Managed Service Identity that should be configured on this API Management Service. At this time the only supported value is`SystemAssigned`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the API Management Service.

`GatewayUrl` - The URL of the Gateway for the API Management Service.

`GatewayRegionalUrl` - The URL of the Regional Gateway for the API Management Service in the specified region.

`ManagementApiUrl` - The URL for the Management API associated with this API Management service.

`PortalUrl` - The URL for the Publisher Portal associated with this API Management service.

`PublicIpAddresses` - Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.

`ScmUrl` - The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.

`Identity` - An `Identity` block as defined below.

`AdditionalLocation` - One or more `AdditionalLocation` blocks as documented below.

`PrincipalId` - The Principal ID associated with this Managed Service Identity.

`TenantId` - The Tenant ID associated with this Managed Service Identity.

## See Also

* [azurerm_api_management](https://www.terraform.io/docs/providers/azurerm/r/api_management.html) in the _Terraform Provider Documentation_