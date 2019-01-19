# Terraform::Kubernetes::Service

A Service is an abstraction which defines a logical set of pods and a policy by which to access them - sometimes called a micro-service.

## Properties

`Metadata` - (Required) Standard service's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Required) Spec defines the behavior of a service. [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#spec-and-status).


## See Also

* [kubernetes_service](https://www.terraform.io/docs/providers/kubernetes/r/service.html) in the _Terraform Provider Documentation_