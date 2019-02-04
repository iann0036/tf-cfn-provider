# Terraform::Kubernetes::StorageClass

Storage class is the foundation of dynamic provisioning, allowing cluster administrators to define abstractions for the underlying storage platform.

Read more at http://blog.kubernetes.io/2017/03/dynamic-provisioning-and-storage-classes-kubernetes.html

## Properties

`Metadata` - (Required) Standard storage class's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Parameters` - (Optional) The parameters for the provisioner that should create volumes of this storage class.
Read more about [available parameters](https://kubernetes.io/docs/concepts/storage/storage-classes/#parameters).

`StorageProvisioner` - (Required) Indicates the type of the provisioner.

`ReclaimPolicy` - (Optional) Indicates the reclaim policy to use.  If no reclaimPolicy is specified when a StorageClass object is created, it will default to Delete.


## See Also

* [kubernetes_storage_class](https://www.terraform.io/docs/providers/kubernetes/r/storage_class.html) in the _Terraform Provider Documentation_