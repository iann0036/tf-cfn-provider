# Azure Stack Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/azurestack** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

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

* [Terraform::AzureStack::AvailabilitySet](AvailabilitySet.md)
* [Terraform::AzureStack::DnsARecord](DnsARecord.md)
* [Terraform::AzureStack::DnsZone](DnsZone.md)
* [Terraform::AzureStack::LbBackendAddressPool](LbBackendAddressPool.md)
* [Terraform::AzureStack::LbNatPool](LbNatPool.md)
* [Terraform::AzureStack::LbNatRule](LbNatRule.md)
* [Terraform::AzureStack::LbProbe](LbProbe.md)
* [Terraform::AzureStack::LbRule](LbRule.md)
* [Terraform::AzureStack::Lb](Lb.md)
* [Terraform::AzureStack::LocalNetworkGateway](LocalNetworkGateway.md)
* [Terraform::AzureStack::NetworkInterface](NetworkInterface.md)
* [Terraform::AzureStack::NetworkSecurityGroup](NetworkSecurityGroup.md)
* [Terraform::AzureStack::NetworkSecurityRule](NetworkSecurityRule.md)
* [Terraform::AzureStack::PublicIp](PublicIp.md)
* [Terraform::AzureStack::ResourceGroup](ResourceGroup.md)
* [Terraform::AzureStack::RouteTable](RouteTable.md)
* [Terraform::AzureStack::Route](Route.md)
* [Terraform::AzureStack::StorageAccount](StorageAccount.md)
* [Terraform::AzureStack::StorageBlob](StorageBlob.md)
* [Terraform::AzureStack::StorageContainer](StorageContainer.md)
* [Terraform::AzureStack::Subnet](Subnet.md)
* [Terraform::AzureStack::TemplateDeployment](TemplateDeployment.md)
* [Terraform::AzureStack::VirtualMachineExtension](VirtualMachineExtension.md)
* [Terraform::AzureStack::VirtualMachineScaleSet](VirtualMachineScaleSet.md)
* [Terraform::AzureStack::VirtualMachine](VirtualMachine.md)
* [Terraform::AzureStack::VirtualNetworkGatewayConnection](VirtualNetworkGatewayConnection.md)
* [Terraform::AzureStack::VirtualNetworkGateway](VirtualNetworkGateway.md)
* [Terraform::AzureStack::VirtualNetwork](VirtualNetwork.md)