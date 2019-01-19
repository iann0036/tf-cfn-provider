# Terraform::GitHub::Repository

This resource allows you to create and manage repositories within your
GitHub organization.

This resource cannot currently be used to manage *personal* repositories,
outside of organizations.

## Properties

TBC

## Return Values

### Fn::GetAtt

`FullName` - A string of the form "orgname/reponame".

`HtmlUrl` - URL to the repository on the web.

`SshCloneUrl` - URL that can be provided to `git clone` to clone the.

`HttpCloneUrl` - URL that can be provided to `git clone` to clone the.

`GitCloneUrl` - URL that can be provided to `git clone` to clone the.

`SvnUrl` - URL that can be provided to `svn checkout` to check out.

## See Also

* [github_repository](https://www.terraform.io/docs/providers/github/r/repository.html) in the _Terraform Provider Documentation_