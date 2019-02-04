# Terraform::Kubernetes::Daemonset

A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created.

## Properties

`Metadata` - (Required) Standard object metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/master/contributors/devel/api-conventions.md#metadata)
- `Spec` - (Required) Spec defines the specification of the desired behavior of the daemonset. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/master/contributors/devel/api-conventions.md#spec-and-status).

`Spec` - (Required) Spec defines the specification of the desired behavior of the daemonset. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/master/contributors/devel/api-conventions.md#spec-and-status).


## See Also

* [kubernetes_daemonset](https://www.terraform.io/docs/providers/kubernetes/r/daemonset.html) in the _Terraform Provider Documentation_