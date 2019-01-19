# Terraform::Gitlab::GroupVariable

This resource allows you to create and manage CI/CD variables for your GitLab groups.
For further information on variables, consult the [gitlab
documentation](https://docs.gitlab.com/ce/ci/variables/README.html#variables).

## Properties

`Group` - (Required, string) The name or id of the group to add the hook to.

`Key` - (Required, string) The name of the variable.

`Value` - (Required, string) The value of the variable.

`Protected` - (Optional, boolean) If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.


## See Also

* [gitlab_group_variable](https://www.terraform.io/docs/providers/gitlab/r/group_variable.html) in the _Terraform Provider Documentation_