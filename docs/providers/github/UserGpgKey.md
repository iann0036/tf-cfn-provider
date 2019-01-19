# Terraform::GitHub::UserGpgKey

Provides a GitHub user's GPG key resource.

This resource allows you to add/remove GPG keys from your user account.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The GitHub ID of the GPG key, e.g. `401586`.

`KeyId` - The key ID of the GPG key, e.g. `3262EFF25BA0D270`.

## See Also

* [github_user_gpg_key](https://www.terraform.io/docs/providers/github/r/user_gpg_key.html) in the _Terraform Provider Documentation_