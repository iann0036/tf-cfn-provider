# Terraform::Kubernetes::PersistentVolume

The resource provides a piece of networked storage in the cluster provisioned by an administrator. It is a resource in the cluster just like a node is a cluster resource. Persistent Volumes have a lifecycle independent of any individual pod that uses the PV.

For more info see [Kubernetes reference](https://kubernetes.io/docs/concepts/storage/persistent-volumes)/

## Properties

`Metadata` - (Required) Standard persistent volume's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Required) Spec of the persistent volume owned by the cluster. See below.


## See Also

* [kubernetes_persistent_volume](https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume.html) in the _Terraform Provider Documentation_