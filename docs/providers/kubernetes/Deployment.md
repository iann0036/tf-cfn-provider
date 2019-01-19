# Terraform::Kubernetes::Deployment

A Deployment ensures that a specified number of pod “replicas” are running at any one time. In other words, a Deployment makes sure that a pod or homogeneous set of pods are always up and available. If there are too many pods, it will kill some. If there are too few, the Deployment will start more.

## Properties

`Metadata` - (Required) Standard deployment's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Required) Spec defines the specification of the desired behavior of the deployment. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#spec-and-status).


## See Also

* [kubernetes_deployment](https://www.terraform.io/docs/providers/kubernetes/r/deployment.html) in the _Terraform Provider Documentation_