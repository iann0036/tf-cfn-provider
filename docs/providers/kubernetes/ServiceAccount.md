# Terraform::Kubernetes::ServiceAccount

A service account provides an identity for processes that run in a Pod.

Read more at [Kubernetes reference](https://kubernetes.io/docs/admin/service-accounts-admin)/

## Properties

`Metadata` - (Required) Standard service account's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`ImagePullSecret` - (Optional) A list of references to secrets in the same namespace to use for pulling any images in pods that reference this Service Account. For more info see [Kubernetes reference](http://kubernetes.io/docs/user-guide/secrets#manually-specifying-an-imagepullsecret).

`Secret` - (Optional) A list of secrets allowed to be used by pods running using this Service Account. For more info see [Kubernetes reference](http://kubernetes.io/docs/user-guide/secrets).

`AutomountServiceAccountToken` - (Optional) Boolean, `true` to enable automatic mounting of the service account token.


## Return Values

### Fn::GetAtt

`DefaultSecretName` - Name of the default secret, containing service account token, created & managed by the service.

## See Also

* [kubernetes_service_account](https://www.terraform.io/docs/providers/kubernetes/r/service_account.html) in the _Terraform Provider Documentation_