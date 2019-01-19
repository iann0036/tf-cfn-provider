# Terraform::Gitlab::Project

This resource allows you to create and manage projects within your
GitLab group or within your user.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Integer that uniquely identifies the project within the gitlab install.

`SshUrlToRepo` - URL that can be provided to `git clone` to clone the.

`HttpUrlToRepo` - URL that can be provided to `git clone` to clone the.

`WebUrl` - URL that can be used to find the project in a browser.

## See Also

* [gitlab_project](https://www.terraform.io/docs/providers/gitlab/r/project.html) in the _Terraform Provider Documentation_