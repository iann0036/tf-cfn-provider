# Terraform::Kubernetes::ResourceQuota

A resource quota provides constraints that limit aggregate resource consumption per namespace. It can limit the quantity of objects that can be created in a namespace by type, as well as the total amount of compute resources that may be consumed by resources in that project.

## Properties

`Metadata` - (Required) Standard resource quota's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`Spec` - (Optional) Spec defines the desired quota. [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#spec-and-status).


## See Also

* [kubernetes_resource_quota](https://www.terraform.io/docs/providers/kubernetes/r/resource_quota.html) in the _Terraform Provider Documentation_