# Terraform::GitHub::UserSshKey

Provides a GitHub user's SSH key resource.

This resource allows you to add/remove SSH keys from your user account.

## Properties

`Title` - (Required) A descriptive name for the new key. e.g. `Personal MacBook Air`.

`Key` - (Required) The public SSH key to add to your GitHub account.


## Return Values

### Fn::GetAtt

`Id` - The ID of the SSH key.

`Url` - The URL of the SSH key.

## See Also

* [github_user_ssh_key](https://www.terraform.io/docs/providers/github/r/user_ssh_key.html) in the _Terraform Provider Documentation_