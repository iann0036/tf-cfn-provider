# Terraform::GitHub::RepositoryDeployKey

Provides a GitHub repository deploy key resource.

A deploy key is an SSH key that is stored on your server and grants
access to a single GitHub repository. This key is attached directly to the repository instead of to a personal user
account.

This resource allows you to add/remove repository deploy keys.

Further documentation on GitHub repository deploy keys:
- [About deploy keys](https://developer.github.com/guides/managing-deploy-keys/#deploy-keys)

## Properties

`Key` - (Required) A ssh key.

`ReadOnly` - (Required) A boolean qualifying the key to be either read only or read/write.

`Repository` - (Required) Name of the GitHub repository.

`Title` - (Required) A title.


## See Also

* [github_repository_deploy_key](https://www.terraform.io/docs/providers/github/r/repository_deploy_key.html) in the _Terraform Provider Documentation_