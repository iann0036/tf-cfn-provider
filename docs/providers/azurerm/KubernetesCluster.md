# Terraform::AzureRM::KubernetesCluster

Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.

`Location` - (Required) The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.

`AgentPoolProfile` - (Required) One or more `AgentPoolProfile` blocks as documented below.

`DnsPrefix` - (Required) DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.

`ServicePrincipal` - (Required) A `ServicePrincipal` block as documented below.

`AddonProfile` - (Optional) A `AddonProfile` block.

`KubernetesVersion` - (Optional) Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

`LinuxProfile` - (Optional) A `LinuxProfile` block.

`NetworkProfile` - (Optional) A `NetworkProfile` block.

`RoleBasedAccessControl` - (Optional) A `RoleBasedAccessControl` block. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### AddonProfile Properties

`AciConnectorLinux` - (Optional) A `AciConnectorLinux` block. For more details, please visit [Create and configure an AKS cluster to use virtual nodes](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal).

`HttpApplicationRouting` - (Optional) A `HttpApplicationRouting` block.

`OmsAgent` - (Optional) A `OmsAgent` block. For more details, please visit [How to onboard Azure Monitor for containers](https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard).

### AgentPoolProfile Properties

`Name` - (Required) Unique name of the Agent Pool Profile in the context of the Subscription and Resource Group. Changing this forces a new resource to be created.

`Count` - (Required) Number of Agents (VMs) in the Pool. Possible values must be in the range of 1 to 100 (inclusive). Defaults to `1`.

`VmSize` - (Required) The size of each VM in the Agent Pool (e.g. `Standard_F1`). Changing this forces a new resource to be created.

`MaxPods` - (Optional) The maximum number of pods that can run on each agent.

`OsDiskSizeGb` - (Optional) The Agent Operating System disk size in GB. Changing this forces a new resource to be created.

`OsType` - (Optional) The Operating System used for the Agents. Possible values are `Linux` and `Windows`.  Changing this forces a new resource to be created. Defaults to `Linux`.

`VnetSubnetId` - (Optional) The ID of the Subnet where the Agents in the Pool should be provisioned. Changing this forces a new resource to be created.

`ClientAppId` - (Required) The Client ID of an Azure Active Directory Application. Changing this forces a new resource to be created.

`ServerAppId` - (Required) The Server ID of an Azure Active Directory Application. Changing this forces a new resource to be created.

`ServerAppSecret` - (Required) The Client Secret of an Azure Active Directory Application. Changing this forces a new resource to be created.

`TenantId` - (Optional) The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used. Changing this forces a new resource to be created.

### LinuxProfile Properties

`AdminUsername` - (Required) The Admin Username for the Cluster. Changing this forces a new resource to be created.

`SshKey` - (Required) One or more `SshKey` blocks. Changing this forces a new resource to be created.

### NetworkProfile Properties

`NetworkPlugin` - (Required) Network plugin to use for networking. Currently supported values are `azure` and `kubenet`. Changing this forces a new resource to be created.

`DnsServiceIp` - (Optional) IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when `NetworkPlugin` is set to `kubenet`. Changing this forces a new resource to be created.

`DockerBridgeCidr` - (Optional) IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when `NetworkPlugin` is set to `kubenet`. Changing this forces a new resource to be created.

`PodCidr` - (Optional) The CIDR to use for pod IP addresses. This field can only be set when `NetworkPlugin` is set to `kubenet`. Changing this forces a new resource to be created.

`ServiceCidr` - (Optional) The Network Range used by the Kubernetes service. This is required when `NetworkPlugin` is set to `kubenet`. Changing this forces a new resource to be created.

### OmsAgent Properties

`Enabled` - (Required) Is the OMS Agent Enabled?.

`LogAnalyticsWorkspaceId` - (Required) The ID of the Log Analytics Workspace which the OMS Agent should send data to.

### AciConnectorLinux Properties

`Enabled` - (Required) Is the virtual node addon enabled?.

`SubnetName` - (Required) The subnet name for the virtual nodes to run.

### RoleBasedAccessControl Properties

`AzureActiveDirectory` - (Optional) An `AzureActiveDirectory` block. Changing this forces a new resource to be created.

`Enabled` - (Required) Is Role Based Access Control Enabled? Changing this forces a new resource to be created.

### ServicePrincipal Properties

`ClientId` - (Required) The Client ID for the Service Principal. Changing this forces a new resource to be created.

`ClientSecret` - (Required) The Client Secret for the Service Principal. Changing this forces a new resource to be created.

### SshKey Properties

`KeyData` - (Required) The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The Kubernetes Managed Cluster ID.

`Fqdn` - The FQDN of the Azure Kubernetes Managed Cluster.

`KubeAdminConfig` - A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.

`KubeAdminConfigRaw` - Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.

`KubeConfig` - A `kube_config` block as defined below.

`KubeConfigRaw` - Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools.

`HttpApplicationRouting` - A `HttpApplicationRouting` block as defined below.

`NodeResourceGroup` - The auto-generated Resource Group which contains the resources for this Managed Kubernetes Cluster.

`HttpApplicationRoutingZoneName` - The Zone Name of the HTTP Application Routing.

`ClientKey` - Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.

`ClientCertificate` - Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.

`ClusterCaCertificate` - Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.

`Host` - The Kubernetes cluster server host.

`Username` - A username used to authenticate to the Kubernetes cluster.

`Password` - A password or token used to authenticate to the Kubernetes cluster.

## See Also

* [azurerm_kubernetes_cluster](https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster.html) in the _Terraform Provider Documentation_