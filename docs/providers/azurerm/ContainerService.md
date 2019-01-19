# Terraform::AzureRM::ContainerService

Manages an Azure Container Service Instance

~> **NOTE:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

~> **DEPRECATED:** [Azure Container Service (ACS) has been deprecated by Azure in favour of Azure (Managed) Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/updates/azure-container-service-will-retire-on-january-31-2020/). Support for ACS will be removed in the next major version of the AzureRM Provider (2.0) - and we **strongly recommend** you consider using [Azure Kubernetes Service (AKS)](kubernetes_cluster.html) for new deployments.

## Properties

`Name` - (Required) The name of the Container Service instance to create. Changing this forces a new resource to be created.

`Location` - (Required) The location where the Container Service instance should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

`OrchestrationPlatform` - (Required) Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

`MasterProfile` - (Required) A Master Profile block as documented below.

`LinuxProfile` - (Required) A Linux Profile block as documented below.

`AgentPoolProfile` - (Required) A Agent Pool Profile's block as documented below.

`ServicePrincipal` - (only Required when you're using `Kubernetes` as an Orchestration Platform) A Service Principal block as documented below.

`DiagnosticsProfile` - (Required) A VM Diagnostics Profile block as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### MasterProfile Properties

`Count` - (Required) Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1.

`DnsPrefix` - (Required) The DNS Prefix to use for the Container Service master nodes.

### LinuxProfile Properties

`AdminUsername` - (Required) The Admin Username for the Cluster.

`SshKey` - (Required) An SSH Key block as documented below.

### SshKey Properties

`KeyData` - (Required) The Public SSH Key used to access the cluster.

### AgentPoolProfile Properties

`Name` - (Required) Unique name of the agent pool profile in the context of the subscription and resource group.

`Count` - (Required) Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.

`DnsPrefix` - (Required) The DNS Prefix given to Agents in this Agent Pool.

`VmSize` - (Required) The VM Size of each of the Agent Pool VM's (e.g. Standard_F1 / Standard_D2v2).

### ServicePrincipal Properties

`ClientId` - (Required) The ID for the Service Principal.

`ClientSecret` - (Required) The secret password associated with the service principal.

### DiagnosticsProfile Properties

`Enabled` - (Required) Should VM Diagnostics be enabled for the Container Service VM's.


## Return Values

### Fn::GetAtt

`Id` - The Container Service ID.

`MasterProfile.fqdn` - FDQN for the master.

`AgentPoolProfile.fqdn` - FDQN for the agent pool.

`DiagnosticsProfile.storageUri` - The URI of the storage account where diagnostics are stored.

## See Also

* [azurerm_container_service](https://www.terraform.io/docs/providers/azurerm/r/container_service.html) in the _Terraform Provider Documentation_