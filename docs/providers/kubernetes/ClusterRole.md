# Terraform::Kubernetes::ClusterRole

A ClusterRole creates a role at the cluster level and in all namespaces.

## Properties

`Metadata` - (Required) Standard kubernetes metadata. For more info see [Kubernetes reference](https://github.com/kubernetes/community/blob/master/contributors/devel/api-conventions.md#metadata)
- `Rule` - (Required) The PolicyRoles for this ClusterRole. For more info see [Kubernetes reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole).

`Rule` - (Required) The PolicyRoles for this ClusterRole. For more info see [Kubernetes reference](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole).


## See Also

* [kubernetes_cluster_role](https://www.terraform.io/docs/providers/kubernetes/r/cluster_role.html) in the _Terraform Provider Documentation_