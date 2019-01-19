# Terraform::Bitbucket::Hook

Provides a Bitbucket hook resource.

This allows you to manage your webhooks on a repository.

## Properties

`Owner` - (Required) The owner of this repository. Can be you or any team you have write access to.

`Repository` - (Required) The name of the repository.

`Url` - (Required) Where to POST to.

`Description` - (Required) The name / description to show in the UI.

`Events` - (Required) The event you want to react on.


## See Also

* [bitbucket_hook](https://www.terraform.io/docs/providers/bitbucket/r/hook.html) in the _Terraform Provider Documentation_