# Terraform::Kubernetes::ConfigMap

The resource provides mechanisms to inject containers with configuration data while keeping containers agnostic of Kubernetes.
Config Map can be used to store fine-grained information like individual properties or coarse-grained information like entire config files or JSON blobs.

## Properties

`Data` - (Optional) A map of the configuration data.

`Metadata` - (Required) Standard config map's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).


## See Also

* [kubernetes_config_map](https://www.terraform.io/docs/providers/kubernetes/r/config_map.html) in the _Terraform Provider Documentation_