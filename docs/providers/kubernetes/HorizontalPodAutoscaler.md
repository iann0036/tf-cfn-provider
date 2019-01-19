# Terraform::Kubernetes::HorizontalPodAutoscaler

Horizontal Pod Autoscaler automatically scales the number of pods in a replication controller, deployment or replica set based on observed CPU utilization.

## Properties

`Metadata` - (Required) Standard horizontal pod autoscaler's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Required) Behaviour of the autoscaler. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#spec-and-status).


## See Also

* [kubernetes_horizontal_pod_autoscaler](https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler.html) in the _Terraform Provider Documentation_