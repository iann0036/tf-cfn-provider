# Terraform::Kubernetes::ClusterRoleBinding

A ClusterRoleBinding may be used to grant permission at the cluster level and in all namespaces

## Properties

`Metadata` - (Required) Standard kubernetes metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/e59e666e3464c7d4851136baa8835a311efdfb8e/contributors/devel/api-conventions.md#metadata).

`RoleRef` - (Required) The ClusterRole to bind Subjects to. For more info see [Kubernetes reference](https://kubernetes.io/docs/admin/authorization/rbac/#rolebinding-and-clusterrolebinding).

`Subject` - (Required) The Users, Groups, or ServiceAccounts to grand permissions to. For more info see [Kubernetes reference](https://kubernetes.io/docs/admin/authorization/rbac/#referring-to-subjects).


## See Also

* [kubernetes_cluster_role_binding](https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding.html) in the _Terraform Provider Documentation_