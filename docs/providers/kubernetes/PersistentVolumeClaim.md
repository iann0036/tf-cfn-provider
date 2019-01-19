# Terraform::Kubernetes::PersistentVolumeClaim

This resource allows the user to request for and claim to a persistent volume.

## Properties

`Metadata` - (Required) Standard persistent volume claim's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Required) Spec defines the desired characteristics of a volume requested by a pod author. For more info see [Kubernetes reference](http://kubernetes.io/docs/user-guide/persistent-volumes#persistentvolumeclaims).

`WaitUntilBound` - (Optional) Whether to wait for the claim to reach `Bound` state (to find volume in which to claim the space).


## See Also

* [kubernetes_persistent_volume_claim](https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_claim.html) in the _Terraform Provider Documentation_