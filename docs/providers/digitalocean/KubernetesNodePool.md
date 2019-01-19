# Terraform::DigitalOcean::KubernetesNodePool

~> **NOTE:** DigitalOcean Kubernetes is currently in [Limited Availability](https://www.digitalocean.com/docs/platform/product-lifecycle/). In order to access its API, you must first by enable Kubernetes on your account by opting-in via the [cloud control panel](https://cloud.digitalocean.com/kubernetes/clusters). While the Kubernetes Cluster functionality is currently in limited availability the structure of this resource may change over time. Please share any feedback you may have by [opening an issue on GitHub](https://github.com/terraform-providers/terraform-provider-digitalocean/issues).

Provides a DigitalOcean Kubernetes node pool resource. While the default node pool must be defined in the `digitalocean_kubernetes_cluster` resource, this resource can be used to add additional ones to a cluster.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` -  A unique ID that can be used to identify and reference the node pool.

`Nodes` - A list of nodes in the pool. Each node exports the following attributes:.

## See Also

* [digitalocean_kubernetes_node_pool](https://www.terraform.io/docs/providers/digitalocean/r/kubernetes_node_pool.html) in the _Terraform Provider Documentation_