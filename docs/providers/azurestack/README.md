# Azure Stack Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/azurestack**. The below arguments may be included as the key/value or JSON properties in the secret:

* `arm_endpoint` - (Optional) The Azure Resource Manager Endpoint for your Azure Stack instance, for example `https://management.westus.mydomain.com`. This can also be sourceed from the `ARM_ENDPOINT` Environment Variable.

* `client_id` - (Optional) The Client ID which should be used. This can also be sourceed from the `ARM_CLIENT_ID` Environment Variable.

* `subscription_id` - (Optional) The Subscription ID which should be used. This can also be sourced from the `ARM_SUBSCRIPTION_ID` Environment Variable.

* `tenant_id` - (Optional) The Tenant ID which should be used. This can also be sourced from the `ARM_TENANT_ID` Environment Variable.

---

When authenticating as a Service Principal using a Client Certificate, the following fields can be set:

* `client_certificate_password` - (Optional) The password associated with the Client Certificate. This can also be sourced from the `ARM_CLIENT_CERTIFICATE_PASSWORD` Environment Variable.

* `client_certificate_path` - (Optional) The path to the Client Certificate associated with the Service Principal which should be used. This can also be sourced from the `ARM_CLIENT_CERTIFICATE_PATH` Environment Variable.

More information on [how to configure a Service Principal using a Client Certificate can be found in this guide](auth/service_principal_client_certificate.html).

---

When authenticating as a Service Principal using a Client Secret, the following fields can be set:

* `client_secret` - (Optional) The Client Secret which should be used. This can also be sourced from the `ARM_CLIENT_SECRET` Environment Variable.

More information on [how to configure a Service Principal using a Client Secret can be found in this guide](auth/service_principal_client_secret.html).

---

For some advanced scenarios, such as where more granular permissions are necessary - the following properties can be set:

* `skip_credentials_validation` - (Optional) Should the Azure Stack Provider skip verifying the credentials being used are valid? This can also be sourced from the `ARM_SKIP_CREDENTIALS_VALIDATION` Environment Variable. Defaults to `false`.

* `skip_provider_registration` - (Optional) Should the Azure Stack Provider skip registering any required Resource Providers? This can also be sourced from the `ARM_SKIP_PROVIDER_REGISTRATION` Environment Variable. Defaults to `false`.


## Supported Resources

* [Terraform::AzureStack::AvailabilitySet](docs/providers/azurestack/AvailabilitySet.md)
* [Terraform::AzureStack::DnsARecord](docs/providers/azurestack/DnsARecord.md)
* [Terraform::AzureStack::DnsZone](docs/providers/azurestack/DnsZone.md)
* [Terraform::AzureStack::LbBackendAddressPool](docs/providers/azurestack/LbBackendAddressPool.md)
* [Terraform::AzureStack::LbNatPool](docs/providers/azurestack/LbNatPool.md)
* [Terraform::AzureStack::LbNatRule](docs/providers/azurestack/LbNatRule.md)
* [Terraform::AzureStack::LbProbe](docs/providers/azurestack/LbProbe.md)
* [Terraform::AzureStack::LbRule](docs/providers/azurestack/LbRule.md)
* [Terraform::AzureStack::Lb](docs/providers/azurestack/Lb.md)
* [Terraform::AzureStack::LocalNetworkGateway](docs/providers/azurestack/LocalNetworkGateway.md)
* [Terraform::AzureStack::NetworkInterface](docs/providers/azurestack/NetworkInterface.md)
* [Terraform::AzureStack::NetworkSecurityGroup](docs/providers/azurestack/NetworkSecurityGroup.md)
* [Terraform::AzureStack::NetworkSecurityRule](docs/providers/azurestack/NetworkSecurityRule.md)
* [Terraform::AzureStack::PublicIp](docs/providers/azurestack/PublicIp.md)
* [Terraform::AzureStack::ResourceGroup](docs/providers/azurestack/ResourceGroup.md)
* [Terraform::AzureStack::RouteTable](docs/providers/azurestack/RouteTable.md)
* [Terraform::AzureStack::Route](docs/providers/azurestack/Route.md)
* [Terraform::AzureStack::StorageAccount](docs/providers/azurestack/StorageAccount.md)
* [Terraform::AzureStack::StorageBlob](docs/providers/azurestack/StorageBlob.md)
* [Terraform::AzureStack::StorageContainer](docs/providers/azurestack/StorageContainer.md)
* [Terraform::AzureStack::Subnet](docs/providers/azurestack/Subnet.md)
* [Terraform::AzureStack::TemplateDeployment](docs/providers/azurestack/TemplateDeployment.md)
* [Terraform::AzureStack::VirtualMachineExtension](docs/providers/azurestack/VirtualMachineExtension.md)
* [Terraform::AzureStack::VirtualMachineScaleSet](docs/providers/azurestack/VirtualMachineScaleSet.md)
* [Terraform::AzureStack::VirtualMachine](docs/providers/azurestack/VirtualMachine.md)
* [Terraform::AzureStack::VirtualNetworkGatewayConnection](docs/providers/azurestack/VirtualNetworkGatewayConnection.md)
* [Terraform::AzureStack::VirtualNetworkGateway](docs/providers/azurestack/VirtualNetworkGateway.md)
* [Terraform::AzureStack::VirtualNetwork](docs/providers/azurestack/VirtualNetwork.md)