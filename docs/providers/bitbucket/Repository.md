# Terraform::Bitbucket::Repository

Provides a Bitbucket repository resource.

This resource allows you manage your repositories such as scm type, if it is
private, how to fork the repository and other options.

## Properties

`Owner` - (Required) The owner of this repository. Can be you or any team you have write access to.

`Name` - (Required) The name of the repository.

`Slug` - (Optional) The slug of the repository.

`Scm` - (Optional) What SCM you want to use. Valid options are hg or git. Defaults to git.

`IsPrivate` - (Optional) If this should be private or not. Defaults to `true`.

`Website` - (Optional) URL of website associated with this repository.

`Language` - (Optional) What the language of this repository should be.

`HasIssues` - (Optional) If this should have issues turned on or not.

`HasWiki` - (Optional) If this should have wiki turned on or not.

`ProjectKey` - (Optional) If you want to have this repo associated with a project.

`ForkPolicy` - (Optional) What the fork policy should be. Defaults to allow_forks.

`Description` - (Optional) What the description of the repo is.


## See Also

* [bitbucket_repository](https://www.terraform.io/docs/providers/bitbucket/r/repository.html) in the _Terraform Provider Documentation_