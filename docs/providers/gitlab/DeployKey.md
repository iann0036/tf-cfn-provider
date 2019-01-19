# Terraform::Gitlab::DeployKey

This resource allows you to create and manage deploy keys for your GitLab projects.

## Properties

`Project` - (Required, string) The name or id of the project to add the deploy key to.

`Title` - (Required, string) A title to describe the deploy key with.

`Key` - (Required, string) The public ssh key body.

`CanPush` - (Optional, boolean) Allow this deploy key to be used to push changes to the project.  Defaults to `false`. **NOTE::** this cannot currently be managed.


## See Also

* [gitlab_deploy_key](https://www.terraform.io/docs/providers/gitlab/r/deploy_key.html) in the _Terraform Provider Documentation_