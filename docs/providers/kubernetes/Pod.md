# Terraform::Kubernetes::Pod

A pod is a group of one or more containers, the shared storage for those containers, and options about how to run the containers. Pods are always co-located and co-scheduled, and run in a shared context.

Read more at [Kubernetes reference](https://kubernetes.io/docs/concepts/workloads/pods/pod)/

## Properties

`Metadata` - (Required) Standard pod's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Required) Spec of the pod owned by the cluster.


## See Also

* [kubernetes_pod](https://www.terraform.io/docs/providers/kubernetes/r/pod.html) in the _Terraform Provider Documentation_