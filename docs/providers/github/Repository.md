# Terraform::GitHub::Repository

This resource allows you to create and manage repositories within your
GitHub organization.

This resource cannot currently be used to manage *personal* repositories,
outside of organizations.

## Properties

`Name` - (Required) The name of the repository.

`Description` - (Optional) A description of the repository.

`HomepageUrl` - (Optional) URL of a page describing the project.

`Private` - (Optional) Set to `true` to create a private repository. Repositories are created as public (e.g. open source) by default.

`HasIssues` - (Optional) Set to `true` to enable the GitHub Issues features on the repository.

`HasProjects` - (Optional) Set to `true` to enable the GitHub Projects features on the repository. Per the github [documentation](https://developer.github.com/v3/repos/#create) when in an organization that has disabled repository projects it will default to `false` and will otherwise default to `true`. If you specify `true` when it has been disabled it will return an error.

`HasWiki` - (Optional) Set to `true` to enable the GitHub Wiki features on the repository.

`AllowMergeCommit` - (Optional) Set to `false` to disable merge commits on the repository.

`AllowSquashMerge` - (Optional) Set to `false` to disable squash merges on the repository.

`AllowRebaseMerge` - (Optional) Set to `false` to disable rebase merges on the repository.

`HasDownloads` - (Optional) Set to `true` to enable the (deprecated) downloads features on the repository.

`AutoInit` - (Optional) Meaningful only during create; set to `true` to produce an initial commit in the repository.

`GitignoreTemplate` - (Optional) Meaningful only during create, will be ignored after repository creation. Use the [name of the template](https://github.com/github/gitignore) without the extension. For example, "Haskell".

`LicenseTemplate` - (Optional) Meaningful only during create, will be ignored after repository creation. Use the [name of the template](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) without the extension. For example, "mit" or "mpl-2.0".

`DefaultBranch` - (Optional) The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created, and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the initial repository creation and create the target branch inside of the repository prior to setting this attribute.

`Archived` - (Optional) Specifies if the repository should be archived. Defaults to `false`.

`Topics` - (Optional) The list of topics of the repository.


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