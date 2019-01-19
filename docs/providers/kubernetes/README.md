# Kubernetes Provider

##Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/kubernetes**. The below arguments may be included as the key/value or JSON properties in the secret:

* `host` - (Optional) The hostname (in form of URI) of Kubernetes master. Can be sourced from `KUBE_HOST`. Defaults to `https://localhost`.
* `username` - (Optional) The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Can be sourced from `KUBE_USER`.
* `password` - (Optional) The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Can be sourced from `KUBE_PASSWORD`.
* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate. Can be sourced from `KUBE_INSECURE`. Defaults to `false`.
* `client_certificate` - (Optional) PEM-encoded client certificate for TLS authentication. Can be sourced from `KUBE_CLIENT_CERT_DATA`.
* `client_key` - (Optional) PEM-encoded client certificate key for TLS authentication. Can be sourced from `KUBE_CLIENT_KEY_DATA`.
* `cluster_ca_certificate` - (Optional) PEM-encoded root certificates bundle for TLS authentication. Can be sourced from `KUBE_CLUSTER_CA_CERT_DATA`.
* `config_path` - (Optional) Path to the kube config file. Can be sourced from `KUBE_CONFIG` or `KUBECONFIG`. Defaults to `~/.kube/config`.
* `config_context` - (Optional) Context to choose from the config file. Can be sourced from `KUBE_CTX`.
* `config_context_auth_info` - (Optional) Authentication info context of the kube config (name of the kubeconfig user, `--user` flag in `kubectl`). Can be sourced from `KUBE_CTX_AUTH_INFO`.
* `config_context_cluster` - (Optional) Cluster context of the kube config (name of the kubeconfig cluster, `--cluster` flag in `kubectl`). Can be sourced from `KUBE_CTX_CLUSTER`.
* `token` - (Optional) Token of your service account.  Can be sourced from `KUBE_TOKEN`.
* `load_config_file` - (Optional) By default the local config (~/.kube/config) is loaded when you use this provider. This option at false disable this behaviour. Can be sourced from `KUBE_LOAD_CONFIG_FILE`.



## Supported Resources

* [Terraform::Kubernetes::ClusterRoleBinding](docs/providers/kubernetes/ClusterRoleBinding.md)
* [Terraform::Kubernetes::ConfigMap](docs/providers/kubernetes/ConfigMap.md)
* [Terraform::Kubernetes::Deployment](docs/providers/kubernetes/Deployment.md)
* [Terraform::Kubernetes::HorizontalPodAutoscaler](docs/providers/kubernetes/HorizontalPodAutoscaler.md)
* [Terraform::Kubernetes::LimitRange](docs/providers/kubernetes/LimitRange.md)
* [Terraform::Kubernetes::Namespace](docs/providers/kubernetes/Namespace.md)
* [Terraform::Kubernetes::NetworkPolicy](docs/providers/kubernetes/NetworkPolicy.md)
* [Terraform::Kubernetes::PersistentVolumeClaim](docs/providers/kubernetes/PersistentVolumeClaim.md)
* [Terraform::Kubernetes::PersistentVolume](docs/providers/kubernetes/PersistentVolume.md)
* [Terraform::Kubernetes::Pod](docs/providers/kubernetes/Pod.md)
* [Terraform::Kubernetes::ReplicationController](docs/providers/kubernetes/ReplicationController.md)
* [Terraform::Kubernetes::ResourceQuota](docs/providers/kubernetes/ResourceQuota.md)
* [Terraform::Kubernetes::RoleBinding](docs/providers/kubernetes/RoleBinding.md)
* [Terraform::Kubernetes::Role](docs/providers/kubernetes/Role.md)
* [Terraform::Kubernetes::Secret](docs/providers/kubernetes/Secret.md)
* [Terraform::Kubernetes::ServiceAccount](docs/providers/kubernetes/ServiceAccount.md)
* [Terraform::Kubernetes::Service](docs/providers/kubernetes/Service.md)
* [Terraform::Kubernetes::StatefulSet](docs/providers/kubernetes/StatefulSet.md)
* [Terraform::Kubernetes::StorageClass](docs/providers/kubernetes/StorageClass.md)