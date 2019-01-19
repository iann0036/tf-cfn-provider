# Terraform::Kubernetes::Role

A role contains rules that represent a set of permissions. Permissions are purely additive (there are no “deny” rules).

## Properties

`Metadata` - (Required) Standard role's metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/master/contributors/devel/api-conventions.md#metadata).

`Rule` - (Required) List of rules that define the set of permissions for this role. For more info see [Kubernetes reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).


## See Also

* [kubernetes_role](https://www.terraform.io/docs/providers/kubernetes/r/role.html) in the _Terraform Provider Documentation_