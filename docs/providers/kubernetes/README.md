# Kubernetes Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/kubernetes** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `host` - (Optional) The hostname (in form of URI) of Kubernetes master. Defaults to `https://localhost`.
* `username` - (Optional) The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint.
* `password` - (Optional) The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.
* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate. Defaults to `false`.
* `client_certificate` - (Optional) PEM-encoded client certificate for TLS authentication.
* `client_key` - (Optional) PEM-encoded client certificate key for TLS authentication.
* `cluster_ca_certificate` - (Optional) PEM-encoded root certificates bundle for TLS authentication.
* `config_path` - (Optional) Path to the kube config file. Defaults to `~/.kube/config`.
* `config_context` - (Optional) Context to choose from the config file.
* `config_context_auth_info` - (Optional) Authentication info context of the kube config (name of the kubeconfig user, `--user` flag in `kubectl`).
* `config_context_cluster` - (Optional) Cluster context of the kube config (name of the kubeconfig cluster, `--cluster` flag in `kubectl`).
* `token` - (Optional) Token of your service account.
* `load_config_file` - (Optional) By default the local config (~/.kube/config) is loaded when you use this provider. This option at false disable this behaviour.



## Supported Resources

* [Terraform::Kubernetes::ClusterRoleBinding](ClusterRoleBinding.md)
* [Terraform::Kubernetes::ClusterRole](ClusterRole.md)
* [Terraform::Kubernetes::ConfigMap](ConfigMap.md)
* [Terraform::Kubernetes::Daemonset](Daemonset.md)
* [Terraform::Kubernetes::Deployment](Deployment.md)
* [Terraform::Kubernetes::HorizontalPodAutoscaler](HorizontalPodAutoscaler.md)
* [Terraform::Kubernetes::LimitRange](LimitRange.md)
* [Terraform::Kubernetes::Namespace](Namespace.md)
* [Terraform::Kubernetes::NetworkPolicy](NetworkPolicy.md)
* [Terraform::Kubernetes::PersistentVolumeClaim](PersistentVolumeClaim.md)
* [Terraform::Kubernetes::PersistentVolume](PersistentVolume.md)
* [Terraform::Kubernetes::Pod](Pod.md)
* [Terraform::Kubernetes::ReplicationController](ReplicationController.md)
* [Terraform::Kubernetes::ResourceQuota](ResourceQuota.md)
* [Terraform::Kubernetes::RoleBinding](RoleBinding.md)
* [Terraform::Kubernetes::Role](Role.md)
* [Terraform::Kubernetes::Secret](Secret.md)
* [Terraform::Kubernetes::ServiceAccount](ServiceAccount.md)
* [Terraform::Kubernetes::Service](Service.md)
* [Terraform::Kubernetes::StatefulSet](StatefulSet.md)
* [Terraform::Kubernetes::StorageClass](StorageClass.md)