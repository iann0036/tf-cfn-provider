# Terraform::AzureRM::ContainerService

Manages an Azure Container Service Instance

~> **NOTE:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

~> **DEPRECATED:** [Azure Container Service (ACS) has been deprecated by Azure in favour of Azure (Managed) Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/updates/azure-container-service-will-retire-on-january-31-2020/). Support for ACS will be removed in the next major version of the AzureRM Provider (2.0) - and we **strongly recommend** you consider using [Azure Kubernetes Service (AKS)](kubernetes_cluster.html) for new deployments.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Container Service ID.

`MasterProfile.fqdn` - FDQN for the master.

`AgentPoolProfile.fqdn` - FDQN for the agent pool.

`DiagnosticsProfile.storageUri` - The URI of the storage account where diagnostics are stored.

## See Also

* [azurerm_container_service](https://www.terraform.io/docs/providers/azurerm/r/container_service.html) in the _Terraform Provider Documentation_