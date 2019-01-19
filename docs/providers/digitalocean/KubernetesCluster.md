# Terraform::DigitalOcean::KubernetesCluster

~> **NOTE:** DigitalOcean Kubernetes is currently in [Limited Availability](https://www.digitalocean.com/docs/platform/product-lifecycle/). In order to access its API, you must first by enable Kubernetes on your account by opting-in via the [cloud control panel](https://cloud.digitalocean.com/kubernetes/clusters). While the Kubernetes Cluster functionality is currently in limited availability the structure of this resource may change over time. Please share any feedback you may have by [opening an issue on GitHub](https://github.com/terraform-providers/terraform-provider-digitalocean/issues).

Provides a DigitalOcean Kubernetes cluster resource. This can be used to create, delete, and modify clusters. For more information see the [official documentation](https://www.digitalocean.com/docs/kubernetes/).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - A unique ID that can be used to identify and reference a Kubernetes cluster.

`ClusterSubnet` - The range of IP addresses in the overlay network of the Kubernetes cluster.

`ServiceSubnet` - The range of assignable IP addresses for services running in the Kubernetes cluster.

`Ipv4Address` - The public IPv4 address of the Kubernetes master node.

`Endpoint` - The base URL of the API server on the Kubernetes master node.

`Status` -  A string indicating the current status of the cluster. Potential values include running, provisioning, and errored.

`CreatedAt` - The date and time when the Kubernetes cluster was created.

`UpdatedAt` - The date and time when the Kubernetes cluster was last updated.

`KubeConfig.0` - A representation of the Kubernetes cluster's kubeconfig with the following attributes:.

`NodePool` - In addition to the arguments provided, these additional attributes about the cluster's default node pool are exported:.

## See Also

* [digitalocean_kubernetes_cluster](https://www.terraform.io/docs/providers/digitalocean/r/kubernetes_cluster.html) in the _Terraform Provider Documentation_