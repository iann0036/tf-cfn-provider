# Terraform::AzureRM::KubernetesCluster

Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Kubernetes Managed Cluster ID.

`Fqdn` - The FQDN of the Azure Kubernetes Managed Cluster.

`KubeAdminConfig` - A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.

`KubeAdminConfigRaw` - Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.

`KubeConfig` - A `kube_config` block as defined below.

`KubeConfigRaw` - Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools.

`HttpApplicationRouting` - A `http_application_routing` block as defined below.

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