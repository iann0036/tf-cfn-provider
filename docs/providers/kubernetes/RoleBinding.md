# Terraform::Kubernetes::RoleBinding

A RoleBinding may be used to grant permission at the namespace level

## Properties

`Metadata` - (Required) Standard kubernetes metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/master/contributors/devel/api-conventions.md#metadata).

`RoleRef` - (Required) The Role to bind Subjects to. For more info see [Kubernetes reference](https://kubernetes.io/docs/admin/authorization/rbac/#rolebinding-and-clusterrolebinding).

`Subject` - (Required) The Users, Groups, or ServiceAccounts to grand permissions to. For more info see [Kubernetes reference](https://kubernetes.io/docs/admin/authorization/rbac/#referring-to-subjects).


## See Also

* [kubernetes_role_binding](https://www.terraform.io/docs/providers/kubernetes/r/role_binding.html) in the _Terraform Provider Documentation_