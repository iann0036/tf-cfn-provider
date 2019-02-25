# Terraform::Gitlab::ProjectCluster

This resource allows you to create and manage project clusters for your GitLab projects.
For further information on clusters, consult the [gitlab
documentation](https://docs.gitlab.com/ce/user/project/clusters/index.html).

## Properties

`Project` - (Required, string) The id of the project to add the cluster to.

`Name` - (Required, string) The name of cluster.

`Enabled` - (Optional, boolean) Determines if cluster is active or not. Defaults to `true`.

`KubernetesApiUrl` - (Required, string) The URL to access the Kubernetes API.

`KubernetesToken` - (Required, string) The token to authenticate against Kubernetes.

`KubernetesCaCert` - (Optional, string) TLS certificate (needed if API is using a self-signed TLS certificate).

`KubernetesNamespace` - (Optional, string) The unique namespace related to the project.

`KubernetesAuthorizationType` - (Optional, string) The cluster authorization type. Valid values are `rbac`, `abac`, `unknown_authorization`. Defaults to `rbac`.

`EnvironmentScope` - (Optional, string) The associated environment to the cluster. Defaults to `*`.


## See Also

* [gitlab_project_cluster](https://www.terraform.io/docs/providers/gitlab/r/project_cluster.html) in the _Terraform Provider Documentation_