# Terraform::Kubernetes::LimitRange

Limit Range sets resource usage limits (e.g. memory, cpu, storage) for supported kinds of resources in a namespace.

Read more in [the official docs](https://kubernetes.io/docs/tasks/configure-pod-container/apply-resource-quota-limit/#applying-default-resource-requests-and-limits).

## Properties

`Metadata` - (Required) Standard limit range's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Optional) Spec defines the limits enforced. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#spec-and-status).


## See Also

* [kubernetes_limit_range](https://www.terraform.io/docs/providers/kubernetes/r/limit_range.html) in the _Terraform Provider Documentation_